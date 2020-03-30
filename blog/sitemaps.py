from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['blog-about']
    def location(self,item):
        return reverse(item)

class StaticViewSitemap1(Sitemap):
    def items(self):
        return ['blog-services']
    def location(self,item):
        return reverse(item)

class StaticViewSitemapc(Sitemap):
    def items(self):
        return ['blog-courses']
    def location(self,item):
        return reverse(item)
