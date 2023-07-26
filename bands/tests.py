from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Bands

class BandsTest(TestCase):
      
      @classmethod
      def setUpTestData(cls):
          testuser1 = get_user_model().objects.create_user(
              username='testuser1', password='1234'
          )
  
          testuser1.save()
  
          test_bands = Bands.objects.create(
              owner = testuser1,
              name = 'Nirvana',
              members = 'Kurt Cobain'
          )
  
          test_bands.save()

          test_bands_2 = Bands.objects.create(
              owner = testuser1,
              name = 'Foo Fighters',
              members = 'Dave Grohl'
          )
          test_bands_2.save()
  
      def test_bands_content(self):
          bands = Bands.objects.get(id=1)
          actual_owner = str(bands.owner)
          actual_name = str(bands.name)
          actual_members = str(bands.members)
  
          self.assertEqual(actual_owner, 'testuser1')
          self.assertEqual(actual_name, 'Nirvana')
          self.assertEqual(actual_members, 'Kurt Cobain',)

      def test_bands_2_content(self):
          bands = Bands.objects.get(id=2)
          actual_owner = str(bands.owner)
          actual_name = str(bands.name)
          actual_members = str(bands.members)
  
          self.assertEqual(actual_owner, 'testuser1')
          self.assertEqual(actual_name, 'Foo Fighters')
          self.assertEqual(actual_members, 'Dave Grohl')

    
