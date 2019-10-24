from django.contrib import admin
# from lawyer.models import Lawyer,State 
from .models import Practice_area,Lawyer,Sub_practice_area, State
# Register your models here.


class data_list(admin.ModelAdmin):
    list_display = ('sub_practice_area','practice_area','lawyer_id')

class data1_list(admin.ModelAdmin):
    list_display = ('practice_type','practice_id')

admin.site.register(Lawyer)
admin.site.register(State)
admin.site.register(Practice_area)
admin.site.register(Sub_practice_area,data1_list)
admin.site.register(Lawyer_practice_area,data_list)
admin.site.register(Data)
