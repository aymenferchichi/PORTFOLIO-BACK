from django.db import models


class Journey(models.Model):
    slug = models.SlugField(unique=True)
    year = models.CharField(max_length=40)
    title = models.CharField(max_length=160)
    eyebrow = models.CharField(max_length=160)
    detail = models.TextField()
    summary = models.TextField()
    focus = models.JSONField(default=list, blank=True)
    accent = models.CharField(max_length=20)
    display_order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f'{self.display_order}: {self.title}'
