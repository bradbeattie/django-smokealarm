from django.db import models
from django.contrib.auth.models import User


class MightHaveOwner(models.Model):
    owner = models.ForeignKey(User, db_index=True, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Timestamped(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    def modified(self):
        return self.created != self.updated
    modified.boolean = True

    class Meta:
        abstract = True


class Report(MightHaveOwner, Timestamped):
    error = models.TextField()
    file = models.CharField(max_length=255)
    line = models.PositiveIntegerField()
    url = models.URLField(max_length=255)
    cookies = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.error
