# Recess API

## Description

This is the backend for the Recess Application. If you want to see the Front-end repo, please go here: https://github.com/bwilson19/recess-frontend

![api screenshot](https://user-images.githubusercontent.com/58187597/76568663-8cd26400-646e-11ea-8806-4497e28b2cb5.png)

### Games

https://recessapi.herokuapp.com/games

### Leagues

https://recessapi.herokuapp.com/leagues

## Technologies Used

- Django
- Python
- PostgreSQL
- Django REST Framework
- JWT

## Model Schemas

Current models on the API are League, Game and User Auth (JWT)

![models](https://user-images.githubusercontent.com/58187597/76569082-84c6f400-646f-11ea-9786-a859d9f5553f.png)

## Getting Started/Installation Instructions

1. Fork & clone ths repo.
2. Run pipenv install to download dependencies (i.e. REST Framework)
3. Run python3 manage.py runserver to start a host on port 8000.

## Contribution Guidelines

#### In order to contribute we ask the following things:

1. Fork & Clone this repo.
2. Do your best to keep the current coding style.
3. Submit a pull request to this current repo with the following information:

- Your name
- A link to your github repository
- An image of the app showing what functionality/ styling you added if the change or improvement was front-facing else a code snippet explaining your enhancement & why it's beneficial.

4. Merges will happen upon approval.

## Future Updates
- Models will be added for user profiles and comments to add a social dynamic to the site
- User model will be pulled in to other models to indicate ownership. (i.e. only able to edit the games or leagues created by the specific user)

## Created By

Brendan Wilson [Brendan's GitHub](https://github.com/bwilson19)

### References

- Django REST Framework Documentation: https://www.django-rest-framework.org/