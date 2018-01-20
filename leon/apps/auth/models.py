# coding: utf-8


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class BaseUser(PermissionsMixin, AbstractBaseUser):

    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
        unique=True,
        db_index=True,
    )
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    uid = models.CharField(_('UID'), max_length=16, db_index=True, null = True, blank = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
