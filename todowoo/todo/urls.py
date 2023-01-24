from django.urls import path
from . import views


app_name = 'todo'


urlpatterns = [
    # Auth Pathes
        path('login/', views.login_user, name='login'),
        path('logout/', views.logout_user, name='logout'),
        path('signup/', views.signup_user, name='signup'),
        
    # Todo Pathes
        path('', views.home, name='home'),
        path('create/', views.create, name='create'),
        path('completed/', views.completed, name='completed'),
        path('current/', views.current, name='current'),
        path('todo/<int:id>/', views.details, name='details'),
        path('todo/<int:id>/complete/', views.complete, name='complete'),
        path('todo/<int:id>/delete/', views.delete, name='delete'),
]

