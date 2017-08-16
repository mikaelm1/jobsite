# Job App

A job board built with Django.

## Getting Started with Docker
Need to have Docker installed. 

#### Running the app
```
docker-compose up --build
```

#### Running migrations
```
$ docker-compose exec web python src/manage.py makemigrations
$ docker-compose exec web python src/manage.py migrate
```

#### Adding an app
```
$ docker exec -it [CONTAINER_ID] bash
$ cd src
$ python manage.py startapp [APP_NAME]
$ exit
```
