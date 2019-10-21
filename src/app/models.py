import uuid

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_ts = models.DateTimeField('Created Timestamp', auto_now_add=True)
    updated_ts = models.DateTimeField('Updated Timestamp', auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def editable_fields(cls):
        return [field.name for field in cls._meta.fields if field.editable and field.name != 'id']


class SlugModel(BaseModel):
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        while not self.slug:
            slug = uuid.uuid4().hex[:6].upper()
            while self.__class__.objects.filter(slug=slug).exists():
                slug = uuid.uuid4().hex[:6].upper()
            self.slug = slug
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
