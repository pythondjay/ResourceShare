from django.test import TestCase
from apps.resources import models

# Create your tests here.

# Test Case class # Test <model-name>Model


class TestTagModel(TestCase):
    def setUp(self) -> None:
        self.tag_name = "Python"
        self.tag = models.Tag(name=self.tag_name)

    def test_create_tag_object_successfully(self):
        self.assertIsInstance(self.tag, models.Tag)

    def test_dunder_str(self):
        # str(self.tag) or self.tag.__str__()
        self.assertEqual(str(self.tag), self.tag_name)


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.category_name = "Programming"
        self.category = models.Category(cat=self.category_name)

    def test_create_category_object_successfully(self):
        self.assertIsInstance(self.category, models.Category)

    def test_verbose_name_plural(self):
        self.assertEqual(self.category._meta.verbose_name_plural, "Categories")

    def test_dunder_str(self):
        # str(self.tag) or self.tag.__str__()
        self.assertEqual(str(self.category), self.category_name)


class TestResourcesModel(TestCase):
    def setUp(self) -> None:
        self.user_id = 1
        self.cat_id = 1
        self.title = "Python for beginners"
        self.link = "https://www.python.org"
        self.description = "Python is a programming language"

    def test_create_resources_object_successfully(self):
        self.assertTrue(self.title, models.Resources)

    def test_dunder_str(self):
        self.assertEqual(str(self.title), self.title)
