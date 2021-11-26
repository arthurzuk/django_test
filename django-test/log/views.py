from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .utils import queryset_to_workbook
from .models import Login

@csrf_exempt
def index(request):
        try:
            data = Login.objects.all()
            columns = ('id', 'username', 'password', 'born_date')
            output = queryset_to_workbook(data, columns)
            response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=logs.xlsx'
            output.close()
            return response
        except AttributeError:
                return HttpResponse('Não há dados no servidor')
        except:
                return HttpResponse(e)
