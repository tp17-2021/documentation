FROM node

WORKDIR /app

RUN npm install retypeapp --global

RUN retype build --override='{"url":"/docs"}'

CMD ["retype", "run", "--verbose"]
