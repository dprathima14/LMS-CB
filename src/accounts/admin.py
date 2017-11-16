from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
	list_display = ["__str__", "username", "email"]
	search_fields = ["username", "email"]
	list_filter = ('admin', 'staff', 'is_active')
	fieldsets = (
		(None, {'fields': ('username', 'full_name', 'email', 'password', 'courses')}),
		# ('Full name', {'fields': ()}),
		('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2')}
		),
	)

	ordering = ('email',)
	filter_horizontal = ()

	#class Meta:
	#	model = User

admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
