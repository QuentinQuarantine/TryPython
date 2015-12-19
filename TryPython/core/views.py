# coding: utf-8

from StringIO import StringIO
from django.core.management import call_command
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse


class IndexView(TemplateView):
    template_name = "main.html"


class EvalResponseView(View):

    def post(self, request):
        to_eval = request.POST.get("toEval")
        try:
            out = StringIO()
            call_command("eval", to_eval, stdout=out)
            out, err = out.getvalue().split("}##{")
            return JsonResponse({'out':  out, 'err': err})
        except Exception as err:
            return HttpResponse(status=500, reason=str(err))
