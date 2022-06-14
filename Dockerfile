FROM python:3-slim
WORKDIR /app

ENV FLAGS_DATABASE=/var/destructivefarm/flags.sqlite
ENV FLASK_APP=/app/server/standalone.py

COPY schema.sql start_server.sh requirements.txt ./
RUN pip install -r requirements.txt
COPY server/ ./server/

VOLUME [ "/var/destructivefarm" ]
EXPOSE 5000

ENTRYPOINT "./start_server.sh"
