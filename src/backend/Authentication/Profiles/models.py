from django.db import models
from backend.Authentication.Users.models import User
from backend.Authentication.Profiles.cities_list import StateChoices, CitiesChoices
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    class LanguageChoices(models.TextChoices):
        en = 'en', _('English')
        fa = 'fa', _('persian')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(_('username'), max_length=150)
    email = models.EmailField(_('email'), max_length=150)
    first_name = models.CharField(_('first name'), max_length=150, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, null=True, blank=True)
    language = models.CharField(_('language'), max_length=64,
                                choices=LanguageChoices.choices,
                                default=LanguageChoices.en,
                                null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=11, null=True, blank=True)

    state = models.CharField(_('state'), max_length=150, null=True, blank=True, choices=StateChoices.choices,
                             default='NoState')

    city = models.CharField(_('city'), max_length=150, null=True, blank=True, choices=CitiesChoices.choices,
                            default='NoCity')

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Contact(models.Model):
    full_name = models.CharField(_('full name'),max_length=255)
    email = models.EmailField(_('email'),)
    message = models.TextField(_('message'),)
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    is_checked = models.BooleanField(_('is checked'),default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contact')
