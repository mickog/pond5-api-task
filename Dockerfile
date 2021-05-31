# File: ./Dockerfile
FROM node:14.17.0-alpine
# Copy the package.json and package.lock.json file to the image
WORKDIR /usr/src/app
COPY package*.json ./
# Run `npm install` to install the dependencies in the 
# package.json file
RUN npm install
# Copy the contents of the project to the image
COPY . .
# This is the default port the serverless framework will 
# listen on when it starts
EXPOSE 3000
# These are just to remind me that these are the
# environment variables this project uses
# ENV AWS_ENDPOINT='http://localhost:8000'
# ENV AWS_REGION='us-west-1'
# ENV AWS_ACCESS_KEY_ID='from-dockerfile-fake-access-key'
# ENV AWS_SECRET_ACCESS_KEY='from-dockerfile-fake-secret-key'
# Run 'npm start' when the container starts.
# This will start serverless, in offline mode, just like
# running the project from the terminal locally
CMD [ "npm", "start" ]