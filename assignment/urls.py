from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

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

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="assignment/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="assignment/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="assignment/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="assignment/password_reset_done.html"),
         name="password_reset_complete"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
