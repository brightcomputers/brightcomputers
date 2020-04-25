from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tinymce_models
# Create your models here.
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Post(models.Model):
    title=models.CharField(max_length=150)
    content=tinymce_models.HTMLField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
