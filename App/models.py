from django.db import models
from django.contrib.auth.models import User


## CHOICES ##


class UserStatus(models.TextChoices):
    IN_TEAM = "In team"
    BENCH = "Bench"
    FIRED = "Fired"


class Role(models.TextChoices):
    WORKER = "Worker"
    MANAGER = "Manager"
    ADMIN = "Admin"


class TaskStatus(models.TextChoices):
    BACKLOG = "Backlog"
    READY_TO_DEV = "Ready to development"
    IN_PROGRESS = "In progress"
    READY_TO_QA = "Ready to Quality Assurance"
    PRODUCTION = "Production"


## MODELS ##


class CustomUser(models.Model):
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #?
    worker_status = models.CharField(max_length=7, choices=UserStatus.choices, default=UserStatus.BENCH)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.WORKER)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=255)

    workers = models.ManyToManyField(CustomUser, related_name='team_workers', limit_choices_to={
        "worker_status": UserStatus.BENCH,
        "role": Role.WORKER,
    },
                                     blank=True)

    managers = models.ManyToManyField(CustomUser, related_name='team_managers', limit_choices_to={
        "role": Role.MANAGER,
    },
                                      blank=True)

    # secret_token_key


class TaskImage(models.Model):
    image = models.ImageField()


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    connection_with_another_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    task_status = models.CharField(max_length=26, choices=TaskStatus.choices, default=TaskStatus.BACKLOG)
    image = models.ManyToManyField(TaskImage)
    responsible_team = models.ForeignKey(Team, related_name='tasks_team', on_delete=models.CASCADE)
    responsible_employee = models.ForeignKey(CustomUser, related_name='task_employee', blank=True, on_delete=models.CASCADE)

    @property
    def comments_count(self):
        return self.comments.count()


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='TaskComments')
    text = models.TextField(max_length=2550)
