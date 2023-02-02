from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', login_required(auth_views.LogoutView.as_view(template_name='registration/logout.html')), name='logout'),
    path('', views.Start.as_view(), name="start"),
    path('home/', views.Home.as_view(), name="post_list_all"),
    path('myposts/', login_required(views.PostList.as_view()), name="post_list"),
    path('myposts/<int:pk>/edit', login_required(views.PostUpdate.as_view()), name='post_update'),
]

urlpatterns += staticfiles_urlpatterns()
