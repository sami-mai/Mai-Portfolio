from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='projects/', blank=True)
    repoUrl = models.CharField(max_length=50)
    deployedUrl = models.CharField(max_length=50)

    def save_project(self):
        self.save()

    def del_project(self):
        self.delete()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
