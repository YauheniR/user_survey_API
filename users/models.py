import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4())
