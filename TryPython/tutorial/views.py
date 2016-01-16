from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from models import Step


class StepView(View):

    def post(self, request):
        step_number = request.POST.get('step')
        step = get_object_or_404(Step, pk=int(step_number))
        return JsonResponse(step.to_dict())
