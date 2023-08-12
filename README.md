# cervejas_app

Web system for advertising, sending orders by email and generating a PDF of the order for a craft beer distributor.

### Project Status:

Finished (master - v1.1.0).

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

![1](https://github.com/KaulyLeite/cervejas_app/assets/33230557/7cf8318a-baa9-4c96-8861-f537a13d1ec8)

<br>

Products page:

![2](https://github.com/KaulyLeite/cervejas_app/assets/33230557/9f5b8c75-4a4b-41af-9b58-416f4d7dcf22)

<br>

About page:

![3](https://github.com/KaulyLeite/cervejas_app/assets/33230557/ea7c4493-7263-453d-b386-664ddfc37a45)

<br>

Order page:

![4](https://github.com/KaulyLeite/cervejas_app/assets/33230557/ac9826bd-ea2b-41b7-8c61-0d4f6251c2d5)

<br>

Order confirmation page:

![5](https://github.com/KaulyLeite/cervejas_app/assets/33230557/f29ad321-70c9-4b19-b506-3816548e7ebc)

<br>

Order submission page:

![6](https://github.com/KaulyLeite/cervejas_app/assets/33230557/42191939-840d-46dd-88a6-f75791596d8f)

<br>

Order submission error page:

![7](https://github.com/KaulyLeite/cervejas_app/assets/33230557/ee12d894-4164-4ca7-b4be-621d791bb6ea)

<br>

PDF generation page:

![8](https://github.com/KaulyLeite/cervejas_app/assets/33230557/2145222f-1974-4022-ac0b-fb56f9e5cd4a)

<br>

Mobile view of a page:

![9](https://github.com/KaulyLeite/cervejas_app/assets/33230557/c1cd2734-6d99-468b-a902-22f941e06d73)
