from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(email='test@gmail.com', password='test')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='test')
            

            