# AWS-Serverless
AWS Services demo and handson


# Introduction 
Lambda function and steps to create a layer in lambda

# Getting Started
To run locally -
pip install -r requirements.txt


Steps to create a layer for deployment

pip install -r requirements.txt --target python
zip -r lambda_layer.zip python

upload it to s3 and then create a new layer or adda new layer in console.


# Steps to build and run docker image locally. 
docker build -t lambda-function .

docker run -v <path to aws creds>/.aws --env application_name=dev --env environment_name=dev  lambda-function