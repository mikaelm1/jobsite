FROM python:3.5-slim
MAINTAINER Mikael Mukhsikaroyan <mikaelm3981@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

RUN mkdir -p /app
WORKDIR /app
COPY . /app/

# ENV DJANGO_SETTINGS_MODULE=jobsite.settings

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
# CMD python3 manage.py runserver 0.0.0.0:8000
