import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Login

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            content = request.POST
            u = content['username']
            b = content['born_date']
            if 'password' in content.keys():
                p = content['password']
                login = Login(username = u, password = p, born_date = b)
                login.save()
                return HttpResponse('Login sucessfully created')
            
            login = Login(username = u, born_date = b)
            login.save()
            return HttpResponse('Login sucessfully created')
            
            
        except Exception as e:
            return HttpResponse(e)
    return HttpResponse('Invalid request method')
