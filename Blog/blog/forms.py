from django import forms
from .models import Blog, Blog_Post

class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text': ''}
        #We're importing the Topic model defined in the models file, using it as a template, and telling this that the only field we want from Topics is the text field. Not the date_added.
        #Then we want this text key in the label dictionary to not have a value paired with it

class Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #Here we are telling Django to expand the number of columns in the text box to 80. Instead of the default 40