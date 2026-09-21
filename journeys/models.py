from django.db import models


class Journey(models.Model):
    class Subcategory(models.TextChoices):
        EXPERIENCE = 'experience', 'Experience'
        PROJECTS = 'projects', 'Projects'

    slug = models.SlugField(unique=True)
    year = models.CharField(max_length=40)
    title = models.CharField(max_length=160)
    eyebrow = models.CharField(max_length=160)
    subcategory = models.CharField(
        max_length=20,
        choices=Subcategory.choices,
        default=Subcategory.EXPERIENCE,
    )
    detail = models.TextField()
    summary = models.TextField()
    client_label = models.CharField(max_length=160, blank=True, default='')
    project_scope = models.CharField(max_length=200, blank=True, default='')
    outcome_highlight = models.CharField(max_length=240, blank=True, default='')
    focus = models.JSONField(default=list, blank=True)
    deliverables = models.JSONField(default=list, blank=True)
    accent = models.CharField(max_length=20)
    display_order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f'{self.display_order}: {self.title}'
