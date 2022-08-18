from django.contrib import admin
from .models import Team, TaskImage, Task, TaskComment, CustomUser


admin.site.register(Team)
admin.site.register(TaskImage)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(CustomUser)
