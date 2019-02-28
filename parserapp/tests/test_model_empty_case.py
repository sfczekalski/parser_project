from django.test import TestCase
from parserapp.models import Page


class PageModelTests(TestCase):

    def setUp(self):
        self.test_page_empty = \
            Page.objects.create(url_address='https://django-mysql.readthedocs.io/en/latest/model_fields/json_field.html')

    def test_ready_keywords_empty_case(self):
        self.assertEquals(self.test_page_empty.words_occurrences, {})

    def test_counting_occurrences_empty_case(self):
        self.assertEquals(self.test_page_empty.count_occurrences([]), {})

    def test_splitting_empty_case(self):
        self.assertEquals(self.test_page_empty.split_keywords(None), [])

    def test_finding_keywords_empty_case(self):
        self.assertEquals(self.test_page_empty.get_keywords_from_webpage(), None)

    def test_redirect_empty_case(self):
        self.assertEquals(self.test_page_empty.get_absolute_url(), '/urlkeywords/1/')

    def test_str_method_empty_case(self):
        self.assertEquals(self.test_page_empty.__str__(),
                          'https://django-mysql.readthedocs.io/en/latest/model_fields/json_field.html')
