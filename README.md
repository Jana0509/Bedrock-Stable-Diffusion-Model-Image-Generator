# Bedrock-Stable-Diffusion-Model-Image-Generator
Generating the Image using Amazon Bedrock Stable diffusion Model

-------------------------------------------------------------------
## Introduction:
This Project demonstrates Creating the High Quality dynamic Image based on user input leveraging Amazon Bedrock Stable diffusion Model. User provides the Input from the Frontend which request goes to Serverless Container service called fargate which is running in Private subnets in multiple availability Zones for the High Availability and fault tolerant solution. ECS is fronted with the Application LOad balancer for the efficient traffic distribution and its avoid the containers get overwhelmed. NAT gateway are sitting in the public subnet and acts as a proxy for the private instances to communicate to the internet. All the components are deployed inside the Virtual Private Cloud in multiple avalability zones for the network isolation and High Secure solution.

------------------------------------------------------------------------
## Architecture

![Stable Diffusion Img](https://github.com/user-attachments/assets/baecf943-bb71-4517-be95-1dbd225ace02)

## Project Highlights:

1. Version Control:
   Leveraged Git and Github for the version control

2. Containerization:
   Containerized the static application using Docker to ensure consistent runtime environments.

3. Docker:
   Used Docker to create the Container Image for the static Application

4. ECS Cluster
   Created the Elastic Container Service Cluster to deploy the containerized App, ensuring scalability and resilience.

5. FARGATE
   Leveraged the Serverless mode of running the containers across multiple availability zones for High availability and used auto scaling for scaliblity.

6. TLS/SSL Encryption:
   Used SSL Certificate for the encryption of the request and response between client and server

7. AMAZON Certificate Manager:
   Created SSL/TLS certificate and stored in ACM

8. Route 53:
   Created the Domain and alais record points to the Application Load balancer

9. IAM:
   Configured IAM roles and policies for secure access control.

10. Load Balancer:
   Deployed a Network Load Balancer (NLB) in public subnets to distribute traffic efficiently across the cluster in multiple AZs.

11. VPC Setup:
    Designed a custom VPC with public, private, and database subnets across multiple Availability Zones.

12. AMAZON BEDROCK:
    Used Stability Diffusion Model of Amazon's Bedrock for creating the High Quality Images.

13. Lambda:
    Serverless function which executes the set of codes which performs the business logic

14. API Gateway:
    Used to create the API [get,post,put,delete] and acts as the gateway for the API request which routes to the correct destination

15. S3:
    Used to store the Image and create the presigned URL for the Images for Viewing.

------------------------------------------------------------------------------
## Understanding of Amazon's Bedrock Stable Diffusion Model:
  Amazon Bedrock is a fully-managed serverless service which provides high-performing Foundation Models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, and Stability AI. It provides the flexibility to use the Model based on the business requirement. We can build generative artificial intelligence (AI) applications with security, privacy, and responsible AI using Amazon Bedrock unified APIs.

  In this Project, we have created Image generator Application leveraging Stability AI diffusion model to generate the High Quality images. Stable Diffusion is one of the family of foundation models which is trained on vast image-text data. It enables generating high-fidelity images from descriptions. It generates images of high quality in virtually any art style and is a leading open model for photorealism.


------------------------------------------------------------------------------------------------
## Key Learning Outcomes:
1. Created the VPC from scratch with public and private subnets across multiple availibility zones for Highly secure, Available and Fault tolerant Solutions.

![image](https://github.com/user-attachments/assets/74713855-8f53-4c26-9375-08db1358ebc6)


2. Created the docker image for the static application and pushed the docker image to Elastic Conatiner Registry(ECR)

3. Created the Elastic Container Service Cluster for deploying the Containerized application.

4. Created and configure ECS Cluster to run ECS fargate container in the private subnet in both the AZ for High availabilty and fault tolerant.

5. Created the ECS tasks which contain the OS specification, Memory, Network for the container to run.

![image](https://github.com/user-attachments/assets/ca18126a-36fa-444a-8ccc-ef95d74f3842)


6. Created and configured Elastic Container Service for running the ECS tasks and used auto scaling for the tasks scalibility.

![image](https://github.com/user-attachments/assets/9a8e78df-34e4-4136-b4cd-19e42e15e7e4)


7. Created and configued the Load balancer to route traffic to the ECS.

![image](https://github.com/user-attachments/assets/1a736191-b073-4a0d-afcc-02f3bfbc10bb)


8. Created the Lambda service which contain python invokes the Stability diffusion model and stores the image in S3.

![image](https://github.com/user-attachments/assets/2b2a87a0-6b0e-4187-b90f-7df670f52b89)


9. Lambda is fronted with API gateway which helps in creating the API.

10. Generated the Presigned URL with the help of S3 and provided to the frontend(ECS fargate)

![image](https://github.com/user-attachments/assets/9c5a295a-ea23-4030-96be-996ac85bc353)

## Conclusion:
This AI image generation service leverages Amazon Bedrock’s Stable Diffusion model to generate high-quality images based on user prompts. From infrastructure design to deployment, this project showcases how scalable cloud architecture can power AI-driven applications.

  
