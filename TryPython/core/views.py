# coding: utf-8

import json
import six
from six import StringIO

from django.core.management import call_command
from django.views.generic import TemplateView, View
from django.http import JsonResponse

if six.PY2:
    import ast_utils
else:
    from . import ast_utils


class IndexView(TemplateView):
    template_name = "main.html"


class EvalView(View):

    def post(self, request):
        to_eval = request.POST.get("toEval")
        default_namespace_value = json.dumps({'functions': []})
        namespace = json.loads(request.session.get('namespace', default_namespace_value))
        out = StringIO()
        if ast_utils.isFunction(to_eval):
            namespace['functions'].append(to_eval)
            call_command("eval", '', json.dumps(namespace), stdout=out)
        else:
            call_command("eval", to_eval, json.dumps(namespace), stdout=out)
        values = json.loads(out.getvalue())
        out, namespace = values['out'], values['namespace']
        err = values['error']
        request.session['namespace'] = namespace
        return JsonResponse({'out': out, 'err': err})
