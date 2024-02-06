from django.urls import path
from .import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.home, name='home'),
  
  
    path('view_history',views.view_history, name="view_history"),

    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user'),
    path('scores_hist/<int:id>',views.score_hist, name='scores_hist'),
   

    
    path('reset_password_form/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="reset_password_form"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="reset_password"),
    path('reset_password_sent_done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name ="setup_password"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),  
]



