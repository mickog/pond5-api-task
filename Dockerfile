FROM node:16-alpine

RUN apk update

RUN npm install -g serverless; \
    npm install -g serverless-localstack;

WORKDIR /app
COPY serverless.yml ./
COPY handler.py ./
COPY dynamo.py ./
COPY localstack_endpoints.json ./

CMD ["sls","deploy" ]