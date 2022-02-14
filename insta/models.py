from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InstaPost(models.Model):
    """Model definition for InstaPost."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    likes = models.ManyToManyField(User)
    image_url = models.URLField()
    caption = models.CharField(max_length=100)
    post_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for InstaPost."""
        verbose_name = 'InstaPost'
        verbose_name_plural = 'InstaPosts'
    
    @property
    def no_of_likes(self):
        return self.likes.all().count()

    def __str__(self):
        """Unicode representation of InstaPost."""
        return f'{str(self.owner)}: {self.caption}'


class UserFollow(models.Model):
    """Model definition for UserFollow."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        """Meta definition for UserFollow."""
        verbose_name = 'UserFollow'
        verbose_name_plural = 'UserFollow'
        unique_together = ('user', 'follower')

    def __str__(self):
        """Unicode representation of UserFollow."""
        return f'{str(self.follower)} follows {str(self.user)}'

