from django.core.validators import FileExtensionValidator
from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg'])])
    pdf = models.FileField(upload_to='pdf/', validators=[FileExtensionValidator(['pdf'])])
