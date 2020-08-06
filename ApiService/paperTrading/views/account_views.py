# from  import Numberid, TickersTable
from django.http import JsonResponse

#For Rest Based Views
# Create your views here.
# https://www.django-rest-framework.org/api-guide/views/

def home():
    return JsonResponse({'hello':'world'})

