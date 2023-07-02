from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff']

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
