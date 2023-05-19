FROM python:3.9-bullseye
RUN apt-get update
WORKDIR /api
COPY requirements.txt /api/
RUN pip3 install -r requirements.txt
COPY ./api/ /api/
COPY docker-entry.sh /api/
CMD ["sh", "docker-entry.sh"]