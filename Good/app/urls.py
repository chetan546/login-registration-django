from django.urls import path,re_path
from . import views

app_name = 'app'

urlpatterns = [

    path("", views.index, name='index'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("register/",views.register, name='register'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.PostDetailView.as_view(),name='detail'),
    path('create',views.PostCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.PostDeleteView.as_view(), name='delete'),

]