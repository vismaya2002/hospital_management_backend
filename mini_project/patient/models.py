from django.db import models
#from django.contrib.auth.models import User
'''from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone



# Create your models here.


class UserManager(BaseUserManager):

  def _create_user(self, email, password,first_name,last_name,contact1,contact2,address,state,city,is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        first_name=first_name,
        last_name=last_name,
        contact1=contact1,
        contact2=contact2,
        address=address,
        state=state,
        city=city,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, first_name,last_name,contact1,contact2,address,state,city, **extra_fields):
    return self._create_user(email, password, first_name,last_name,contact1,contact2,address,state,city, False, False, **extra_fields)

  def create_superuser(self, email, password, first_name,last_name,contact1,contact2,address,state,city, **extra_fields):
    user=self._create_user(email, password, first_name,last_name,contact1,contact2,address,state,city, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','contact1','contact2','address','state','city']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)'''




'''class addInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField()'''



