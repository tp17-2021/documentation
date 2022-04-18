FROM node as build

WORKDIR /app

RUN npm install retypeapp --global

COPY . /app/

RUN retype build --override='{"url":"/docs"}'


FROM nginx:1.19-alpine

COPY --from=build /app/.retype /usr/share/nginx/html
