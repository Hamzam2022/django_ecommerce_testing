import pytest
from django.contrib.auth.models import User

#
# def test_user_creation(new_user):
#     count = User.objects.all().count()
#     assert count == 1
#
#
# def test_superuser_creation(new_superuser):
#     count = User.objects.all().count()
#     assert count == 1
#
#
# def test_user_creation1(new_user):
#     assert isinstance(new_user, User) is True
#
#
# def test_superuser_details(new_superuser):
#     assert new_superuser.is_staff
#     assert new_superuser.is_superuser
#     assert new_superuser.is_active
#     assert new_superuser.username == "test@test.com"
#     assert new_superuser.first_name == "test_name"
#     assert new_superuser.last_name == "lastname"
#     assert new_superuser.email == "test@test.com"
#
#
# def test_user_details(new_user):
#     assert new_user.is_staff is False
#     assert new_user.is_superuser is False
#     assert new_user.is_active
#     assert new_user.username == "test@test.com"
#     assert new_user.first_name == "test_name"
#     assert new_user.last_name == "lastname"
#     assert new_user.email == "test@test.com"
#
#
# def test_set_check_password_user(new_user):
#     new_user.set_password("new-password")
#     assert new_user.check_password("new-password") is True
#
#
# def test_set_check_password_superuser(new_superuser):
#     new_superuser.set_password("new-password")
#     assert new_superuser.check_password("new-password") is True
#
#
# def test_delete_user(new_user):
#     User.delete(new_user)
#     count = User.objects.all().count()
#     assert count == 0
#
#
# def test_delete_superuser(new_superuser):
#     User.delete(new_superuser)
#     count = User.objects.all().count()
#     assert count == 0
