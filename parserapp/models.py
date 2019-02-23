from django.db import models
import requests
from bs4 import BeautifulSoup
from django.urls import reverse


class Page(models.Model):
    url_address = models.URLField()

    def split_keywords(self, str_keywords):
        try:
            list_keywords = str_keywords.split(',')
        except AttributeError:
            return []

        return [x.strip() for x in list_keywords]

    def get_keywords_from_webpage(self):
        #url = 'http://www.kurshtml.edu.pl/html/wyrazy_kluczowe,body.html'
        response = requests.get(self.url_address)
        html = response.text
        page_content = BeautifulSoup(html, 'html.parser')

        all_meta_tags = page_content.find_all('meta')
        for tag in all_meta_tags:
            for key, value in tag.attrs.items():
                if key.lower() == 'name' and value.lower() == 'keywords':
                    for k, v in tag.attrs.items():
                        if k.lower() == 'content':
                            return v

        return None

    def count_occurrences(self, my_list):
        occurrences = {}

        for word in my_list:
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

        return occurrences

    @property
    def words_occurrences(self):
        keywords = self.get_keywords_from_webpage()
        list_kw = self.split_keywords(keywords)
        return self.count_occurrences(list_kw)

    def get_absolute_url(self):
        return reverse('url-detail', kwargs={'pk': self.pk})
