from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


from django import forms
# Create your views here.

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            login(request, form.user)
            # url = request.urlparams[0]
            return HttpResponse('''
                <script>
                    window.location.href = '/'
                </script>
            ''')

    template_vars = {
        'form': form,
    }

    return render(request, 'account/login.html', template_vars)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('Your username or password is incorrect')
        self.user = user
        return self.cleaned_data
