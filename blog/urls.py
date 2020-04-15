from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdaetView, PostDeleteView, UserPostListView
from  .import views
from .sitemaps import PostSitemap,StaticViewSitemap,StaticViewSitemap1,StaticViewSitemapc
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import static

sitemaps={
    'posts':PostSitemap,
    'static':StaticViewSitemap,
    's':StaticViewSitemap1,
    'c':StaticViewSitemapc,

}

urlpatterns = [
    path('',views.home,name='home'),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('blog/',PostListView.as_view(),name='blog-home'),
    path('search/', views.search, name='search'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdaetView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),
    path('services/',views.services,name='blog-services'),
    path('courses/',views.courses,name='blog-courses'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='blog/password_change.html'),
        name='password_change'),
]
