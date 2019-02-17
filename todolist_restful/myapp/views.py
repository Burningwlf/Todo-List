from django.forms import model_to_dict
from django.http import JsonResponse, QueryDict
from django.shortcuts import render

# Create your views here.
from django.views import View

from myapp.models import List


class ListAPI(View):

    def post(self,req):
        params = req.POST
        title = params.get("title")
        content = params.get("content")
        date = params.get("date")



        List.objects.create(
            title= title,
            content = content,
            date = date,

        )

        return JsonResponse({"msg":"ok"},status=201)


    def get(self,req):
        id = int(req.GET.get("id"))

        list = List.objects.get(pk=id)

        my_dict = model_to_dict(list)

        return JsonResponse(my_dict)


    def delete(self,req):
        params = QueryDict(req.body)
        id = int(params.get("id"))
        List.objects.get(pk=id).delete()
        return JsonResponse({"msg": "deleted"}, status=204)

    def put(self, req):
        params = QueryDict(req.body)
        id = int(params.get("id"))
        list = List.objects.get(id=id)

        list.title = params.get("title", list.title)
        list.content = params.get("content", list.content)
        list.price = params.get("date", list.date)
        list.finished = params.get('finshed',list.finished)
        list.save()

        return JsonResponse(model_to_dict(list))