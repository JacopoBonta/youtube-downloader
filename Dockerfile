FROM tiangolo/uwsgi-nginx-flask:python3.7
# set starting processes number
ENV UWSGI_CHEAPER 4
# set maximum processes number
ENV UWSGI_PROCESSES 64
RUN apt install ca-certificates -y && update-ca-certificates
WORKDIR /app
ENV DOWNLOAD_PATH /app/data
ENV SERVER_ADDRESS 0.0.0.0
ENV SERVER_PORT 80
COPY . .
RUN pip3 install -r requirements.txt
VOLUME [ "/app/data" ]