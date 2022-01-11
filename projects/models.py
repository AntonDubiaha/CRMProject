from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.urls.base import reverse
from tinymce import models as tinymce_models


class Project(models.Model):
    name = CharField(max_length=50)
    description = tinymce_models.HTMLField()
    date_start = DateTimeField()
    date_end = DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='company_project')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'project_id': self.pk})
