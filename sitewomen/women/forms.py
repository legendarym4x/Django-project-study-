from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, ValidationError

from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not chosen', label='Categories')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Not married', required=False,
                                     label='Husband')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'photo', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Length exceeds 50 characters')


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')
