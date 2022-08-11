from django.db import models
from . import CustomAbstractUser
from django.utils.translation import gettext_lazy as _


class User(CustomAbstractUser):
    is_online = models.BooleanField(default=False)

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["id", "is_online"]

    def __str__(self):
        return f"{self.username}"
