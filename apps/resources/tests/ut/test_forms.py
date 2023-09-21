from django.test import TestCase
from apps.resources.form import PostResourceForm


class TestPostResourceForm(TestCase):
    def test_form_is_valid(self):
        data = {
            "title": "Test",
            "link": "https://test.com",
            "description": "Test",
            "category": 1,
            "tag": [1],
        }

        form = PostResourceForm(data=data)

        self.assertTrue(form.is_valid())

    def test_form_missing_link_generate_errors(self):
        data = {
            "title": "Test",
            "description": "Test",
            "category": 1,
            "tag": [1],
        }

        form = PostResourceForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["link"], ["This field is required."])
