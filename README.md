# pond5-api-task

## Prerequisites 
Please have Docker installed on the machine that will be running the applciation. Docker can be downloaded here https://docs.docker.com/get-docker/

## Running Application
`docker compose up`

## Hitting Endpoints
Download and import the pond5_items.postman_collection.json that is included in the repo. For base url in collection please set with endpoint from docker sls output
![alt text](https://github.com/mickog/pond5-api-task/blob/master/endpoint_image.png?raw=true)

## Project Description
I decided rather than go with a flask and mock db I would experiment with the Serverless Framework, Localstack, and Docker. I understand Pond5 are using AWS so using Localstack as a mock AWS environment seemed like a good idea. 

## Future Work
I really don't like that I am asking you guys to set the base url in the postman collection as it is one more step for you to running my application. As you may know API gateway sets a unique API ID on a new deploy. So rather than me have this hosted as localhost:3000/path or something along them lines I have it hosted on a mock AWS API Gateway on localhost which will have a unique ID generated on each deploy of my mock Cloudformation Stack. I may try add a custom domain name, it's a little tricky with the combination of Serverless, Docker and Localstack running to map localhost to a custom domain, although I may take a further look at this. I made the decision to go with the mock AWS stuff because I know you use AWS as a cloud provider. 

I may add some unit tests here using boto3 and moto3 clients. This is what I usually use for writing tests for AWS resources.

Also would like to put some sort of security on the gateway such as Oauth or the like.
