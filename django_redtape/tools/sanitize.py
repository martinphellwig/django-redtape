"""
Perform sanitization check prior of releasing the app as ready.
"""
from django.contrib.auth.models import Group
from django.conf import settings

def main():
    "Perform sanitization checks"
    if not Group.objects.filter(name=settings.DEFAULT_UGP_GROUPNAME).exists():
        Group.objects.create(name=settings.DEFAULT_UGP_GROUPNAME)

