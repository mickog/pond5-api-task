FROM node:16-alpine

RUN apk update

RUN npm install -g serverless; \
    npm install -g serverless-localstack;

WORKDIR /app
COPY serverless.yml ./
COPY handler.py ./
COPY dynamo.py ./
COPY localstack_endpoints.json ./

EXPOSE 3000
CMD ["sls","deploy" ]