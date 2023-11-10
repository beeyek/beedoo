from django.http import JsonResponse
from .models import Reports
from scripts.selenium_script import run_selenium_script

def get_report_by_id(request, report_id):
    try:
        report = Reports.objects.values().get(id=report_id)
        result = run_selenium_script(report)
        response_data = {
            'result': result
        }
    except Reports.DoesNotExist:
        response_data = {
            'error': 'Report not found'
        }

    return JsonResponse(response_data)
