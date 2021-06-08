from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User


class TestCategoryModels(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return_name(self):
        """
        Test category model return
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModels(TestCase):
    def setUp(self):
        self.dataCategory = Category.objects.create(name='django', slug='django')
        self.user = User.objects.create(username='damian')
        self.dataProduct = Product.objects.create(category=self.dataCategory, created_by=self.user, title='django book',
                                                  author='damian', description='awesome book', image='django.jpg',
                                                  slug='django', price=24.11)

    def test_product_return_title(self):
        """
        tests return title from product
        """
        data = self.dataProduct
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django book')
