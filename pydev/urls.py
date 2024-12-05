from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("resumes/", include("resumes.urls")),
    path("", include("pages.urls")),
]
