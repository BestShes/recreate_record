from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'user_type', 'is_active', 'last_login')


admin.site.register(Member, MemberAdmin)
