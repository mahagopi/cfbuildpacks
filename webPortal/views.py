from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage

from .models import Quotation, Approver
from .forms import QuoteForm, QuoteForm_first, QuoteForm_second

from .devlog import Dlog

import json
from django.core import serializers

# Create your views here.

def index(request):
    return HttpResponse("|..|")

def quote_list(request):
    print(request.user)
    q = Quotation.objects.filter(requestor_name=request.user)
    #print(q.form_id)
    return render(request, 'quote_list.html', {'frm_flds' : q})

def quote_querry(request, quote_id):
    print("quote_id : ", quote_id)
    q = Quotation.objects.filter(form_id=quote_id).first()
    #print(q.form_id)
    return render(request, 'quote_query.html', {'frm_flds' : q})

def quote_first(request):
    print("|.Q.u.o.t.e.F.i.r.s.t.|")

    q = Quotation()
    q.form_status = "Initiated"
    if request.method == 'POST':
        Dlog.resp(request)
        print(q)
        print(q.id)
        form1 = QuoteForm_first(request.POST)
        if form1.is_valid():
            print("\n!!!!!!!!!!!!!!!!!!!!")
            print(form1)
            my_quote = form1.save(commit=False)
            #my_quote.user = request.user # Set the user object here
            my_quote.save()
        else:
            print("\n################")  
    print(request.user)
    return render(request, 'quote_first.html', {'frm_flds' : q})

def quote_second(request):
    print("|.Q.u.o.t.e.S.e.c.o.n.d.|")

    q = Quotation()
    q.form_status = "Initiated"
    if request.method == 'POST':
        Dlog.resp(request)
        form1 = QuoteForm_first(request.POST)
        if form1.is_valid():
            print("\n!!!!!!!!!!!!!!!!!!!!")
            print(form1)
            my_quote = form1.save(commit=False)
            #my_quote.user = request.user # Set the user object here
        else:
            print("\n################")
        return render(request, 'quote_second.html', {'frm_flds' : my_quote})
    return render(request, 'quote_second.html', {'frm_flds' : q})

def quote_final(request):
    print("|.Q.u.o.t.e.T.h.i.r.d.|")

    q = Quotation()
    q.form_status = "Initiated"
    if request.method == 'POST':
        Dlog.resp(request)
        form1 = QuoteForm_second(request.POST)
        if form1.is_valid():
            print("\nSUCCESS!!!!!!!!finalll!!!!!!!!!!")
            print(form1)
            my_quote = form1.save(commit=False)
            my_quote.form_status  = "Submitted"
            my_quote.trm_cond = request.POST['trm_cond']
            my_quote.save()
            uxlr = "http://localhost:8000/portal/quote/verify/" + str(q.id)
            email = EmailMessage('IBM Quote', uxlr, to=['gauravsinghgs08@gmail.com'])
            email.send()
        else:
            print("\nCHUD GAYEEEEEEEEEEEEEEEE ################")
        return render(request, 'quote_final.html', {'frm_flds' : my_quote})
    return render(request, 'quote_final.html', {'frm_flds' : q})

def aprv_search(request):
    # if request.method == 'GET':
    app_name =  request.GET.get('search') 
    status = Approver.objects.filter(usr_name__contains=r'{0}'.format(app_name))[:10]
    data = serializers.serialize('json', status)
    return HttpResponse(data, content_type="application/json")
    # else:
    #     return HttpResponse("Try /GET")

def quote_verify(request, quote_id):
    q = Quotation.objects.filter(form_id=quote_id).first()
    return render(request, 'quote_verify.html', {'frm_flds' : q})

def quote_verify_submit(request):
    quote_id = request.POST['form_id']
    if request.method == 'POST':
        q = Quotation.objects.filter(form_id=quote_id).first()
        print("Change Statutsssssssssssssssssssssss2")
        q.form_status  = "Confirmed"
        q.save()
    return render(request, 'quote_verify_confirm.html', {'frm_flds' : q})
