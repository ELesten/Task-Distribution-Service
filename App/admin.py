from django.contrib import admin
from .models import Team, TaskImage, Task, TaskComment, CustomUser


class TeamAdmin(admin.ModelAdmin):
    fields = ('team_name', 'managers')


admin.site.register(Team, TeamAdmin)
admin.site.register(TaskImage)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(CustomUser)
