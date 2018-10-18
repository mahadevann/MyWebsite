from django import forms
import numpy as np
from .ProcessFile import ProcessFile

class NameForm(forms.Form):
    # formname = "displaychoices"
    image_src = '/static/images/home.jpg'

    dyear = np.arange(1980, 2017, 1)
    f = {}
    for yr in dyear:
        f[yr] = yr
    Ytup = f.items()
    pf = ProcessFile()
    df = pf.createDataframe("countycodes.csv")
    df.index = df['Code']

    cdict = {}
    county = df['County'].unique()
    type(county)
    for c in county:
        cdict[c] = c
    Ctup = cdict.items()

    twp = {}
    code = df['Muni']

    for c in np.arange(len(code)):
        twp[str(df.index[c]) + ':' + df.iat[c, 2]] = df.iat[c, 0]

    Ttup = twp.items()


    County = forms.ChoiceField(choices=Ctup, label='County', widget = forms.Select(attrs = {
            'onChange' : "dothis();" ,}))
    Township = forms.ChoiceField(choices=Ttup, label='Township')
    Year_From = forms.ChoiceField(choices=Ytup, label='From Year')
    #Year_To = forms.ChoiceField(choices=Ytup)

    # Last_name = forms.CharField(label='Last name', max_length=100)



    def yeardropdown(self):
        dyear = np.arange(1980, 2017, 1)
        f = {}
        for yr in dyear:
            f[yr] = yr
        tup = f.items()
        return tup


class FileForm(forms.Form):
    image_src = "/static/images/home.jpg"
    formname = "uploadfile"
    file = forms.FileField()


class MailForm(forms.Form):
    mailsent = ''
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    sender = forms.EmailField(label='', widget= forms.TextInput(attrs={'placeholder': 'email'}))
    subject = forms.CharField(max_length=100,label='',widget= forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='',widget= forms.Textarea(attrs={'placeholder': 'Message','rows':'5'}))
