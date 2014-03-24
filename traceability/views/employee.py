from django.views import generic
from traceability.models.employee import Employee


class EmployeeDetail(generic.DetailView):
    model = Employee


class EmployeeList(generic.ListView):
    model = Employee
    paginate_by = 25


class EmployeeCreate(generic.CreateView):
    model = Employee


class EmployeeUpdate(generic.UpdateView):
    model = Employee
