from django.contrib import admin
from personalinfo import models


# Register your models here.
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'jtimestamp']
   
    class Meta:
        model = models.ContactProfile



admin.site.register(models.User)
admin.site.register(models.Skill)
admin.site.register(models.Testimonial)
admin.site.register(models.Certificate)
admin.site.register(models.Interested)
admin.site.register(models.Academic)
admin.site.register(models.Job)
admin.site.register(models.Publication)
admin.site.register(models.Portfolio)
admin.site.register(models.ContactProfile, ContactProfileAdmin)