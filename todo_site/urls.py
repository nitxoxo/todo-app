
from django.contrib import admin
from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name="index"),  # main todo list
    path('toggle/<int:id>/', views.toggle_complete, name="toggle"),  # mark complete
    path('del/<int:item_id>/', views.remove, name="del"),  # remove task
    path('register/', views.register_view, name="register"),  # register
    path('login/', views.Login_view, name="login"), 
    path('edit/<int:id>/', views.edit_task, name="edit"),
    path('logout/', views.Logout_view, name="logout"),  # logout
    path('admin/', admin.site.urls),  # admin
]


