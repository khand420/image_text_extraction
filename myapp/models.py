from django.db import models

class ImageText(models.Model):
    image = models.ImageField(upload_to='images/')
    extracted_text = models.TextField()
    bold_words = models.TextField()
    image_base64 = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ImageText {self.id}"