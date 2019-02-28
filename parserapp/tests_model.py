from django.test import TestCase
from .models import Page
from django.test import Client


class PageModelTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_page = Page.objects.create(url_address='http://www.kurshtml.edu.pl/html/wyrazy_kluczowe,body.html')
        self.test_page_empty = \
            Page.objects.create(url_address='https://django-mysql.readthedocs.io/en/latest/model_fields/json_field.html')

    def test_ready_keywords(self):
        self.assertEquals(self.test_page.words_occurrences, {'klucz': 1, 'Google': 1, 'SEO': 1, 'pozycjonowanie': 1})

    def test_counting_occurrences(self):
        self.assertEquals(self.test_page.count_occurrences(['klucz', 'Google', 'SEO', 'pozycjonowanie']),
                                                           {'klucz': 1, 'Google': 1, 'SEO': 1, 'pozycjonowanie': 1})

    def test_splitting(self):
        self.assertEquals(self.test_page.split_keywords('klucz, Google, SEO, pozycjonowanie'),
                                                        ['klucz', 'Google', 'SEO', 'pozycjonowanie'])

    def test_finding_keywords(self):
        self.assertEquals(self.test_page.get_keywords_from_webpage(), 'klucz, Google, SEO, pozycjonowanie')

    def test_redirect(self):
        self.assertEquals(self.test_page.get_absolute_url(), '/urlkeywords/1/')

    def test_str_method(self):
        self.assertEquals(self.test_page.__str__(), 'http://www.kurshtml.edu.pl/html/wyrazy_kluczowe,body.html')