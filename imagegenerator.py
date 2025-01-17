import boto3
import base64
import json
import os
import uuid
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from botocore.client import Config

def lambda_handler(event, context):
    # Stable Diffusion model details
    stable_diffusion_model_id = "stability.stable-diffusion-xl-v1"
    timeout_duration = 12

    # Initialize AWS clients
    bedrock_client = boto3.client("bedrock-runtime")
    s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))  # This is correct

    # Environment variables
    bucket_name = "imagegenerationbyjana"
    if not bucket_name:
        return {
            "statusCode": 500,
            "body": "BUCKET environment variable is not set."
        }

    try:
        # Parse request body
        request_body = json.loads(event['body'])
        prompt = request_body.get("prompt")
        style_preset = request_body.get("stylePreset")
        seed = int(request_body.get("seed", 0))

        if not prompt:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Prompt is required."})
            }

        # Prepare payload for Stable Diffusion model
        payload = prepare_request_payload(prompt, style_preset, seed)

        # Invoke Stable Diffusion model
        response = bedrock_client.invoke_model(
            body=json.dumps(payload),
            contentType='application/json',
            accept='application/json',
            modelId=stable_diffusion_model_id
        )

        response_data = json.loads(response['body'].read())
        results = response_data.get("artifacts", [])
        if not results:
            return {
                "statusCode": 500,
                "body": "No image generated."
            }

        base64_string = results[0].get("base64")
        if not base64_string:
            return {
                "statusCode": 500,
                "body": "No base64 image found in response."
            }

        # Upload image to S3 and generate pre-signed URL
        presigned_url = upload_image_to_s3_and_get_presigned_url(base64_string, bucket_name, timeout_duration, s3_client)

        return {
            "statusCode": 200,
            "body": json.dumps({"presigned_url": presigned_url})
        }

    except (NoCredentialsError, PartialCredentialsError):
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "AWS credentials not found or incomplete."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def prepare_request_payload(prompt, style_preset, seed):
    payload = {
        "text_prompts": [
            {"text": prompt}
        ],
        "seed": seed
    }
    if style_preset:
        payload["style_preset"] = style_preset
    return payload

def upload_image_to_s3_and_get_presigned_url(base64_string, bucket_name, timeout_duration, s3_client):
    file_name = f"generated_image_{uuid.uuid4().hex}.jpg"
    object_key = file_name

    # Decode base64 image
    image_data = base64.b64decode(base64_string)

    # Upload image to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=image_data,
        ContentType="image/jpeg"
    )

    # Generate pre-signed URL
    presigned_url = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": object_key},
        ExpiresIn=int(timeout_duration * 3600)
    )

    return presigned_url
