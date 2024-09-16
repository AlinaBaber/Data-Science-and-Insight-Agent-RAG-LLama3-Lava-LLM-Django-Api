from rest_framework import views, status
from rest_framework.response import Response
from .tasks import run_pipeline_async

class RunPipelineView(views.APIView):
    def post(self, request):
        data = request.data
        run_pipeline_async.delay(data)  # `.delay()` is used to run the task asynchronously
        return Response({"message": "Pipeline is running in the background"}, status=status.HTTP_202_ACCEPTED)
#celery -A your_project worker -l info
