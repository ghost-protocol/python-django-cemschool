from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Student, Parent, Medical
from .forms import StudentForm, ParentForm, MedicalForm

####begin:students
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def save_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            students = Student.objects.all()
            data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
                'students': students
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
    else:
        form = StudentForm()
    return save_student_form(request, form, 'students/includes/partial_student_create.html')

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    else:
        form = StudentForm(instance=student)
    return save_student_form(request, form, 'students/includes/partial_student_update.html')

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        student.delete()
        data['form_is_valid'] = True
        students = Student.objects.all()
        data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
            'students': students
        })
    else:
        context = {'student': student}
        data['html_form'] = render_to_string('students/includes/partial_student_delete.html', context, request=request)
    return JsonResponse(data)
####end:students

####begin:parents
@login_required
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'parents/parent_list.html', {'parents': parents})

@login_required
def save_parent_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            parents = Parent.objects.all()
            data['html_parent_list'] = render_to_string('parents/includes/partial_parent_list.html', {
                'parents': parents
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
    else:
        form = ParentForm()
    return save_parent_form(request, form, 'parents/includes/partial_parent_create.html')

@login_required
def parent_update(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
    else:
        form = ParentForm(instance=parent)
    return save_parent_form(request, form, 'parents/includes/partial_parent_update.html')

@login_required
def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    data = dict()
    if request.method == 'POST':
        parent.delete()
        data['form_is_valid'] = True
        parents = Parent.objects.all()
        data['html_parent_list'] = render_to_string('parents/includes/partial_parent_list.html', {
            'parents': parents
        })
    else:
        context = {'parent': parent}
        data['html_form'] = render_to_string('parents/includes/partial_parent_delete.html', context, request=request)
    return JsonResponse(data)

####end:parents

####begin:medicals
@login_required
def medical_list(request):
    medicals = Medical.objects.all()
    return render(request, 'medicals/medical_list.html', {'medicals': medicals})

@login_required
def save_medical_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            medicals = Medical.objects.all()
            data['html_medical_list'] = render_to_string('medicals/includes/partial_medical_list.html', {
                'medicals': medicals
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def medical_create(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
    else:
        form = MedicalForm()
    return save_medical_form(request, form, 'medicals/includes/partial_medical_create.html')

@login_required
def medical_update(request, pk):
    medical = get_object_or_404(Medical, pk=pk)
    if request.method == 'POST':
        form = MedicalForm(request.POST, instance=medical)
    else:
        form = MedicalForm(instance=medical)
    return save_medical_form(request, form, 'medicals/includes/partial_medical_update.html')

@login_required
def medical_delete(request, pk):
    medical = get_object_or_404(Medical, pk=pk)
    data = dict()
    if request.method == 'POST':
        medical.delete()
        data['form_is_valid'] = True
        medicals = Medical.objects.all()
        data['html_medical_list'] = render_to_string('medicals/includes/partial_medical_list.html', {
            'medicals': medicals
        })
    else:
        context = {'medical': medical}
        data['html_form'] = render_to_string('medicals/includes/partial_medical_delete.html', context, request=request)
    return JsonResponse(data)

####end:medicals