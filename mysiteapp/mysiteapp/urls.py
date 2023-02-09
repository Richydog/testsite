"""mysiteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import register, user_login, user_logout, Home, PostsByCategory, GetPost, PostsByTag, add_posts, Search, \
    profile, PostUpdateView, PostDeleteView,  CreateComm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #   path('', include('blog.urls')),
    path('', Home.as_view(), name='home'),
    path('register/', include('blog.urls')),
    path('login/', include('blog.urls')),
    path('logout/', include('blog.urls')),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    #    path('post/<str:slug>/', get_post, name='post'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    #  path('category/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('add-post/', add_posts, name='add_posts'),
    path('search/', Search.as_view(), name='search'),
    path('profile/', profile, name='profile'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('add_comm/', CreateComm.as_view(), name='comment'),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
