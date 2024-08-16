from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import APIKeyAuthentication
from .decorators import validate_request
from .models import UploadedData
import pandas as pd
import numpy as np

class FileUploadView(APIView):
    authentication_classes = [APIKeyAuthentication]

    @validate_request()
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        
        # Check if the uploaded file is a CSV
        if not file.name.endswith('.csv'):
            return Response({"error": "Only CSV files are allowed."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the file is empty
        if file.size == 0:
            return Response({"error": "The uploaded file is empty."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Read CSV file into a DataFrame
            df = pd.read_csv(file)
            
            # Convert DataFrame to the desired JSON format
            data = df.to_dict(orient='list')
            
            # Store the data in the database
            uploaded_data = UploadedData.objects.create(data=data)            
            return Response({"message": "File uploaded and data stored successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveDataView(APIView):
    authentication_classes = [APIKeyAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            # Retrieve all uploaded data
            all_data = UploadedData.objects.all()
            
            # Prepare response
            response_data = {}
            
            for data in all_data:
                # Convert JSON data to DataFrame
                df = pd.DataFrame(data.data)
                
                # Calculate summary statistics
                statistics = {}
                for column in df.select_dtypes(include=np.number).columns:
                    column_stats = {
                        'mean': df[column].mean(),
                        'median': df[column].median(),
                        'mode': df[column].mode().tolist()
                    }
                    statistics[column] = column_stats
                
                # Add to response data
                response_data[data.id] = statistics
            
            return Response({"data": response_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)