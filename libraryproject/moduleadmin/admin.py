from django.contrib import admin

# Register your models here.
from .models import admindetails,bookdetails,studentdetails
admin.site.register(admindetails)
admin.site.register(bookdetails)
admin.site.register(studentdetails)