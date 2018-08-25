from django.db import models
from django.db.models.query import QuerySet


class PersonQuerySet(QuerySet):
    def set(self, slug, **kwargs):
        return self.filter(slug=slug).update(**kwargs)


class Person(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=10, null=True)

    objects = PersonQuerySet.as_manager()
