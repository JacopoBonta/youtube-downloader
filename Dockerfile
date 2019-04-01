FROM python:3.7
WORKDIR /app
ENV DOWNLOAD_PATH=/app/data
COPY . .
RUN ./install.sh
VOLUME [ "/app/data" ]
EXPOSE 5000
CMD ./start.sh