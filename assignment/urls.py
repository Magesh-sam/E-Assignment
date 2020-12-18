from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('faculty/', views.faculty, name="faculty"),

    path('createassignment/', views.createassignment, name="createassignment"),
    path('updateassignment/<str:pk>/',
         views.updateassignment, name="updateassignment"),
    path('deleteassignment/<str:pk>/',
         views.deleteassignment, name="deleteassignment"),



    path('submitform', views.model_form_upload, name="submitform"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
