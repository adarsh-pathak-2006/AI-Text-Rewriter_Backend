from django.db import models


class MainDB(models.Model):
    input=models.TextField()
    style=models.CharField(max_length=15, choices=[('PROFESSIONAL','Professional'), ('CASUAL', 'Casual'), ('RESPECT-TONED', 'Respect-Toned')])
    output=models.TextField(null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.input[:100]
