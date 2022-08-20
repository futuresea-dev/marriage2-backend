from django.contrib import admin

# Register your models here.
from .models import inviteMarried_request

class inviteMarried_request_Admin(admin.ModelAdmin):
    search_fields=['maleName']    
    list_filter= ['location']


admin.site.register(inviteMarried_request,inviteMarried_request_Admin)
