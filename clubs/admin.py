from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import StudentClubsTitle, Announcement, About, Club, ClubItems


class AnnouncementAdmin(SummernoteModelAdmin):
    summernote_fields = ('announcement_description',)

class ClubAdmin(admin.ModelAdmin):
    pass

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_description')

admin.site.register(StudentClubsTitle)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(ClubItems)
