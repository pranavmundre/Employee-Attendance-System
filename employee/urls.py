from django.urls import path, include

from employee import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todays-attendance', views.todays_attendance, name='todays_attendance'),
    path('update-todays-attendance', views.update_todays_attendance, name='update_todays_attendance'),
    path('all-attendance', views.all_attendance, name='all_attendance'),
]
