from django.db import models
from django_gallery.settings import AUTH_USER_MODEL


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gallery_added')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.name) + ' - ' + str(self.user_id.email)

    class Meta:
        verbose_name_plural = "User Gallery"