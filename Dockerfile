FROM node

WORKDIR /app

RUN npm install retypeapp --global

CMD ["retype", "build"]
