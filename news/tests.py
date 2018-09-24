from django.test import TestCase
#instead of importing items/classes one by one use * to import everything
from .models import *

# Create your tests here.
class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.cheruiyot=Editor(first_name='Cheruiyot', last_name='Collins', email='noreply@gmail.com')

#testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cheruiyot,Editor))
