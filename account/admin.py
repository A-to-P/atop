from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(ConsultantProfile)
admin.site.register(RestaurantProfile)
admin.site.register(EduVerification)
