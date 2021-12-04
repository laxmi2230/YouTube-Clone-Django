from django.db import models
from django.conf import settings


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # noqa: E501
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    parent = models.ForeignKey('Video', null=True, blank=True, on_delete=models.CASCADE)  # noqa: E501
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.post

    def get_comments(self):
        return Video.objects.filter(parent=self).order_by('-date')

    def calculate_comments(self):
        self.comments = Video.objects.filter(parent=self).count()
        self.save()
        return self.comments

    def comment(self, user, post):
        video_comment = Video(user=user, post=post, parent=self)
        video_comment.save()
        self.comments = Video.objects.filter(parent=self).count()
        self.save()
        return video_comment
