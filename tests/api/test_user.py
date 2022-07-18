import pytest
from django.test import client
from django.urls import reverse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.test import APIClient
from base.models import Product, Order
from django.contrib.auth.models import User
client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )

    response = client.post("/api/users/register/", payload)

    data = response.data

    assert data["name"] == payload["name"]
    assert data["username"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="test11@test.com", password="super-secret"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post("/api/users/login/", dict(username="test11@test.com", password="super-secret"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_profile():
    payload = dict(
        name="testing123",
        email="test111@test.com",
        password="super-secret"
    )

    client.post("/api/users/register/", payload)
    client.post("/api/users/login/", dict(username="test111@test.com", password="super-secret"))
    response = client.get("http://localhost:7000/#/profile")
    assert response.status_code == 200



# @pytest.mark.django_db
# def test_logout():
    # payload = dict(
    #     name="testing123",
    #     email="test111@test.com",
    #     password="super-secret"
    # )
    #
    # client.post("/api/users/register/", payload)
    # client.post("/api/users/login/", dict(username="test111@test.com", password="super-secret"))
    # response = client.post("/api/users/logout/")
    # assert response.status_code == 200
