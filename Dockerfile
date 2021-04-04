RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
EXPOSE 8000
CMD python app.py

