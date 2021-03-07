from django.shortcuts import render
import requests
import json

# Create your views here.
def calculate(request):
    if request.method == 'GET':
        a = int(request.GET.get('a', '0'))
        b = int(request.GET.get('b', '0'))

        payload = {
            'a': a,
            'b': b,
        }
        headers = {
            'Content-type': 'application/json'
        }
        url = 'http://localhost:8080/calculate'
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return render(request, 'calculate.html', {'a': a, 'b': b, 'result': response.json})
        else:
            return render(request, 'calculate.html', {'a': a, 'b': b, 'result': response})


        