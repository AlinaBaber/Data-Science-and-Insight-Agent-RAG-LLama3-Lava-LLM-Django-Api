from django.db import models
from django.forms import JSONField
from databrickschatbotapi.DataSciencePipelineProcess.models import DataSciencePipelineProcess

class DataSciencePipelineResult(models.Model):
    id = models.AutoField(primary_key=True)
    process = models.ForeignKey(
        DataSciencePipelineProcess,
        on_delete=models.CASCADE,
        related_name='results'
    )
    result_data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Results for Process ID {self.process.id} at {self.created_at}"
