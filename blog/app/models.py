from django.db import models
import uuid
class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class Blog(models.Model):
    pass
class Reviews(models.Model):
    pass