# pond5-api-task

## Prerequisites 
Please have Docker installed on the machine that will be running the applciation. Docker can be downloaded here https://docs.docker.com/get-docker/

## Running Application
`docker compose up`

## Hitting Endpoints
Download and import the pond5_items.postman_collection.json that is included in the repo. For base url in collection please set with endpoint from docker output
![alt text](https://github.com/mickog/pond5-api-task/blob/master/endpoint_image.png?raw=true)

## Project Description
I decided rather than go with a flask and mock db I would experiment with the Serverless Framework, Localstack, and Docker. I understand Pond5 are using AWS so using Localstack as a mock AWS environment seemed like a good idea. 

## Future Work
I really don't like that I am asking you guys to set the base url in the postman collection. As you may know API gateway sets a unique API ID on a new deploy. I had plans to give the API a custom domain name but unfortunatly discovered late into the project that this wasn't possible when using a combination Serverless, Docker and Localstack. 

I may add some unit tests here using boto3 and moto3 clients. This is what I usually use for writing tests for AWS resources.

Also would like to put some sort of security on the gateway such as Oauth or the like.
