from django import forms
from blogapp.models import Register
from blogapp.models import Post

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'