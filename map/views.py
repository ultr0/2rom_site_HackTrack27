from django.shortcuts import render

# Create your views here.
from django.views import generic

from map.forms import AddAnswer
from map.models import Answer, Map


class MainVew(generic.TemplateView):
    template_name = 'map/index.html'
    error = None
    graz = None
    form = AddAnswer

    def get(self,request, error=None, graz=None, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        correct  = Answer.objects.filter(correct=True, group=request.user).last()
        map = Map.objects.get(id=(correct.map.id+1))

        context['graz'] = graz
        context['error'] = error
        context['map'] = map
        context['form'] = self.form(initial={'map': map,})

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.group = request.user
            map = Map.objects.filter(id=answer.map.id).first()
            if map:
                if answer.answer == map.passcode:
                    self.graz = 'True'
                    answer.correct = True
                else:
                    answer.correct = False
                    self.error = 'False'
                answer.save(form.cleaned_data)
            else:
                self.error = 'False'

        return self.get(request, error=self.error, graz=self.graz, *args, **kwargs)