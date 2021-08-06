import os
from django.test import TestCase
from django.conf import settings

flag = f"------------------------------------------------------------------"


#
# this file is used to fulfill unit test of the whole project structure.
#



class StructureTests(TestCase): 
    """
    foundation
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.rango_app_dir = os.path.join(self.project_base_dir, 'rango')
    
    def test_project_created(self):
        """
        project configuration directory tests
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'tango_with_django_project'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'tango_with_django_project', 'urls.py'))
        
        self.assertTrue(directory_exists, f"{flag}project directory does not exist{flag}")
        self.assertTrue(urls_module_exists, f"{flag}the core urls.py file does not exist{flag}")
    
    def test_rango_app_created(self):
        """
        app conf
        """
        directory_exists = os.path.isdir(self.rango_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.rango_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.rango_app_dir, 'views.py'))
        
        self.assertTrue(directory_exists, f"{flag}app directory does not exist{flag}")
        self.assertTrue(is_python_package, f"{flag}app is missing files{flag}")
        self.assertTrue(views_module_exists, f"{flag}app is missing files{flag}")
    
    def test_rango_has_urls_module(self):
        """
        separate urls
        """
        module_exists = os.path.isfile(os.path.join(self.rango_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{flag}app's urls.py is missing{flag}")
    
    def test_is_rango_app_configured(self):
        """
        install app 
        """
        is_app_configured = 'rango' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{flag}app is not in INSTALLED_APPS.{flag}")
  
