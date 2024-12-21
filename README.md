
# **BizRadar**

Django app that helps users find businesses in a specific area

![Demo](https://github.com/sethlagman/bizradar/blob/main/demo.gif?raw=true)

## Features

- Search for any businesses
- Specify a location

## Installation

- [X]  [Download Python 3.13.0](https://www.python.org/downloads/release/python-3130/)
- [X]  Clone or download this repository
- [X]  Go to the project directory via CLI or any IDE of your choice
- [X]  Create a virtual environment
    - For Linux or macOS: `python3 -m venv venv`
    - For Windows: `python -m venv venv`
- [X]  Activate the virtual environment
    - For Linux or macOS: `source venv/bin/activate`
    - For Windows: `venv\Scripts\activate`
- [X]  Install the dependencies
    - `pip install -r requirements.txt`
- [X]  Set up environment variables
    - Create .env file
    - Input your keys
    ```
    SECRET_KEY=<django key>
    API_KEY=<yelp api key>
    ```
- [X]  Change directory to bizradar app
    - `cd bizradar`
- [X]  Collect static files
    - `python manage.py collectstatic`
- [X]  Run the django app
    - `python manage.py runserver`
- [X]  Navigate to
    - http://127.0.0.1:8000/

## Creation

- Python
- Django
- Yelp API