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


    #testing the save method
    def test_save_method(self):
        self.cheruiyot.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def tearDown(self):

        # Editor.objects_all = []

        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    #
    # def test_delete_object(self):
    #     '''
    #     this is to ensure we can remove a social account from our list
    #     '''
    #     self.cheruiyot.save_editor()
    #     test_object = Editor(first_name='Cheruiyot', last_name='Collins', email='noreply@gmail.com') #new account to save
    #     test_object.save_editor()
    #
    #     self.test_object.delete_object()
    #     self.assertEqual(len(Editor.objects_all),1)
