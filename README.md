# cervejas_app

Web system for advertising, sending orders by email and generating a PDF of the order for a craft beer distributor.

### Project Status:

Finished (master - v1.0.0).

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

## Management

### Brands and Products:

The data for brands and products must be registered through Django Admin.

### About Page Information Configuration:

The data for rendering e-mail, phone, and WhatsApp information on the About page can be registered through a "config.ini" file as shown in the example below:

```sh
[SOBRE]
email = email@email.com
telefone = (99) 99999-9999
whatsapp = 5599999999999
```

### Email Order Sending Configuration:

The data for configuring the email address and password for sending the order by email must be used through environment variables.

## Screenshots

Main page:

![index](https://github.com/KaulyLeite/cervejas_app/assets/33230557/e42a439b-d604-46f0-872b-6be954f2464c)

<br>

Products page:

![produtos](https://github.com/KaulyLeite/cervejas_app/assets/33230557/7dbca366-6b45-41f6-9a4a-485747bd1038)

<br>

About page:

![sobre](https://github.com/KaulyLeite/cervejas_app/assets/33230557/a1206aa7-4f20-4a8e-8849-78333b3d8a3d)

<br>

Order page:

![pedidos](https://github.com/KaulyLeite/cervejas_app/assets/33230557/00729d89-0b44-4589-a3dd-adbe036891dd)

<br>

Order confirmation page:

![confirmacao](https://github.com/KaulyLeite/cervejas_app/assets/33230557/b6271d12-0606-4325-9ae6-998ddc6eba15)

<br>

Order submission page:

![envio](https://github.com/KaulyLeite/cervejas_app/assets/33230557/8a088c4f-5b87-48b3-865f-6b134cd929b4)

<br>

Order submission error page:

![erro](https://github.com/KaulyLeite/cervejas_app/assets/33230557/519edd18-fc49-4b06-ac82-52f7f17ddb07)

<br>

PDF generation page:

![pdf](https://github.com/KaulyLeite/cervejas_app/assets/33230557/c78ad196-1436-4cfe-9e53-b76437a6765c)

<br>

Mobile view of a page:

![mobile](https://github.com/KaulyLeite/cervejas_app/assets/33230557/a2bf79f4-318b-4a5f-ab76-3c30e1d69536)
