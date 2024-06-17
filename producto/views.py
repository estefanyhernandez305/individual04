from django.http import HttpResponse
from django.views.generic.base import View

class ProductoView(View):
    def get(self,request):
        return HttpResponse(content='Producto View - Ready!!!')
