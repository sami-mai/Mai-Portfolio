from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(allow_unicode=True, unique=True, default='')
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']

    @classmethod
    def project_item(cls):
        project = cls.objects.all()
        return project
