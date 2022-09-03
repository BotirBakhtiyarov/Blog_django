from django.urls import path, include
from . import views

urlpatterns =[
    # path('base/', views.base, name='base'),
    path('', views.IndexListView.as_view(), name='index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='project'),
    path('update/<int:pk>/', views.BlogUpdateView, name='update'),
    path('create', views.BlogCreateView, name='create'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
