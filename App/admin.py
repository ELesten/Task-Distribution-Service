from django.contrib import admin
from .models import Team, TaskImage, Task, TaskComment, CustomUser


class TaskCommentInline(admin.TabularInline):
    model = TaskComment


class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('image', )
    inlines = [
        TaskCommentInline,
    ]


class CustomUserInline(admin.TabularInline):
    model = CustomUser
    fields = ('username', 'first_name', 'last_name', )


class TeamAdmin(admin.ModelAdmin):
    fields = ('team_name', 'managers')
    filter_horizontal = ('managers', )

    inlines = [
        CustomUserInline,
    ]


admin.site.register(Team, TeamAdmin)
admin.site.register(TaskImage)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment)
admin.site.register(CustomUser)

