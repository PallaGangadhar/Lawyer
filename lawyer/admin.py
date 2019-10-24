from django.contrib import admin
# from lawyer.models import Lawyer,State 
from .models import Practice_area,Lawyer,Sub_practice_area, State
# Register your models here.

admin.site.register(Lawyer)
admin.site.register(State)
admin.site.register(Practice_area)
admin.site.register(Sub_practice_area)

