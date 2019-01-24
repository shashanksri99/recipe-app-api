from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, \
                                        BaseUserManager, \
                                        PermissionsMixin
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new UserManager
        """
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db) #This is used to save into db "_db" allows us to use multiple Database

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    custome user model that supports using username as email of the User
    """
    email = models.EmailField(max_length = 256, unique = True)
    name = models.CharField(max_length = 256)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
