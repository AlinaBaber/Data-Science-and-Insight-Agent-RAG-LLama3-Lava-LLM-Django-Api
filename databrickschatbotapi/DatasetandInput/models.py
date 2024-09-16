from django.db import models
from databrickschatbotapi.DataSciencePipelineProcess.models import DataSciencePipelineProcess
from databrickschatbotapi.ProblemType.models import ProblemType

class DatasetandInput(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='datasets/')
    target_variable = models.CharField(max_length=100)
    #problemtype = models.CharField(max_length=100)
    datetime_column = models.CharField(max_length=100, blank=True, null=True)

    # Adding a foreign key relationship to DataSciencePipelineProcess
    # `on_delete=models.CASCADE` specifies that if the referenced DataSciencePipelineProcess is deleted,
    # the associated Dataset should also be deleted.
    process = models.ForeignKey(
        DataSciencePipelineProcess,
        on_delete=models.CASCADE,
        related_name='datasets'
    )
    # Foreign key to ProblemType
    problem_type = models.ForeignKey(
        ProblemType,
        on_delete=models.SET_NULL,  # Set to NULL if the ProblemType is deleted
        null=True,                 # This field is optional
        related_name='datasets'
    )

    def __str__(self):
        return f"{self.file.name} ({self.problem_type.type if self.problem_type else 'No Type'}) - Process ID: {self.process.id}"
