from django.db import models
from common.models import MightHaveOwner, Timestamped


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
