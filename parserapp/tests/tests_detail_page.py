from django.test import TestCase
from django.urls import reverse
from django.test import Client
from parserapp.models import Page


class DetailPageTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_page = Page.objects.create(url_address='http://www.kurshtml.edu.pl/html/wyrazy_kluczowe,body.html')

    def test_url_detail_page(self):
        url = reverse('url-detail', kwargs={'pk': 1})
        self.assertEquals(url, '/urlkeywords/1/')

    def test_status_code_detail_page(self):
        response = self.client.get('/urlkeywords/1/')
        self.assertEquals(response.status_code, 200)

    def test_status_code_detail_page_by_name(self):
        response = self.client.get(reverse('url-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)

    def test_correct_template_detail_page(self):
        response = self.client.get(reverse('url-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'parserapp/page_detail.html')

