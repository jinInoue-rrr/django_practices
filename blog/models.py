## 以下、写経

from django.conf import settings
from django.db import models
from django.utils import timezone

## Postは定義されるオブジェクトの名前（大文字から始める）
## 

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # publishと__str__はPostのメソッドなのでインデントしている
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
