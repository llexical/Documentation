from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        """
        query set does not selected is_delete files
        """
        return super(SoftDeleteManager, self).get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    """
    Shared model functions go in here
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def delete(self, hard_delete=False, **kwargs):
        """
        soft delete implimentation
        """
        if hard_delete:
            return super(BaseModel, self).delete(**kwargs)

        self.is_deleted = True
        self.deleted_at = datetime.now()
        return self.save() # Most likely to change LOL

