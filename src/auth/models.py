# coding: utf-8


from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class BaseUser(PermissionsMixin, AbstractBaseUser):

    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
        db_index=True,
    )
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField('active', default=False,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    uid = models.CharField('UID', max_length=16, db_index=True, null = True, blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
