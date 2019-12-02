from django import forms
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class contactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    file = forms.FileField()
