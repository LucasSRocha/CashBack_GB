from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from localflavor.br.models import BRCPFField

from utils import clean_string_punctuation


class UserManager(BaseUserManager):
    def create(
        self,
        email: str,
        full_name: str,
        password: str = None,
        cpf: str = None,
        is_active: bool = True,
        is_staff: bool = False,
        is_superuser: bool = False,
    ):
        if not email:
            raise ValueError("Email required")
        if not full_name:
            raise ValueError("Complete name required")
        if not password:
            raise ValueError("Password required")
        if not cpf:
            raise ValueError("CPF required")

        obj = self.model(
            cpf=clean_string_punctuation(cpf),
            full_name=full_name,
            email=self.normalize_email(email),
        )
        obj.set_password(password)
        obj.is_staff = is_staff
        obj.is_active = is_active
        obj.is_superuser = is_superuser
        obj.save()
        return obj

    def create_staffuser(
        self, email: str, full_name: str, password: str, cpf: str,
    ):
        obj = self.create(
            cpf=cpf, email=email, full_name=full_name, password=password, is_staff=True,
        )
        return obj

    def create_superuser(
        self, email: str, full_name: str, password: str, cpf: str,
    ):
        obj = self.create(
            cpf=cpf,
            email=email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return obj


class User(AbstractBaseUser, PermissionsMixin):
    cpf = BRCPFField(unique=True, max_length=11)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "full_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
