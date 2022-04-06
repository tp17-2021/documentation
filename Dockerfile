FROM node

WORKDIR /app

RUN npm install retypeapp --global

CMD ["retype", "build", "--host", "0.0.0.0", "/docs"]
