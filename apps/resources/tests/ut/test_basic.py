from django.test import TestCase

# Create your tests here.


class TestBasicCalculation(TestCase):
    def test_basic_sum(self):
        # Arrange
        x = 1
        y = 4

        # Act
        result = x + y

        # Assert
        self.assertEqual(result, 5)
