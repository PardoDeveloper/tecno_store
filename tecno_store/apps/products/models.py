from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ManyToManyField(Category)     
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"Image of {self.product.name}"