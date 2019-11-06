from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.utils import timezone


class Map(models.Model):
    """
    Сущность карт
    """
    image = models.ImageField(verbose_name="Изображение карты", upload_to="map_img/")
    passcode = models.TextField(verbose_name="Кодовое слово", max_length=300)
    token = models.TextField(verbose_name="ссылка", max_length=20)


# class Hrono(models.Model):
#     """
#     Сущность что за чем идёт
#     """
#     main = models.ForeignKey(Map, on_delete=models.CASCADE)
#     prev = models.ForeignKey(Map, on_delete=models.CASCADE, blank=True, null=True)
#     next = models.ForeignKey(Map, on_delete=models.CASCADE, blank=True, null=True)


class Answer(models.Model):
    """
    Ответ на карту
    """
    answer = models.TextField(verbose_name="Ответ", max_length=300)
    timecode = models.DateTimeField(default=timezone.now)
    # correct = models.BooleanField(verbose_name="Правильный", default=False)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    group = models.ForeignKey(User, on_delete=models.CASCADE)
