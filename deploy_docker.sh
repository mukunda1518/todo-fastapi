#!/bin/bash


# Set AWS configuration variables
AWS_ACCESS_KEY_ID="AKIA2YICAK6TH2BRGCVT"
AWS_SECRET_ACCESS_KEY="d84YhuHB7gQMqPLUVqi6ql+luyNvhJuhN+tCVvXS"
AWS_REGION="ap-south-1"  # e.g., us-west-2
AWS_OUTPUT_FORMAT="json"

# Configure AWS CLI
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set region $AWS_REGION
aws configure set output $AWS_OUTPUT_FORMAT

# Variables
AWS_REGION="ap-south-1"                 # e.g., us-west-2
ACCOUNT_ID="739275462566"             # Your AWS Account ID
REPOSITORY_NAME="fastapi/todo-app"   # Name of the ECR repository
IMAGE_TAG="latest1.1"                       # Tag of the image to pull

# Authenticate Docker to the Amazon ECR registry
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

echo "Login success"

# Pull the Docker image from Amazon ECR
docker pull $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:$IMAGE_TAG

echo "Image pull success"

# Run the Docker container
docker run -d --name todo-app-container -p 8081:8000 $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:$IMAGE_TAG

echo "Container is now running."
