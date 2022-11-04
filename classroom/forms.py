from django import forms
from .models import Course
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'teacher_name','course_description']

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].label = "Tên lớp"
        self.fields['teacher_name'].label = "Tên giáo viên"
        self.fields['course_description'].label = "Môn học"

        self.fields['course_name'].widget.attrs.update(
            {
                'placeholder': 'Nhập tên lớp',
            }
        )

        self.fields['teacher_name'].widget.attrs.update(
            {
                'placeholder': 'Nhập tên giáo viên',
            }
        )

        self.fields['course_description'].widget.attrs.update(
            {
                'placeholder': 'Tên môn học',
            }
        )

    def is_valid(self):
        valid = super(CourseCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CourseCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course