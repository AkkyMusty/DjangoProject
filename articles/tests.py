from django.template.defaultfilters import title
from django.test import TestCase

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="Hello World", content='Something else')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 1)

