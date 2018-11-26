from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.



class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='manka',first_name='mehdi',last_name='Marcus',email='manka@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_data(self):
        self.assertTrue(self.user.username,"manka")
        self.assertTrue(self.user.first_name,"mehdi")
        self.assertTrue(self.user.last_name,'Mutuma')
        self.assertTrue(self.user.email,'manka@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)
class NeighbourhoodTestClass(TestCase):
  """
  Tests Neighborhood class and its functions
  """
  def setUp(self):
      self.hood = Neighbourhood(name='test',description='test')

  def test_instance(self):
      self.assertTrue(isinstance(self.hood, Neighbourhood))

  def test_save_method(self):
      """
      Function to test that a neighborhood is being saved
      """
      self.hood.save_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertTrue(len(hoods) > 0)

  def test_delete_method(self):
      """
      Function to test that a neighborhood can be deleted
      """
      self.hood.save_neighbourhood()
      self.hood.delete_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertTrue(len(hoods) == 0)



class BusinessTestClass(TestCase):
  """
  Tests Business Class and its functions
  """
  def setUp(self):
      self.hood = Neighbourhood(name='test',description='test')
      self.biz = Business(name='test',category='test')

  def test_instance(self):
      self.assertTrue(isinstance(self.biz, Business))

  def test_save_method(self):
      """
      Function to test that a business is being saved
      """
      self.biz.save_business()
      bizs = Business.objects.all()
      self.assertTrue(len(bizs) > 0)

  def test_delete_method(self):
      """
      Function to test that a business can be deleted
      """
      self.biz.save_business()
      self.biz.delete_business()
      self.assertTrue(len(bizs) == 0)
