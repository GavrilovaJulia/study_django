from django.db import models
from django.utils import timezone
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(default=timezone.now(), verbose_name="Дата публикации")
    image = models.ImageField(upload_to='images/', verbose_name="Картинка")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blogs/{self.id}'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
