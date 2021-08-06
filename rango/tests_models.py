from rango.models import Category, Product, Cart, Search, UserProfile
from django.test import TestCase

flag = f"------------------------------------------------------------------"


#
# this file is used to fulfill  unit test  of models.
#



class ModelTests(TestCase):
    """
    whether models are set up correctly
    """
    def setUp(self):
        category_py = Category.objects.get_or_create(id = 'c1', name = 'Toys', sales = 534)
        Category.objects.get_or_create(id = 'c2', name='Clothing', sales=289)
        
        Product.objects.get_or_create(category=category_py[0],
                                   id='c1p1',
                                   name='Phone',
                                   price=141.34,
                                   sales = 182)
    
    def test_category_model(self):
        """
        category model test
        """
        category_py = Category.objects.get(id='c1')
        self.assertEqual(category_py.name, 'Toys', f"{flag}attribute type of category or something about attributes is nnot correct{flag}")
        self.assertEqual(category_py.sales, 534, f"{flag}attribute type of category or something about attributes is nnot correct{flag}")
        
        category_dj = Category.objects.get(id='c2')
        self.assertEqual(category_dj.name, 'Clothing', f"{flag}attribute type of category or something about attributes is nnot correct{flag}")
        self.assertEqual(category_dj.sales, 289, f"{flag}attribute type of category or something about attributes is nnot correct{flag}")
    
    def test_product_model(self):
        """
        Product model test
        """
        category_py = Category.objects.get(name='Toys')
        product = Product.objects.get(id = 'c1p1')
        self.assertEqual(product.name, 'Phone', f"{flag}attribute type of product or something about attributes is nnot correct{flag}")
        self.assertEqual(product.price, 141.34, f"{flag}attribute type of product or something about attributes is nnot correct{flag}")
        self.assertEqual(product.sales, 182, f"{flag}attribute type of product or something about attributes is nnot correct{flag}")
        self.assertEqual(product.category, category_py, f"{flag}attribute type of product or something about attributes is nnot correct{flag}")
    
    def test_str_method(self):
        """
        str method correctness test
        """
        category_py = Category.objects.get(name='Toys')
        product = Product.objects.get(name='Phone')
        
        self.assertEqual(str(category_py), 'Toys', f"{flag}str method has some problem{flag}")
        self.assertEqual(str(product), 'Phone',  f"{flag}str method has some problem{flag}")

