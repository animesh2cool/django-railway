from django import forms
import datetime

class userForms(forms.Form):
    num1=forms.CharField(label="value 1",required=False,widget=forms.Textarea(attrs={'class': 'form-control'}))
    num2=forms.CharField(label="value 2",required=True)
    email=forms.EmailField()
    day=forms.DateField(initial=datetime.date.today)