from django.test import TestCase
from django.urls import reverse
from django.test import Client


class HomePageTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status_code_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_status_code_home_page_by_name(self):
        response = self.client.get(reverse('url-create'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template_home_page(self):
        response = self.client.get(reverse('url-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'parserapp/page_form.html')

    def test_post(self):
        response = self.client.post('/', {'url_address': 'http://www.kurshtml.edu.pl/html/wyrazy_kluczowe,body.html'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/urlkeywords/1/')
