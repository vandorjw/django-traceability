from django.http import HttpResponseRedirect
from django.views import generic
from traceability.models.batch import Batch, Input
from traceability.models.item import Item
from traceability.forms.batch import InputFormSet, BatchCreate, BatchUpdate


class BatchDetail(generic.DetailView):
    template_name = 'traceability/batch/batch_detail.html'
    model = Batch


class BatchList(generic.ListView):
    template_name = 'traceability/batch/batch_list.html'
    model = Batch
    paginate_by = 25


class BatchUpdate(generic.UpdateView):
    template_name = 'traceability/batch/batch_form.html'
    model = Batch
    form_class = BatchUpdate


class BatchCreate(generic.CreateView):
    template_name = 'traceability/batch/batch_create.html'
    model = Batch
    form_class = BatchCreate

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        input_form = InputFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, input_form=input_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        input_form = InputFormSet(self.request.POST)
        if (form.is_valid() and input_form.is_valid()):
            return self.form_valid(form, input_form)
        else:
            return self.form_invalid(form, input_form)

    def form_valid(self, form, input_form):
        self.object = form.save()
        input_form.instance = self.object
        input_form.save()
        #  Mass Create Item objects
        start_s = form.cleaned_data['start_serial']
        end_s = form.cleaned_data['end_serial']
        slist = list(range(start_s, end_s+1))
        data = [Item(item_id=s, batch=self.object) for s in slist]
        Item.objects.bulk_create(data)
        return HttpResponseRedirect(self.object.get_absolute_url)

    def form_invalid(self, form, input_form):
        return self.render_to_response(
            self.get_context_data(form=form, input_form=input_form))
