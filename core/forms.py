from django import forms
from .models import Assignment, Exam, AssignmentSubmission, ExamSubmission


# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'marks', 'startdate','enddate']

    def __init__(self, *args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Tên bài tập"
        self.fields['content'].label = "Nội dung"
        self.fields['marks'].label = "Điểm tối đa"
        self.fields['startdate'].label = "Ngày giao"
        self.fields['enddate'].label = "Ngày nộp"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Nhập tên bài',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Nội dung',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Điểm tối đa',
            }
        )

    def is_valid(self):
        valid = super(AssignmentCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# EXAM CREATE FORM
class ExamCreateForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'content', 'marks', 'duration']

    def __init__(self, *args, **kwargs):
        super(ExamCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Tên đề bài"
        self.fields['content'].label = "Nội dung"
        self.fields['marks'].label = "Điểm tối đa"
        self.fields['duration'].label = "Thời gian làm bài"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Nhập tên',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Nội dung',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Điểm tối đa',
            }
        )

    def is_valid(self):
        valid = super(ExamCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(ExamCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# ASSIGNMENT SUBMISSION FORM

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['name', 'assignment', 'content', 'file','marks']

    def __init__(self, *args, **kwargs):
        super(AssignmentSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = " Tên học sinh"
        self.fields['assignment'].label = "Bài tập"
        self.fields['content'].label = "Câu trả lời"
        self.fields['file'].label = "Tệp đính kèm"
        self.fields['marks'].label = "Điểm"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Điền họ tên',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Điền câu trả lời',
            }
        )

        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Tệp đính kèm',
            }
        )

    def is_valid(self):
        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course

# EXAM SUBMISSION FORM
class ExamSubmissionForm(forms.ModelForm):
    class Meta:
        model = ExamSubmission
        fields = ['name', 'exam', 'content', 'file','marks']

    def __init__(self, *args, **kwargs):
        super(ExamSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = " Tên học sinh"
        self.fields['exam'].label = "Đề thi"
        self.fields['content'].label = "Câu trả lời"
        self.fields['file'].label = "Tệp đính kèm"
        self.fields['marks'].label = "Điểm"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Điền họ tên',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Viết câu trả lời',
            }
        )

        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Tệp đính kèm',
            }
        )

    def is_valid(self):
        valid = super(ExamSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(ExamSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course