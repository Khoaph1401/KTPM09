from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User


# STUDENT REGISTRATION FORM
class StudentRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Họ Tên"
        self.fields['password1'].label = "Mật khẩu"
        self.fields['password2'].label = "Xác nhận mật khẩu"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Nhập Họ Tên',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
              'placeholder': 'Nhập Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Nhập mật khẩu',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Xác nhận mật khẩu',
            }
        )

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
        error_messages = {
            'name': {
                'required': 'Yêu cầu Họ Tên',
                'max_length': ' Họ Tên quá dài',
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "student"
        if commit:
            user.save()
        return user


# INSTRUCTOR REGISTRATION FORM
class InstructorRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(InstructorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Họ Tên"
        self.fields['password1'].label = "Mật khẩu"
        self.fields['password2'].label = "Xác nhận mật khẩu"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Nhập Họ Tên',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
              'placeholder': 'Nhập Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Nhập mật khẩu',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Xác nhận mật khẩu',
            }
        )

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
        error_messages = {
            'name': {
                'required': 'Yêu cầu Họ Tên',
                'max_length': ' Họ Tên quá dài'
            },
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "instructor"
        if commit:
            user.save()
        return user


# LOGIN FORM FOR BOTH USER
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Nhập Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Nhập mật khẩu'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("Người dùng không tồn tại")
            if not self.user.check_password(password):
                raise forms.ValidationError("Mật khẩu sai.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


# STUDENT PROFILE UPDATE FORM
class StudentProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['Họ Tên'].widget.attrs.update(
            {
                'placeholder': 'Nhập Họ Tên',
            }
        )

    class Meta:
        model = User
        fields = ["name"]


# INSTRUCTOR PROFILE UPDATE FORM
class InstructorProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InstructorProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Nhập Họ Tên',
            }
        )
    class Meta:
        model = User
        fields = ["name"]