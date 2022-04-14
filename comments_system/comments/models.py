from django.db import models


class Post(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=30)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=30)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True,
        null=True, related_name='child_comment', default=None)
    level = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['-created']

    def set_level(self):
        self.level = self.parent.level + 1
