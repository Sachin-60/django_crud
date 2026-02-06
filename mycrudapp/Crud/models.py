from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1, help_text="Rating out of 10")
    review = models.TextField()

    def __str__(self):
        return self.title

