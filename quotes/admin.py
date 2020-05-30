from django.contrib import admin

# Register your models here.

from . models import tbl_category
from . models import tbl_adminPost

admin.site.register(tbl_category)
admin.site.register(tbl_adminPost)
