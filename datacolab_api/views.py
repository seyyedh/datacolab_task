from rest_framework.response import Response
from rest_framework.views import APIView
import json
import csv

class CompaniesAPI(APIView):
    def get(self,request):
        json_file = '/home/seyyedh/workspace/django/datacolab_task/data.json'
        with open(json_file, 'r') as j:
            data = json.loads(j.read())
        return Response(data=data)

class CompanyDetailAPI(APIView):
    def get(seld, request,comp_id):
        json_file = '/home/seyyedh/workspace/django/datacolab_task/data1.csv'
        with open(json_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        rows = rows[comp_id]
        return Response(data={'name': rows[0],
                        'environment': rows[1],
                        'social':rows[2],
                        'governance':rows[3],
                        'rating':rows[4]})
