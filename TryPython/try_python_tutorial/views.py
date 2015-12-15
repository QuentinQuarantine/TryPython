# coding: utf-8

import json
from StringIO import StringIO
from django.core.management import call_command
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = "main.html"


class EvalResponseView(View):

    def post(self, request):
        to_eval = json.loads(self.request.body.decode('utf-8'))['toEval']
        try:
            out = StringIO()
            call_command("evalcommand", to_eval, stdout=out)
            out, err = out.getvalue().split("}##{")
            return JsonResponse({'out':  out, 'err': err})
        except subprocess.CalledProcessError as err:
            raise err
