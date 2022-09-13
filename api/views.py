# from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
 
from api.models import showemp
import graphlib
from unittest import result
import numpy as np
#import matplotlib.pyplot as plt
import pyodbc 

#from unittest import result

def showempnames(request):
    results = showemp.objects.all()
    return render(request, "dropdown.html", {"showemp":results})

class HomeView(View):
    def HomeView(self, request, *args, **kwargs):
	    return render(request, 'index.html')


####################################################

## if you don't want to user rest_framework

# def get_data(request, *args, **kwargs):
#
# data ={
#			 "sales" : 100,
#			 "person": 10000,
#	 }
#
# return JsonResponse(data) # http response


#######################################################

## using rest_framework classes

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def charts1(self, request, format = None):
            cnxn = pyodbc.connect(driver = "ODBC Driver 17 for SQL Server",
                        host = "10.1.1.47",
                        database ="unofinance_report",
                        uid = "uno",
                        pwd= "swift",
                        port = "1433")


            cursor = cnxn.cursor()
            cursor.execute("select top 7 ZONEGRPUNIT,Sum(Amount) [Amount] from sampletable where Isnull(ZONEGRPUNIT,'') <> '' group by ZONEGRPUNIT")
            ##cursor.execute("select top 7 ZONEGRPUNIT from sampletable where Isnull(ZONEGRPUNIT,'') <> '' group by ZONEGRPUNIT")

                    # Fecthing Data From mysql to my python progame
                    
            result = cursor.fetchall
                    
            labels = []
            chartdata = []
                    
            for i in cursor:
                labels.append(i[0])
                chartdata.append(i[1])
                        
            print("ZONE GROUP UNITS = ", labels)
            print(" chartdata = ", chartdata)
                    # Visulizing Data using Matplotlib
            '''
            labels = [
                        'January',
                        'February',
                        'March',
                        'April',
                        'May',
                        'June',
                        'July'
                        ]
            '''
            chartLabel = "my data"
            #chartdata = [0, 10, 5, 2, 20, 30, 45]
            data = {
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
            return Response(data)
