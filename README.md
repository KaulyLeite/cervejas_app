# cervejas_app

Web system for promotion, order placement, and inventory management for a craft beer distributor.

### Project Status:

Under development.

## Setup

First, clone the GitHub repository:

```sh
git clone git@github.com:KaulyLeite/cervejas_app.git
```

Change to the new directory:

```sh
cd cervejas_app
```

Activate the virtualenv for the project.

Install the necessary dependencies:

```sh
pip install -r requirements.txt
```

Apply the migrations:

```sh
python manage.py migrate
```

Run the application:

```sh
python manage.py runserver
```

Open in a browser:

```sh
http://127.0.0.1:8000/
```
