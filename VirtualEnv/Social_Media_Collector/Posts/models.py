from django.db import models
from Users.models import Departments, Classes

# Create your models here.
class Images(models.Model):
    id = models.UUIDField(primary_key=True)
    uploader = models.ForeignKey('Users.Profiles', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    caption = models.TextField()
    storage_path = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    storage_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'images'
