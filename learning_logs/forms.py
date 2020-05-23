from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Simple form to accept data from users."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """A form to accept the Entry instances of a particular Topic."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


