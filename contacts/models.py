from django.db import models


class ContactMessage(models.Model):
	class Status(models.TextChoices):
		NEW = 'new', 'New'
		READ = 'read', 'Read'
		REPLIED = 'replied', 'Replied'

	name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=180)
	phone = models.CharField(max_length=40, blank=True)
	message = models.TextField()
	status = models.CharField(
		max_length=20,
		choices=Status.choices,
		default=Status.NEW,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name} - {self.subject}"
