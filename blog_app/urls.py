from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.login_view, name='login'),
    # path('register/', views.register, name='register'),
    path('detail/<slug>/', views.blog_detail, name='blog_detail'),
    path('addblog/', views.add_blog, name='add_blog'),
    path('seeblog/', views.see_blog, name='see_blog'),
    path('blogdelete/<int:id>/', views.blog_delete, name='blog_delete'),
    path('blogupdate/<slug>/', views.blog_update, name='blog_update'),
    path('logout/', views.logout_view, name='logout_view'),
]