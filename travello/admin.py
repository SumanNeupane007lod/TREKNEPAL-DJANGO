from django.contrib import admin
from .models import Destination,TrekkingGuide,Testimonials,News,Booked

# Register your models here.

admin.site.site_header="Trek Nepal admin panel"

class TrekkingGuideAdmin(admin.ModelAdmin):
    list_display=('name','email','status','phoneno')
    

class DestinationAdmin(admin.ModelAdmin):
    list_display=('name','price','offer')


admin.site.register(Destination,DestinationAdmin)
admin.site.register(TrekkingGuide,TrekkingGuideAdmin)
admin.site.register(Testimonials)
admin.site.register(News)

class BookedAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_no')
admin.site.register(Booked,BookedAdmin)

