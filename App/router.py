from django.urls import path, include

routes = [
    path("app/", include("App.urls")),
]
