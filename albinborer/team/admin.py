from django.contrib import admin
from team.models import Designation,Member,AccessRecord

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    fields = ('name', 'email_url','tele_phone','tele_fax')

admin.site.register(Designation)
admin.site.register(Member)
admin.site.register(AccessRecord)


