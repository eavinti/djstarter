from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from apps.accounts.models import Account


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'
    readonly_fields = [
        'id', 'date_of_birth',
    ]


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'get_name', 'date_joined', 'is_superuser', 'is_staff', 'is_active')
    inlines = (AccountInline, )
    ordering = ['-date_joined']

    def get_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)