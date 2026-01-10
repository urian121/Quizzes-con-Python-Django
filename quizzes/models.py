from django.db import models

class QuizQuestion(models.Model):
    pregunta = models.TextField()
    opciones = models.JSONField()
    respuesta_correcta = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.id}. {self.pregunta[:60]}"
