from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import pandas as pd
import numpy as np
import os
from django.conf import settings

from .forms import NameForm,FileForm,MailForm
from .ProcessFile import ProcessFile

pf = ProcessFile()
pf.df = pf.createDataframe("Millburn1.csv")
pf.dcc = pf.createDataframe("countycodes.csv")


def login(request):
    return render(request, 'blogsite/login.html')


def index(request):
    return render(request, 'blogsite/index.html')


def contactus(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['sender'],
                ['netjac@gmail.com'],
                fail_silently=False,
            )

        email=MailForm()
        email.mailsent = 'Mail sent successfully!'
    else:
        email = MailForm()
        email.mailsent=''

    return render(request, 'blogsite/ContactUs.html', {'form': email})


def bloghome(request):
    return render(request, 'blogsite/bloghome.html')


def headerbar(request):
    return render(request, 'blogsite/HeaderBar.html')


def test(request):
    return render(request, 'blogsite/sub/test1.html')


def services(request):
    return render(request, 'blogsite/services.html')


def blogdetail(request):
    plot,count = pf.getSalesPriceCount(pf.df,'sales')

    return render(request, 'blogsite/Blogdetail.html', {'plots':plot,'counts':count})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if 'File' in request.POST:
            # create a form instance and populate it with data from the request:
            #fileinp = FileForm(request.POST, request.FILES)
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                #handle_uploaded_file(request.FILES['file'])
                #pf = ProcessFile()
                #pf.createDataframe("/static/images/myfig.png")
                #form = NameForm(getchoices(pf.dfinp),getchoices(pf.dfinp))
                form = NameForm()
                #form.full_clean()
                # NameForm.image_src = '/'+pf.plotimage
                # form.base_fields['Plot'].choices = getchoices(pf.dfinp)
                # form.base_fields['GroupBy'].choices = getchoices(pf.dfinp)
        else:
            # create form instance and populate it with data from request
            form = NameForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                tid =(form.cleaned_data['Township'].split(":")[0])
                yfrom = form.cleaned_data['Year_From']
                #yto = form.cleaned_data['Year_To']
                img = pf.boxplotbymuni(tid,yfrom)
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                # NameForm(request.POST, df)
                # return HttpResponseRedirect('/your-name/',{'form':newform})
                #pf = ProcessFile()
                #pf.createDataframe("/static/images/myfig.png")
                #plot = form.cleaned_data['Plot']
                #groupby = form.cleaned_data['Plot']
                NameForm.image_src = "/" + img
                #form=NameForm()
                return render(request, 'blogsite/diygraph.html', {'form': form})
            else:
                HttpResponseRedirect('/your-name/')
    # if a GET (or any other method) we'll create a blank form
    else:
        # NameForm.image_src = "/static/images/home.jpg"
        #form = FileForm()
        form = NameForm()

    return render(request,'blogsite/diygraph.html', {'form': form})



def handle_uploaded_file(f):
    file_path = os.path.join(settings.BASE_DIR, 'static/temp1.csv')
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def getchoices(df):
    p = {}
    dlist = np.arange(1, len(df.columns))
    clist = df.columns
    for i in range(len(clist) - 3):
        p[dlist[i]] = clist[i]
    t = p.items()
    return t