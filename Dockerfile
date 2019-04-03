FROM tiangolo/uwsgi-nginx-flask:python3.7
WORKDIR /app
ENV DOWNLOAD_PATH /app/data
ENV SERVER_ADDRESS 0.0.0.0
ENV SERVER_PORT 3100
COPY . .
RUN pip3 install -r requirements.txt
VOLUME [ "/app/data" ]
EXPOSE 3100