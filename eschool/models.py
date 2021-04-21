import uuid
from djongo import models
from django.contrib.auth.models import User


# Create your models here.
class Lesson(models.Model):
  CHOICES = (
    ('YT', 'YouTube'),
    ('FB', 'Facebook'),
    ('OK', 'Одноклассники'),
    ('DM', 'Dailymotion'),
    ('VM', 'Vimeo'),
  )

  lesson_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
  title = models.CharField(max_length=255)
  published_date = models.DateTimeField()
  categories = models.TextField()
  content = models.TextField()
  video_type = models.CharField(max_length=255, choices = CHOICES, default=1)
  video_id = models.CharField(max_length=255, blank=True)
  published_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  