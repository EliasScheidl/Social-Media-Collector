from django.db import models
from Users.models import Profiles
from Posts.models import Images
import uuid


class UserInteractions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Profiles, models.DO_NOTHING, blank=True, null=True)
    image = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True)
    interaction_type = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_interactions'
        unique_together = (('user', 'image'),)
