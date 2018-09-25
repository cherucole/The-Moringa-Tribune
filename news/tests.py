from django.test import TestCase
#instead of importing items/classes one by one use * to import everything
from .models import *
import datetime as dt

#Create your tests here.
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

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james = Editor(first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(title='Test Article', post='This is a random test Post', editor=self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

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
