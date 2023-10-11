from django.shortcuts import render
import re
import requests
import datetime

# Create your views here.


def index(request):
    latitude = 0
    longitude = 0
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

    appid = '0db8b81e1f8b489f5b675cefc6e3ed27'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMETERS = {'lat': latitude, 'lon': longitude, 'appid': appid}
    r = requests.get(url=URL, params=PARAMETERS)
    res = r.json()
    description = res['weather'][0]['description']
    temperature = res['main']['temp']
    feels_like = res['main']['feels_like']
    day = datetime.date.today()
    return render(request, 'index.html', {'description': description,
                                          'temperature': temperature, 'feels_like': feels_like, 'day': day, 'title': 'weather'})
