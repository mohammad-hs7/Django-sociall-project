from django import forms
from . models import Post

class PostCreatedForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # created = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control'}))

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', )
