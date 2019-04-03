FROM tiangolo/uwsgi-nginx-flask:python3.7
WORKDIR /app
ENV DOWNLOAD_PATH /app/data
ENV SERVER_ADDRESS 0.0.0.0
ENV SERVER_PORT 80
COPY . .
RUN pip3 install -r requirements.txt
VOLUME [ "/app/data" ]