from django.urls import path
from resumes.views import index

app_name = "pages"

urlpatterns = [
    path("", index, name="home")
]