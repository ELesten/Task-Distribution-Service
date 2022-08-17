from django.urls import path, include

routes = [
    path("first/", include("App.urls")),
]
