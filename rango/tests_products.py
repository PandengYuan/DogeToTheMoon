import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

flag = f"------------------------------------------------------------------"

#
# this file is used to fulfill  unit test  of products.
#


class ProductTests(TestCase):
    """
    url mapping
    """
    def setUp(self):
        self.views_module = importlib.import_module('rango.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('tango_with_django_project.urls')
    
    def test_view_exists(self):
        """
        whether views exist and functional
        """
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.index)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'login' in self.views_module_listing
        is_callable = callable(self.views_module.login)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'register' in self.views_module_listing
        is_callable = callable(self.views_module.register)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'add_category' in self.views_module_listing
        is_callable = callable(self.views_module.add_category)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'cart' in self.views_module_listing
        is_callable = callable(self.views_module.cart)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'payment' in self.views_module_listing
        is_callable = callable(self.views_module.payment)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'product_search' in self.views_module_listing
        is_callable = callable(self.views_module.product_search)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'upload_product' in self.views_module_listing
        is_callable = callable(self.views_module.upload_product)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        name_exists = 'remove_product' in self.views_module_listing
        is_callable = callable(self.views_module.remove_product)


        self.assertTrue(name_exists, f"{flag} index() view does not exist.{flag}")
        self.assertTrue(is_callable, f"{flag}created index() view correctly, but does not functional{flag}")


        
