FROM python:3.8-slim-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
EXPOSE 5000
CMD python app.py