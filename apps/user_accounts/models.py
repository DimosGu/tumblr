from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):

  def create_user(self, email, username, password=None):

    user = self.model(
      email=self.normalize_email(email),
      username=username,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, username, password):
    user = self.create_user(email,
      username=username,
      password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

  def get_by_username(self, username):
    return self.get(username=username)


class User(AbstractBaseUser):

  email = models.EmailField(max_length=255, unique=True)
  username = models.CharField(max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  objects = CustomUserManager()

  class Meta:
    app_label = 'user_accounts'

  def get_full_name(self):
    return self.email

  def get_short_name(self):
    return self.email

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
    return True

  def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
    return True

  @property
  def is_staff(self):
    "Is the user a member of staff?"
    return self.is_admin

  def get_username(self, username):
    return self.get(username=username)