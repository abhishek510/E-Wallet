from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WalletUserCreationForm, WalletUserChangeForm
from .models import WalletUser


class CustomUserAdmin(UserAdmin):
    add_form = WalletUserCreationForm
    form = WalletUserChangeForm
    model = WalletUser
    list_display = ('phone_number', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)


admin.site.register(WalletUser, CustomUserAdmin)