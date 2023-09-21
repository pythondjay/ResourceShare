from django.test import TestCase, Client
from django.urls import reverse
from apps.resources.models import Tag, Category
from apps.user.models import User
from apps.resources import models


class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_page_view_user_count(self):
        # Arrange
        User.objects.create(
            username="test",
            password="test2023",
            first_name="test",
            last_name="test",
            email="test@test",
            bio="test bio",
            title="test developer",
        )
        expected_user_cnt = 1

        # Act
        response = self.client.get(
            reverse("home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        # Assert
        self.assertEqual(response.context["user_cnt"], expected_user_cnt)

    def test_home_page_view_resources_count(self):
        # Arrange
        user = User.objects.create_user(
            username="test",
            password="test2023",
            first_name="test",
            last_name="test",
            email="test@test",
            bio="test bio",
            title="test developer",
        )
        user.save()

        # tag = models.Tag(name="test")
        tag = Tag.objects.create(name="test")

        tag.save()

        cat = Category.objects.create(cat="test")

        cat.save()

        resource = models.Resources.objects.create(
            user_id=user,
            cat_id=cat,
            title="test",
            description="test",
            link="https://test.com",
        )

        # set the many to many relationship
        resource.tag.add(tag)
        resource.save()
        expected_resources_cnt = 1

        # Act
        response = self.client.get(
            reverse("home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        # Assert
        self.assertEqual(response.context["cnt"], expected_resources_cnt)

    def test_home_page_view_resource_per_category_count(self):
        pass

    def test_resource_detail_redirect_to_login_for_non_auth_user(self):
        response = self.client.get(
            reverse("resources-detail", kwargs={"id": 1}),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.status_code, 302)
