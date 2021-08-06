import os
import warnings
import importlib
from django.test import TestCase
from django.conf import settings


flag = f"------------------------------------------------------------------"

#
# this file is used to fulfill   unit test  of database config.
#

class DatabaseConfTests(TestCase):
    """
    database conf test
    """
    def setUp(self):
        pass
    
    def does_gitignore_include_database(self, path):
        """
        test gitignore functionality
        """
        f = open(path, 'r')
        
        for line in f:
            line = line.strip()
            
            if line.startswith('db.sqlite3'):
                return True
        
        f.close()
        return False
    
    def test_databases_variable_exists(self):
        """
        database settings variable configuration check
        """
        self.assertTrue(settings.DATABASES, f"{flag}settings module does not have a databases variable{flag}")
        self.assertTrue('default' in settings.DATABASES, f"{flag}default database configuration correct{flag}")
    
    def test_gitignore_for_database(self):
        """
         git ralevanted
        """
        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()
        
        if git_base_dir.startswith('fatal'):
            warnings.warn("not using Git repository")
        else:
            gitignore_path = os.path.join(git_base_dir, '.gitignore')
            
            if os.path.exists(gitignore_path):
                self.assertTrue(self.does_gitignore_include_database(gitignore_path), f"{flag}.gitignore file does not include 'db.sqlite3'{flag}")
            else:
                warnings.warn("not have .gitignore file ")
