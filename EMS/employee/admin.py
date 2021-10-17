from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(employee)
class Employee_table(admin.ModelAdmin):
	search_fields=(
		'emp_id',
		'User_id__email',
		'User_id__first_name',
		'User_id__last_name',
		'designation',
		"Department_id__name"
	)
	list_display = ['User_id','Department','designation']
	# list_filter = ["Slot_id__Timing_id__Shift_id"]
	# readonly_fields = ('timestamp',)

@admin.register(department)
class department_table(admin.ModelAdmin):
	# search_fields=(
	# 	'emp_id',
	# 	'email',
	# 	'User_id__first_name',
	# 	'User_id__last_name',
	# 	'designation',
	# 	"Department_id__name"
	# )
	# list_display = ['user_id','Division_id','ip']
	# list_filter = ["Slot_id__Timing_id__Shift_id"]
	# readonly_fields = ('timestamp',)
	pass


@admin.register(attendance)
class attendance_table(admin.ModelAdmin):
	# search_fields=(
	# 	'emp_id',
	# 	'email',
	# 	'User_id__first_name',
	# 	'User_id__last_name',
	# 	'designation',
	# 	"Department_id__name"
	# )
	list_display = ['Employee_id','entry_time','exit_time']
	# list_filter = ["Slot_id__Timing_id__Shift_id"]
	# readonly_fields = ('timestamp',)
	pass