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

    def get_page_content(self):
        response = requests.get(self.url_address)
        html = response.text
        page_content = BeautifulSoup(html, 'html.parser')
        return page_content

    def get_keywords_from_webpage(self):
        all_meta_tags = self.get_page_content().find_all('meta')
        for tag in all_meta_tags:
            for key, value in tag.attrs.items():
                if key.lower() == 'name' and value.lower() == 'keywords':
                    for k, v in tag.attrs.items():
                        if k.lower() == 'content':
                            return v

        return None

    def count_occurrences(self, my_list):
        occurrences = {}
        tags = self.get_page_content().find_all('div')

        for word in my_list:
            count = 0
            for tag in tags:
                text = tag.text
                count += text.count(word)
            occurrences[word] = count

        return occurrences

    @property
    def words_occurrences(self):
        keywords = self.get_keywords_from_webpage()
        list_kw = self.split_keywords(keywords)
        return self.count_occurrences(list_kw)

    def get_absolute_url(self):
        return reverse('url-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.url_address
