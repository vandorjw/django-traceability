from django.views import generic
from traceability.models.employee import Employee


class EmployeeDetail(generic.DetailView):
    template_name = 'traceability/employee/employee_detail.html'
    model = Employee


class EmployeeList(generic.ListView):
    template_name = 'traceability/employee/employee_list.html'
    model = Employee
    paginate_by = 25


class EmployeeCreate(generic.CreateView):
    template_name = 'traceability/employee/employee_form.html'
    model = Employee


class EmployeeUpdate(generic.UpdateView):
    template_name = 'traceability/employee/employee_form.html'
    model = Employee
