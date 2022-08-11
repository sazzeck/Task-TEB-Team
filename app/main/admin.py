from django.contrib.admin import register, ModelAdmin
from .models import User


@register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        "username",
        "is_online",
        "is_active",
        "is_staff",
        "last_login",
        "date_joined",
    )

    list_display_links = ("username",)

    search_fields = ("username",)

    list_filter = (
        "is_online",
        "is_active",
        "is_staff",
        "last_login",
    )

    list_editable = (
        "is_active",
        "is_staff",
    )

    show_full_result_count = True
