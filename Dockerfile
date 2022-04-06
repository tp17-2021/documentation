FROM node

WORKDIR /app

RUN npm install retypeapp --global

CMD ["retype", "watch", "--host", "0.0.0.0"]
