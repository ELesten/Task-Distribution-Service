from django.contrib import admin
from .models import Team, CustomUser, TaskImage, Task, TaskComment


admin.site.register(Team)
admin.site.register(CustomUser)
admin.site.register(TaskImage)
admin.site.register(Task)
admin.site.register(TaskComment)
