from django.db import models
from Users.models import Departments, Profiles, Classes
import uuid
from django.utils import timezone

class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uploader = models.ForeignKey(Profiles, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    caption = models.TextField()
    storage_path = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    is_reported = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'images'
