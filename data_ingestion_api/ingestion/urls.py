from django.urls import path
from .views import FileUploadView, RetrieveDataView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('statistics/', RetrieveDataView.as_view(), name='retrieve-data'),
]
