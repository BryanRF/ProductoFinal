from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path("finals/", include("finals.urls")),
    path("api/", include("finals.urls_apis")),
]
