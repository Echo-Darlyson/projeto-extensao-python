from django.shortcuts import render
from django.http import HttpResponse
import pandas
import matplotlib.pyplot as plt
import os

def index(request):
    
    df = pandas.read_excel(os.path.join(os.getcwd(), "dados_areas_verdes_urbanas.xlsx"))
    table = df.to_html(classes=("table table-striped"))
    context = {"cod" : table}
    return render(request, "index.html", context)

def analise(request):
    
    option=""
    if request.method == "POST":
        if "checkbox" in request.POST:
            d = request.POST
            for key,value in d.items():
                if value == "arbo":
                    option = "arbo"
                elif value == "vgt_per":
                    option = "vgt_per"
                elif value == "vgt_con":
                    option = "vgt_con"
                elif value == "fauna":
                    option = "fauna"
                else:
                    option = "ilhas_calor"

    df = pandas.read_excel(os.path.join(os.getcwd(), "dados_areas_verdes_urbanas.xlsx"))
    table = df.to_html(classes=("table table-striped"))
    
    context = {"cod" : table, "option": option}
    return render(request, "graphics.html", context)

# Create your views here.
