from django.http import HttpResponseRedirect
from django.views import generic
from traceability.models.incident import Incident
from traceability.forms.incident import UpdateFormSet, IncidentUpdate


class IncidentDetail(generic.DetailView):
    model = Incident
    template_name = 'traceability/incident/incident_detail.html'


class IncidentAffected(generic.DetailView):
    model = Incident
    template_name = 'traceability/incident/incident_affected.html'


class IncidentList(generic.ListView):
    template_name = 'traceability/incident/incident_list.html'
    model = Incident
    paginate_by = 25


class IncidentCreate(generic.CreateView):
    template_name = 'traceability/incident/incident_form.html'
    model = Incident


class IncidentUpdate(generic.UpdateView):
    template_name = 'traceability/incident/incident_update.html'
    model = Incident
    form_class = IncidentUpdate

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        update_form = UpdateFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, update_form=update_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        update_form = UpdateFormSet(self.request.POST)
        if (form.is_valid() and update_form.is_valid()):
            return self.form_valid(form, update_form)
        else:
            return self.form_invalid(form, update_form)

    def form_valid(self, form, update_form):
        self.object = form.save()
        update_form.instance = self.object
        update_form.save()
        return HttpResponseRedirect(self.object.get_absolute_url())

    def form_invalid(self, form, update_form):
        return self.render_to_response(
            self.get_context_data(form=form, update_form=update_form))
