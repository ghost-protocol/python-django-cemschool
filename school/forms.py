from django import forms
from .models import Student, Parent, Medical

class StudentForm(forms.ModelForm):

        class Meta:
                model = Student
                fields = (
                        'surname',
                        'firstname',
                        'othername',
                        'dateofbirth',
                        'hometown',
                        'date_admission'
                )

class ParentForm(forms.ModelForm):

        class Meta:
                model = Parent
                fields = (
                        'student',
                        'title',
                        'relationship',
                        'surname',
                        'firstname',
                        'othername',
                        'address',
                        'residence',
                        'occupation',
                        'education_level',
                        'children_home'
                )

class MedicalForm(forms.ModelForm):

        class Meta:
                model = Medical
                fields = (
                        'student',
                        'whooping_cough',
                        'diphteria',
                        'tetanus',
                        'measels',
                        'medical_officer_remarks',
                )