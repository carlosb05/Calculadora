from django.contrib import admin
from .models.user import User
from .models.record import Record

admin.site.register(User)
admin.site.register(Record)
# Register your models here.
