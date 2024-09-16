from celery import shared_task
from databrickschatbotapi.DatascientistPipeline.datasciencepipeline import run_data_pipeline  # assuming you have a function to run your pipeline

@shared_task
def run_pipeline_async(data):
    run_data_pipeline(data)
