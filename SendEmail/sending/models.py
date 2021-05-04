from django.db import models


class SendEmailModel(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=500, default="Hello!")
    file = models.FileField(default='files/LINEAR-ALGEBRA.pdf')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
