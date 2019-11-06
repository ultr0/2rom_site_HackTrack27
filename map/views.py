from django.shortcuts import render

# Create your views here.
from django.views import generic

from map.forms import AddAnswer


class MainVew(generic.TemplateView):
    template_name = 'map/index.html'
    form = AddAnswer

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # prj_in_progress = Project.objects.filter(editor_profile=request.user, admin_approve=False)
        # prj_done = Project.objects.filter(editor_profile=request.user, admin_approve=True)
        # context['projects_all'] = len(prj_in_progress)
        # context['projects_done'] = len(prj_done)
        context['graz'] = None
        context['form'] = self.form(
        #     initial={
        #     'username':request.user.username,
        #     'email':request.user.email,
        #     'first_name':request.user.first_name,
        #     'last_name':request.user.last_name,
        #     'last_login':request.user.last_login,
        #     'date_joined':request.user.date_joined,
        # }
        )

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.group = request.user
            f.map = request.user
            print('s')

        # user = User.objects.get(id=request.user.id)
        # user.last_name = form.data['last_name']
        # user.email = form.data['email']
        # user.first_name = form.data['first_name']
        # # user.username = form.cleaned_data['username']
        # user.save()
        return self.get(request, *args, **kwargs)