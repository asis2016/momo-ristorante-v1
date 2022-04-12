# Mo:mo: Ristorante

Mo:mo: Ristorante is a modern and responsive Bootstrap 4 restaurant website template made in Django framework.

## Demo

[https://momo-ristorante-v1.herokuapp.com/](https://momo-ristorante-v1.herokuapp.com/)

## Tech Stack

- HTML5/ CSS3, JavaScript, SASS
- Django 3.2.3, Python 3.8
- Whitenoise, Gunicorn, Heroku, Docker 20.10.6

## Environment Variables

To run this project, you will need to add the following environment variables:

`SECRET_KEY` `django-insecure-v34h48=*da_@x!pa)8w1u2x38o$a&yxi!9f(2@s@68+t%ds!t_`

## Installation

### Run Locally

Clone the project

```bash
  git clone https://github.com/asis2016/momo-ristorante-v1.git
```

Go to the project directory

```bash
  cd momo-ristorante-v1
```

Start the project

```
# docker build .
```

```
$ docker-compose --version
```

```
# docker-compose up -f docker-compose.yml -d
```

### Installing PIP packages

```bash
  docker-compose exec web pipenv install docutils
```

## Usage

### Up and running

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Django Administration

Goto [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

- username: root
- password: root

### Running tests

To run tests, run the following command

```bash
docker-compose exec web python manage.py test
```

# Database diagram

## "Features"

1. very basic website
2. Only admin CRUD available

## NA

1. No Dashboard
2. No custom CRUD maintained

## Demo with Screenshots

[home](https://momo-ristorante-v1.herokuapp.com/)

![home](/screenshots/screenshot-v2.png)

## Feedback

If you have any feedback, please reach out to us at dev@asm.com.np

## Contributing

Contributions are always welcome! please contact us at dev@asm.com.np

## License

[MIT (./LICENSE)](./LICENSE)

## Shout-out
- [unsplash.com](https://unsplash.com/)