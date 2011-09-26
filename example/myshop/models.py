from django.db import models
from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product
from shop.models.defaults.bases import BaseCart


class BookManager(PolymorphicManager):
    """A dumb manager to test the behavior with poylmorphic"""
    def get_all(self):
        return self.all()


class Book(Product):
    isbn = models.CharField(max_length=255)
    
    objects = BookManager()
    
    class Meta:
        pass


class MyCart(BaseCart):
    class Meta(object):
        abstract=False

