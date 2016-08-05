from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .typeform import tf_load_data
from .models import FormResponse


class Index(View):
    def get(self, request):
        context = {}
        context['test'] = "i am paradox"
        return render(request, 'postapi/index.html', context)

    def post(self, request):
        return HttpResponse("post page")


class Api(APIView):

    def get(self, request):
        return Response(request.data)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Api, self).dispatch(request, *args, **kwargs)

    def post(self, request, format=".json"):
        data = request.data
        d = tf_load_data(answers_json=data)
        status = 'ok' if d else 'error'
        response = {'status': status}
        resp = FormResponse(text=json.dumps(data))
        resp.save()
        return Response(response)
