from django.db import models
from databrickschatbotapi.DataSciencePipelineProcess.models import DataSciencePipelineProcess


class ProcessLog(models.Model):
    id = models.AutoField(primary_key=True)
    process = models.ForeignKey(
        DataSciencePipelineProcess,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Log for Process ID {self.process.id} at {self.timestamp}: {self.message[:50]}"
