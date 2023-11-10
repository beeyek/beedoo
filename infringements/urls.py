from django.urls import path
from .views import get_report_by_id

urlpatterns = [
    path('<int:report_id>/', get_report_by_id, name='get_report_by_id'),
]
