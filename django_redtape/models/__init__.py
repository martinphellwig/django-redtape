"""
Red Tape module
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.timezone import now
from functools import lru_cache


class DateTimeStampManager(models.Manager):
    "Query Manager to restrict returning data"
    def get_queryset(self):
        "get_queryset override"
        query = models.Manager.get_queryset(self)
        ts_now = now()

        activate_lte = models.Q(dts_activate__lte=ts_now)
        query = query.filter(dts_activate__lte=activate_lte)

        deleted_nil = models.Q(dts_deleted__isnull=False)
        deleted_gte = models.Q(dts_deleted__gte=ts_now)
        query = query.filter(deleted_nil | deleted_gte)

        return query


class DateTimeStamp(models.Model):
    "Date/Time Stamps"
    all_objects = models.Manager
    objects = DateTimeStampManager
    class Meta:
        "Meta section to identify this is abstract"
        abstract = True

    dts_activate = models.DateTimeField(auto_now_add=True)
    dts_inserted = models.DateTimeField(auto_now_add=True)
    dts_modified = models.DateTimeField(null=True, blank=True)
    dts_archived = models.DateTimeField(null=True, blank=True)


@lru_cache(1)
def default_group():
    "Return default group."
    return Group.objects.get(name=settings.DEFAULT_UGP_GROUPNAME)


class UserGroupPermission(models.Model):
    "User/Group Permissions"
    class Meta:
        "Meta section to identify this is abstract"
        abstract = True

    ugp_editor = models.ForeignKey(Group, default=default_group,
                                   related_name='ugp_editor')
    ugp_select = models.ForeignKey(Group, default=default_group,
                                   related_name='ugp_select')
    ugp_modify = models.ForeignKey(Group, default=default_group,
                                   related_name='ugp_modify')
    ugp_delete = models.ForeignKey(Group, default=default_group,
                                   related_name='ugp_delete')


class RedTape(DateTimeStamp, UserGroupPermission):
    """Provides a table with permission details and date/time stamps.
    You would typically inherit from this model if you want to use the
    functionality in your designated models. This is not a meta model, which
    means the model is 'extended' with the model you created.
    """
    pass

