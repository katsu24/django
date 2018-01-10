from django.contrib import admin
from owner.models import GroupSchedule

# Register your models here.
class GroupScheduleAdmin(admin.ModelAdmin):
    list_display = ('group','owner',)

admin.site.register(GroupSchedule,GroupScheduleAdmin)