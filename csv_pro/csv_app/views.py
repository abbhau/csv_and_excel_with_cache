from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
import csv
from django.http import JsonResponse
import openpyxl


class CsvView(APIView):

    def get(self, request, country):
        with open('static//ASH.csv', encoding= 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            country = country
            li = []
            s = set()
            di = {}
            for rec in reader:
                li.append(rec['country'])
                s.add(rec['country'])

                if rec['country'] not in di:
                    di[rec['country']] = int(rec['numberrange'])
                else:
                    di[rec['country']] = di[rec['country']] + int(rec['numberrange'])
            
            count_city = {}
            for i in s:
                if i == country :
                    count_city[country] = li.count(country) 
            
            numberrange_city = {}
            for k,v in di.items():
                if k == country :
                    numberrange_city[k] = v
            
        return JsonResponse({"Count_city":count_city, "nuberrange_city":numberrange_city})


class ExcelView(APIView):
    def get(self, request):
        file_path = 'static//Project-Management-Sample-Data.xlsx'
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        headers = []
        rows = []
        for obj_index, obj  in enumerate(ws.iter_rows(values_only=True)):
            if obj_index == 5:
                headers.append(list(obj))
            if obj_index >5:
                rows.append(list(obj))
        headers[0].pop(0)
        for i in rows:
            i.pop(0)
        
        obj_list = []
        
        for i in rows:
            obj_list.append(dict(zip(headers[0],i)))
        
        return JsonResponse({"excel":obj_list})


            
