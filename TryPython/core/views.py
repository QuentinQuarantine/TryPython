# coding: utf-8

import json
from StringIO import StringIO
from django.core.management import call_command
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse


class IndexView(TemplateView):
    template_name = "main.html"


class EvalResponseView(View):

    def post(self, request):
        to_eval = request.POST.get("toEval")

        namespace = request.session.get('namespace', "{}")

        out = StringIO()
        call_command("eval", to_eval, namespace, stdout=out)
        out, namespace, err = out.getvalue().split("}##{")

        request.session['namespace'] = namespace
        return JsonResponse({'out':  out, 'err': err})
