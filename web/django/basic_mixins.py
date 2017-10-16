"""
Mixins I often find a use for when working on django projects
"""
from django.db import models


class BaseMixin(models.Model):
    """
    A mixin for a very common usecase
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TimeStampMixin(models.Model):
    """
    Keeping track of when an object is created or modified is extremely useful
    """
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    modified = models.DateTimeField(auto_now=True, null=True, editable=False)

    class Meta:
        abstract = True


class CreationModificationMixin(TimeStampMixin):
    """
    Abstract mixin for tracking creation and modification details
    This mixin inherits from TimeStampMixin as when you track who it is
    usually a good idea to track when
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='+',
                                   null=True, blank=True, editable=False)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='+',
                                    null=True, blank=True, editable=False)

    class Meta:
        abstract = True
