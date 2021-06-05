# Mo:mo: Ristorante

Mo:mo: Ristorante is a modern and responsive Bootstrap 4 restaurant website template made in Django framework.

Status: WIP

## Tech Stack
Docker 20.10.6, Python 3.8, Django 3.2.3, Whitenoise, Gunicorn, Heroku

## Demo
[https://momo-ristorante-v1.herokuapp.com/](https://momo-ristorante-v1.herokuapp.com/)

## Environment Variables

To run this project, you will need to add the following environment variables:

`SECRET_KEY` `django-insecure-v34h48=*da_@x!pa)8w1u2x38o$a&yxi!9f(2@s@68+t%ds!t_`


## Run Locally

Clone the project

```bash
  git clone https://github.com/asis2016/momo-ristorante-v1.git
```

Go to the project directory

```bash
  cd momo-ristorante-v1
```

Start the project

```bash
  docker build .
```

```bash
  docker-compose up -f docker-compose.yml -d
```

## Running Tests

To run tests, run the following command

```bash
  docker-compose exec web python manage.py test
```

## Running the project locally

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Running Django Administration

Goto [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- username: root
- password: root

## Demo with Screenshots

[home](https://momo-ristorante-v1.herokuapp.com/)

![home](/screenshots/screenshot-v2.png)


## "Features"

1. very basic website
2. Only admin CRUD available

## NA

1. No Dashboard
2. No custom CRUD maintained

## Feedback

If you have any feedback, please reach out to us at hello@amaharjan.com