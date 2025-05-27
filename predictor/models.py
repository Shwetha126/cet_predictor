from django.db import models
from django.contrib.auth.models import User

class Marks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cet_marks = models.FloatField()
    puc_marks = models.FloatField()
from django.db import models

class Prediction(models.Model):
    cet_marks = models.FloatField()
    puc_marks = models.FloatField()
    predicted_rank = models.FloatField()
    admission_probability = models.FloatField()

    def __str__(self):
        return f"Prediction: Rank {self.predicted_rank}, Probability {self.admission_probability}"

    def predicted_rank(self):
        return 50000 - (self.cet_marks * 300 + self.puc_marks * 100)  # Example formula

    def admission_probability(self):
        rank = self.predicted_rank()
        if rank < 10000:
            return "High"
        elif rank < 30000:
            return "Moderate"
        else:
            return "Low"