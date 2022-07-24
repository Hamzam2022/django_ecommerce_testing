import pytest
from rest_framework import request
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
client = APIClient()


def test_api_product_creation(new_superuser):
    client.force_authenticate(new_superuser)
    response = client.post("/api/products/create/")
    # data = response.data
    assert response.status_code == 200
