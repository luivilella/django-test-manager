from django.db import models
from django.db.models.query import QuerySet


class Country(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)


class PersonQuerySet(QuerySet):
    def set(self, slug, **kwargs):
        return self.filter(slug=slug).update(**kwargs)

    def set2(self, slug, **kwargs):
        return self.set(slug, **kwargs)


class Person(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=10, null=True)
    country = models.ForeignKey(
        Country, blank=True, null=True, related_name='persons',
        on_delete=models.SET_NULL
    )

    objects = PersonQuerySet.as_manager()
