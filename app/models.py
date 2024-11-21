from django.db import models

class DifyModel(models.Model):
    query = models.TextField(
        max_length=300,
    ) 
    answer = models.CharField(
        max_length=600
    )
    conversation_id = models.CharField(
        max_length=300,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    ) 
    def __str__(self):
        return self.query
