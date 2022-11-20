from django.contrib.auth import forms, views
from django.urls import reverse_lazy


class FormControlMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class AuthenticationForm(FormControlMixin, forms.AuthenticationForm):
    pass


class PasswordChangeForm(FormControlMixin, forms.PasswordChangeForm):
    pass


class PasswordResetForm(FormControlMixin, forms.PasswordResetForm):
    pass


class SetPasswordForm(FormControlMixin, forms.SetPasswordForm):
    pass


class LoginView(views.LoginView):
    form_class = AuthenticationForm
    template_name = 'djaccount/views/forms/login.djhtml'


class LogoutView(views.LogoutView):
    template_name = 'djaccount/views/logout.djhtml'


class PasswordChangeView(views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'djaccount/views/forms/password_change.djhtml'
    success_url = reverse_lazy('djaccount:password_change_done')


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'djaccount/views/password_change_done.djhtml'


class PasswordResetView(views.PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'djaccount/views/forms/password_reset.djhtml'
    email_template_name = 'djaccount/emails/password_reset_email.txt'
    subject_template_name = 'djaccount/emails/password_reset_subject.txt'
    success_url = reverse_lazy('djaccount:password_reset_done')


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'djaccount/views/password_reset_done.djhtml'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'djaccount/views/forms/password_reset_confirm.djhtml'
    success_url = reverse_lazy('djaccount:password_reset_complete')


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'djaccount/views/password_reset_complete.djhtml'
