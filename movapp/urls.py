from .import views
from django.urls import path
app_name='movapp'

urlpatterns = [
    path('', views.movie, name='movie'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('addMovie/', views.addMovie, name='addMovie'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('search/', views.searchBar, name='search'),

]