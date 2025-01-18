# Bedrock-Stable-Diffusion-Model-Image-Generator
Generating the Image using Amazon Bedrock Stable diffusion Model

-------------------------------------------------------------------
## Introduction:
This Project demonstrates Creating the High Quality dynamic Image based on user input leveraging Amazon Bedrock Stable diffusion Model. User provides the Input from the Frontend which request goes to Serverless Container service called fargate which is running in Private subnets in multiple availability Zones for the High Availability and fault tolerant solution. ECS is fronted with the Application LOad balancer for the efficient traffic distribution and its avoid the containers get overwhelmed. NAT gateway are sitting in the public subnet and acts as a proxy for the private instances to communicate to the internet. All the components are deployed inside the Virtual Private Cloud in multiple avalability zones for the network isolation and High Secure solution.

------------------------------------------------------------------------
## Architecture

![Stable Diffusion Img](https://github.com/user-attachments/assets/baecf943-bb71-4517-be95-1dbd225ace02)

## Project Highlights:
