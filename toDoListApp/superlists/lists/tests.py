from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import homePage

# Create your tests here.
class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve("/")
    self.assertEqual(found.func, homePage)