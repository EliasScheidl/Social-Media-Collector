from django.db import models
from Users.models import Departments, Classes, Profiles
import uuid

class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uploader = models.ForeignKey(Profiles, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    caption = models.TextField()
    storage_path = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    likes_count = models.IntegerField()
    dislikes_count = models.IntegerField()
    is_reported = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'images'
