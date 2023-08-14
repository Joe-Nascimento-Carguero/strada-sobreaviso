FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN

CMD [ 'python', 'strada_sobreaviso/main.py' ]