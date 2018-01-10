from django.contrib import admin
from schedule.models import WorkTime, MonthShift, StaffSchedule, NgShift, GuestSchedule

# Register your models here.
#### base classes ####

class DateAdmin(admin.ModelAdmin):

    def schedule_date(self,obj):
        return obj.strfdate()

    date_hierarchy = 'date'

class TimeTableAdmin(admin.ModelAdmin):

    def time_table(self,obj):
        return obj.strftimetable()

#### Main Classes ####
##### staff #####
class MonthShiftAdmin(admin.ModelAdmin):
    list_display = ('year','month','groupschedule','completed',)
    list_filter = ('groupschedule',)

admin.site.register(MonthShift,MonthShiftAdmin)

class WorkTimeAdmin(TimeTableAdmin):
    list_display = ('title','time_table',)
    list_filter = ('groupschedule',)

admin.site.register(WorkTime,WorkTimeAdmin)

class StaffScheduleAdmin(DateAdmin):
    list_display = ('schedule_date','staff','worktime',)
    list_filter = ('staff__groupschedule','date','staff',)

admin.site.register(StaffSchedule,StaffScheduleAdmin)

class NgShiftAdmin(DateAdmin):
    list_display = ('staff','schedule_date','get_values')

    def get_values(self,obj):
        return obj.ng_values()

    list_filter = ['date','staff',]

admin.site.register(NgShift,NgShiftAdmin)

##### guest #####
class GuestScheduleAdmin(DateAdmin,TimeTableAdmin):
    list_display = ('schedule_date','guest','time_table',)

    list_filter = ['date','guest',]

admin.site.register(GuestSchedule,GuestScheduleAdmin)

