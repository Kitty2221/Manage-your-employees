import pytest
from tests.fixtures import *
import json


def test_plant_post(client, plant_data):
    res = client.post("/api/v1/plants", json=plant_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_plants(client):
    res = client.get("/api/v1/plants")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_plant(client):
    res = client.get('/api/v1/plants/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_plant(client, upd_plant_data):
    res = client.put("/api/v1/plants/5", json=upd_plant_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_plant_delete(client):
    res = client.delete('/api/v1/plants/8')
    assert res.status_code == 204
    res = client.get('/api/v1/plants/8')
    assert res.status_code == 404


def test_employee_post(client, employee_data):
    res = client.post("/api/v1/employees", json=employee_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_employees (client):
    res = client.get("/api/v1/employees")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_employee(client):
    res = client.get('/api/v1/employees/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_employee(client, upd_employee_data):
    res = client.put("/api/v1/employees/6", json=upd_employee_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_employees_delete(client):
    res = client.delete('/api/v1/employees/8')
    assert res.status_code == 204
    res = client.get('/api/v1/employees/8')
    assert res.status_code == 404


def test_salon_post(client, salon_data):
    res = client.post("/api/v1/salons", json=salon_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_salons(client):
    res = client.get("/api/v1/salons")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_salon(client):
    res = client.get('/api/v1/salons/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_salon(client, upd_salon_data):
    res = client.put("/api/v1/salons/3", json=upd_salon_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_salons_delete(client):
    res = client.delete('/api/v1/salons/8')
    assert res.status_code == 204
    res = client.get('/api/v1/salons/8')
    assert res.status_code == 404


def test_menu_item_post(client, menu_item_data):
    res = client.post("/api/v1/menu-items", json=menu_item_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_menu_items(client):
    res = client.get("/api/v1/menu-items")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_menu_item(client):
    res = client.get('/api/v1/menu-items/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_menu_item(client, upd_menu_item_data):
    res = client.put("/api/v1/menu-items/3", json=upd_menu_item_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_menu_item_destroy(client):
    res = client.delete('/api/v1/menu-items/8')
    assert res.status_code == 204
    res = client.get('/api/v1/menu-items/8')
    assert res.status_code == 404