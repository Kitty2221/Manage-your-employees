import random

import pytest
from app import app, db


@pytest.fixture
def client():
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db:3306/flask_test'
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client


@pytest.fixture()
def plant_data():
    random_id = random.randint(0, 240)
    yield {
        "location": f"Test {random_id}",
        "name": f"Test {random_id}",
        "director_id": random_id
    }


@pytest.fixture()
def upd_plant_data():
    random_id = random.randint(0, 100)
    yield {
        "location": f"NEW_Text {random_id}",
        "name": f"NEW_Text {random_id}",
        "director_id": random_id
    }


@pytest.fixture()
def employee_data():
    random_id = random.randint(0, 100)
    yield {
        "name": f"Test name {random_id}",
        "email": f"test{random_id}@mail.com",
        "department_type": f"Test department type {random_id}",
        "department_id": random_id
    }


@pytest.fixture()
def upd_employee_data():
    random_id = random.randint(0, 100)
    yield {
        "name": f"NEW_Text name {random_id}",
        "email": f"test{random_id}@mail.com",
        "department_type": f"NEW_Text department type {random_id}",
        "department_id": random_id
    }


@pytest.fixture()
def salon_data():
    random_id = random.randint(0, 100)
    yield {
        "name": f"Test name {random_id}",
        "city": f"Test city {random_id}",
        "address": f"Test address {random_id}"
    }


@pytest.fixture()
def upd_salon_data():
    random_id = random.randint(0, 100)
    yield {
        "name": f"NEW_Text name {random_id}",
        "city": f"NEW_Text city {random_id}",
        "address": f"NEW_Text address {random_id}"
    }


@pytest.fixture()
def menu_item_data():
    yield {
        "name": "Test link",
        "link": "/test-link",
        "is_active": 1,
    }


@pytest.fixture()
def upd_menu_item_data():
    yield {
        "name": "NEW_Text link",
        "link": "/new-test-link",
        "is_active": 1,
    }