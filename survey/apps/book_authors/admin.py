# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Book, Author
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)