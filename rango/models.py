from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# category table structure
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    CHAR_MAX_LENGTH = 128
    id = models.CharField(max_length=CHAR_MAX_LENGTH, primary_key=True)
    name = models.CharField(max_length=CHAR_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)
    sales = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='product_images', blank=True)

    # deal with slug to achieve the url functionality
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    # adjust class name
    class Meta:
        verbose_name_plural = 'Categories'

    # toString method
    def __str__(self):
        return self.name


# product table structure
class Product(models.Model):
    CHAR_MAX_LENGTH = 128
    # a product must belong to a category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id = models.CharField(max_length=CHAR_MAX_LENGTH, primary_key=True)
    name = models.CharField(max_length=CHAR_MAX_LENGTH, unique=True)
    description = models.FileField(upload_to='product_description', blank=True)
    # detailed_description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    sales = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    picture = models.ImageField(upload_to='product_images', blank=True)

    # slug problem . same as category
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# cart table structure   
class Cart(models.Model):
    CHAR_MAX_LENGTH = 128
    buyer_name = models.CharField(max_length=CHAR_MAX_LENGTH, default='')
    product_name = models.CharField(max_length=CHAR_MAX_LENGTH, default='')

    def __str__(self):
        return self.buyer_name + self.product_name

# search area on the page 
class Search(models.Model):
    CHAR_MAX_LENGTH = 128
    content = models.CharField(max_length=CHAR_MAX_LENGTH, default='')

    def __str__(self):
        return self.content


# userprofile table structure
class UserProfile(models.Model):
    CHAR_MAX_LENGTH = 128
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    address = models.CharField(max_length=CHAR_MAX_LENGTH, default='', blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    usertype = models.CharField(max_length=CHAR_MAX_LENGTH, default='')

    def __str__(self):
        return self.user.username


