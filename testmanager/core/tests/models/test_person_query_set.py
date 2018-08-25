from django.test import TestCase
from core.models import Country, Person

class TestSet(TestCase):
    def test_just_update_records_with_the_same_slug(self):
        Person.objects.create(slug='batman', name='John')
        Person.objects.create(slug='batman', name='Connor')
        Person.objects.create(slug='bruce', name='Ill be back')

        Person.objects.set('batman', name='###')

        expected_value = 2
        result = Person.objects.filter(name='###').count()

        self.assertEqual(result, expected_value)


    def test_just_update_records_with_the_same_slug_using_related_manager(self):
        country = Country.objects.create(name='Ireland')

        Person.objects.create(slug='batman', name='John', country=country)
        Person.objects.create(slug='batman', name='Connor', country=country)
        Person.objects.create(
            slug='bruce', name='Ill be back', country=country
        )

        country.persons.set('batman', name='###')

        expected_value = 2
        result = Person.objects.filter(name='###').count()

        self.assertEqual(result, expected_value)
