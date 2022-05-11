from django.db import models
import datetime


# Create your models here.
class UserComments(models.Model):
    user_comment = models.TextField(max_length=4000,help_text="User Personal Comment", default=True)
    review_date = models.DateTimeField(default=timezone.now)
    user_name = models.TextField(max_length=50,help_text="Name", default=True)
    def __str__(self) -> str:
            return self.user_comment


