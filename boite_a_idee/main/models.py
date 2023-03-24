from django.db import models
from django.utils import timezone
from authentication.models import User


class Idea(models.Model):
    title=models.CharField(max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField(max_length=200, blank=True, null=True)
    time_ordered = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self) -> str:
        return f"{self.title} - {self.description}"
    class Meta:
        verbose_name_plural = "Ideas"
        
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    time_liked = models.DateTimeField(default=timezone.now)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    time_disliked = models.DateTimeField(default=timezone.now)
        
