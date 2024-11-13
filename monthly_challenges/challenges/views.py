from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound  , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
months = {
    "January": "New year, new beginnings.",
    "February": "Love is in the air.",
    "March": "Spring forward and blossom.",
    "April": "April showers bring May flowers.",
    "May": "Bloom where you are planted.",
    "June": "Hello, sunshine and warmth.",
    "July": "Freedom and fireworks.",
    "August": "Savor the last days of summer.",
    "September": "Back to routines and fresh starts.",
    "October": "Embrace the colors of fall.",
    "November": "Gratitude turns what we have into enough.",
    "December": "Joy to the world and holiday cheer."
}



def month_by_number(request , month_number):
    all_months=list(months.keys())
    
    if month_number > len(all_months) or month_number <= 0 :
         return HttpResponseNotFound ("Invalid Month Number")
     
    path=reverse('month_by_name' , args=[all_months[month_number-1]])
    return HttpResponseRedirect(path)


def month_by_name (request , month_name):
    try:
     month_quote =months[month_name]
    except:
        return HttpResponseNotFound ("Invalid Name")
    return HttpResponse(f"<h1>{month_quote}<h1>")
    
     
def index(request):
    months_list=""    
    for month in list(months.keys()) :
        path=reverse('month_by_name' , args=[month])
        months_list += f"<li><a href='{path}'>{month.capitalize()}</a></li>"
    
    
    respons_data = f'<ul>{months_list}</ul>'
    return HttpResponse(respons_data)
    
    
    
    