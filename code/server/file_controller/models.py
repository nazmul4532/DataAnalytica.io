from django.db import models

class FileMetadata(models.Model):
    file_name = models.CharField(max_length=255)
    cloudinary_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    modified_file = models.JSONField(default=list)
    operations = models.JSONField(default=list)
    user_id = models.CharField(max_length=255)  
    edited_file = models.URLField()
    
