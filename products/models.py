from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    image = models.FileField(upload_to="products/category_img/",blank=True,null=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1

            while Category.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter+=1
            
            self.slug = unique_slug
        
        super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    slug = models.SlugField(unique=True,blank=True)
    image = models.ImageField(upload_to="products/product_img/",blank=True,null=True)

    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products",)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1

            while Product.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter+=1
            
            self.slug = unique_slug
        
        super().save(*args, **kwargs)


