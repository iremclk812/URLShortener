from django.db import models
from django.db import models


class URL(models.Model):
    long_url = models.URLField("Original URL")
    short_url = models.CharField("Short URL", max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.PositiveIntegerField("Attempt Count", default=1)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url} (Attempts: {self.attempts})"

# Create your models here.
