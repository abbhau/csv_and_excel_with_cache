from django.urls import path
from .views import CsvView, ExcelView

urlpatterns = [
    path('csvs/<str:country>/', CsvView.as_view(), name='csvs'),
    path('excels/', ExcelView.as_view(), name='excels')
]