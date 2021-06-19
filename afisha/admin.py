from django.contrib import admin
from django.contrib.admin import register

from afisha.filters import CitySelectFilter
from afisha.models import Event, EventParticipant
from common.models import City
from users.utils import (
    AdminOnlyPermissionsMixin,
    AdminAndModersPermissionsMixin,
)


@register(Event)
class EventAdmin(AdminAndModersPermissionsMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "city",
        "address",
        "contact",
        "title",
        "description",
        "startAt",
        "endAt",
        "seats",
    )
    list_filter = (
        CitySelectFilter,
        "startAt",
    )
    empty_value_display = "-пусто-"
    search_fields = ("title",)

    def get_queryset(self, request):
        if request.user.profile.is_moderator_reg:
            return Event.objects.filter(
                city__in=City.objects.filter(region=request.user.profile)
            )

        else:
            return Event.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.profile.is_moderator_reg:
            form.base_fields["city"].queryset = request.user.profile.region
        form.base_fields[
            "startAt"
        ].help_text = "Время и дата указываются в формате местного времени"
        form.base_fields[
            "endAt"
        ].help_text = "Время и дата указываются в формате местного времени"
        return form


@register(EventParticipant)
class EventParticipantAdmin(AdminOnlyPermissionsMixin, admin.ModelAdmin):
    list_display = ("user", "event")
    empty_value_display = "-пусто-"
