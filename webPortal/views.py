from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage

from .models import Quotation

# Create your views here.

def index(request):
    return HttpResponse("|..|")

def quote_list(request):
    print(request.user)
    q = Quotation.objects.filter(requestor_name=request.user)
    #print(q.form_id)
    return render(request, 'quote_list.html', {'frm_flds' : q})

def quote_confirm(request, quote_id):
    print("confirmmmmm ;",quote_id)
    q = Quotation.objects.filter(id=quote_id).first()
    print(q.form_id)
    if request.method == 'POST':
        q = Quotation.objects.filter(form_id=quote_id).first()
        print("Change Statutsssssssssssssssssssssss")
        q.form_status  = "Confirmed"
        q.save()
    return render(request, 'quote_confrm.html', {'frm_quote' : q})

def quote_ssconfirm(request):
    print("Quote confirmmmmmmm")
    print(request.POST['form-id'])
    if request.method == 'POST':
        q = Quotation.objects.filter(id=request.POST['form-id']).first()
        print(q.form_id)
        print("Change Statutsssssssssssssssssssssss")
        q.form_status  = "Confirmed"
        q.save()
    return render(request, 'quote_save.html', {'frm_quote' : q})

def quote_save(request):
    if request.method == 'POST':
        print(request.POST['form-id'])
        q = Quotation.objects.filter(id=request.POST['form-id']).first()
        print(q.form_id)
        q.trm_cond = request.POST['tnconds']
        q.save()
        print("t & C savedddddddddd")
        uxlr = "http://localhost:8000/portal/quote/" + str(q.id)
        email = EmailMessage('IBM Quote', uxlr, to=['gauravsinghgs08@gmail.com'])
        email.send()
    q = Quotation.objects.filter(id=request.POST['form-id']).first()
    return render(request, 'quote_save.html', {'frm_quote' : q})

def quote_querry(request, quote_id):
    print("quote_id : ", quote_id)
    q = Quotation.objects.filter(form_id=quote_id).first()
    #print(q.form_id)
    return render(request, 'quote_id.html', {'frm_flds' : q})

def quote(request):
    #return HttpResponse("|.Q.u.o.t.e.|")

    q = Quotation()
    q.form_status = "Initiated"
    if request.method == 'POST':
        print(request)
        print(request.user)
        print(request.POST['form-id'])
        print(request.POST['form-status'])
        print(request.POST['requestor-name'])
        print(request.POST['requestor-email'])
        print(request.POST['submission-date'])
        print(request.POST['valid-upto'])
        print(request.POST['sales-connect'])
        print(request.POST['form-rfs'])


        print(request.POST['form-acc-name'])
        print(request.POST['form-cstmr-id'])
        print(request.POST['form-sales-id'])
        print(request.POST['form-aprv-name'])

        print(request.POST['rsk-rating'])
        print(request.POST['rsk-region'])
        print(request.POST['rsk-custom'])


        print(request.POST.get('ws-firewall-yes', False))
        print(request.POST.get('ws-firewall-no', False)) 
        print(request.POST.get('ws-hostips-yes', False))
        print(request.POST.get('ws-hostips-no', False))
        print(request.POST.get('ws-dacfte-yes', False))
        print(request.POST.get('ws-dacfte-no', False))

        print(request.POST.get('coe-endpoint', False))
        print(request.POST.get('coe-das', False)) 
        print(request.POST.get('coe-infra', False))
        print(request.POST.get('coe-iam', False))
        print(request.POST.get('coe-sioc', False))
        print(request.POST.get('eps-malware', False)) 
        print(request.POST.get('eps-websec', False))
        print(request.POST.get('eps-emailsec', False))
        print(request.POST.get('eps-vulmgmnt', False))
        print(request.POST.get('eps-dlp', False))

        print(request.POST['esc-bs'])
        print(request.POST['esc-bfte'])
        print(request.POST['esc-b7'])
        print(request.POST['esc-tfte'])
        print(request.POST['esc-b77'])
        print(request.POST['esc-ttfte'])

        print(request.POST['malware-winopn'])
        print(request.POST['malware-srvcscp'])
        
        print(request.POST['servers-vendor'])
        print(request.POST['servers-antimware'])
        print(request.POST['servers-noconsole'])

        print(q)
        print(q.id)

       
    print(request.user)
    return render(request, 'quote.html', {'frm_flds' : q})

def quote_prvw(request):
    #return HttpResponse("|.Q.u.o.t.e.|")
    if request.method == 'POST':
        q = Quotation()
        print(request)
        print(request.user)
        
        print(request.POST['form-id'])
        print(request.POST['form-status'])
        print(request.POST['requestor-name'])
        print(request.POST['requestor-email'])
        print(request.POST['submission-date'])
        print(request.POST['valid-upto'])
        print(request.POST['sales-connect'])
        print(request.POST['form-rfs'])


        print(request.POST['form-acc-name'])
        print(request.POST['form-cstmr-id'])
        print(request.POST['form-sales-id'])
        print(request.POST['form-aprv-name'])

        print(request.POST['rsk-rating'])
        print(request.POST['rsk-region'])
        print(request.POST['rsk-custom'])


        print(request.POST.get('ws-firewall-yes', False))
        print(request.POST.get('ws-firewall-no', False)) 
        print(request.POST.get('ws-hostips-yes', False))
        print(request.POST.get('ws-hostips-no', False))
        print(request.POST.get('ws-dacfte-yes', False))
        print(request.POST.get('ws-dacfte-no', False))

        print(request.POST.get('coe-endpoint', False))
        print(request.POST.get('coe-das', False)) 
        print(request.POST.get('coe-infra', False))
        print(request.POST.get('coe-iam', False))
        print(request.POST.get('coe-sioc', False))
        print(request.POST.get('eps-malware', False)) 
        print(request.POST.get('eps-websec', False))
        print(request.POST.get('eps-emailsec', False))
        print(request.POST.get('eps-vulmgmnt', False))
        print(request.POST.get('eps-dlp', False))

        print(request.POST['esc-bs'])
        print(request.POST['esc-bfte'])
        print(request.POST['esc-b7'])
        print(request.POST['esc-tfte'])
        print(request.POST['esc-b77'])
        print(request.POST['esc-ttfte'])

        print(request.POST['malware-winopn'])
        print(request.POST['malware-srvcscp'])
        
        print(request.POST['servers-vendor'])
        print(request.POST['servers-antimware'])
        print(request.POST['servers-noconsole'])

        q.form_id = request.POST['form-id']
        q.form_status = request.POST['form-status']
        q.requestor_name = request.POST['requestor-name']
        q.requestor_email = request.POST['requestor-email']
        q.submission_date = request.POST['submission-date']
        q.valid_upto = request.POST['valid-upto']
        q.sales_connect = request.POST['sales-connect']
        q.form_rfs = request.POST['form-rfs']

        q.form_acc_name = request.POST['form-acc-name']
        q.form_cstmr_id = request.POST['form-cstmr-id']
        q.form_sales_id = request.POST['form-sales-id']
        q.form_aprv_name = request.POST['form-aprv-name']
        
        q.rsk_rating = request.POST['rsk-rating']
        q.rsk_region = request.POST['rsk-region']
        q.rsk_custom = request.POST['rsk-custom']

        q.ws_firewall_yes = request.POST.get('ws-firewall-yes', False)
        q.ws_firewall_no = request.POST.get('ws-firewall-no', False)
        q.ws_hostips_yes = request.POST.get('ws-hostips-yes', False)
        q.ws_hostips_no = request.POST.get('ws-hostips-no', False)
        q.ws_dacfte_yes = request.POST.get('ws-dacfte-yes', False)
        q.ws_dacfte_no = request.POST.get('ws-dacfte-no', False)

        q.coe_endpoint = request.POST.get('coe-endpoint', False)
        q.coe_das = request.POST.get('coe-das', False)
        q.coe_infra = request.POST.get('coe-infra', False)
        q.coe_iam = request.POST.get('coe-iam', False)
        q.coe_sioc = request.POST.get('coe-sioc', False)
        q.eps_malware = request.POST.get('eps-malware', False)
        q.eps_websec = request.POST.get('eps-websec', False)
        q.eps_emailsec = request.POST.get('eps-emailsec', False)
        q.eps_vulmgmnt = request.POST.get('eps-vulmgmnt', False)
        q.eps_dlp = request.POST.get('eps-dlp', False)

        if len(request.POST['esc-bs']) > 1:
            q.esc_bs = float( request.POST['esc-bs'])
        else:
            q.esc_bs = float(0)
        if len(request.POST['esc-bfte']) > 1:
            q.esc_bfte = float( request.POST['esc-bfte'])
        else:
            q.esc_bfte = float(0)
        if len(request.POST['esc-b7']) > 1:
            q.esc_b7 = float( request.POST['esc-b7'])
        else:
            q.esc_b7 = float(0)
        if len(request.POST['esc-tfte']) > 1:
            q.esc_tfte = float( request.POST['esc-tfte'])
        else:
            q.esc_tfte = float(0)
        if len(request.POST['esc-b77']) > 1:
            q.esc_b77 = float( request.POST['esc-b77'])
        else:
            q.esc_b77 = float(0)
        if len(request.POST['esc-ttfte']) > 1:
            q.esc_ttfte = float( request.POST['esc-ttfte'])
        else:
            q.esc_ttfte = float(0)

        q.malware_winopn = request.POST['malware-winopn']
        q.malware_srvcscp = request.POST['malware-srvcscp']
        q.servers_vendor = request.POST['servers-vendor']
        q.servers_antimware = request.POST['servers-antimware']
        q.servers_noconsole = request.POST['servers-noconsole']
        q.save()
        print("FORM SAVEDDDDDDDDDD")

    q = Quotation.objects.filter(form_id=request.POST['form-id']).first()
    return render(request, 'quote_prvw.html',{'frm_quote': q})

def chk_quote(request):
    #return HttpResponse("|.Q.u.o.t.e.|")

    q = Quotation()
    
    if request.method == 'POST':
        print(request)
        print(request.user)
        print(request.POST['form-id'])
        print(request.POST['form-status'])
        print(request.POST['requestor-name'])
        print(request.POST['requestor-email'])
        print(request.POST['submission-date'])
        print(request.POST['valid-upto'])
        print(request.POST['sales-connect'])
        print(request.POST['form-rfs'])


        print(request.POST['form-acc-name'])
        print(request.POST['form-cstmr-id'])
        print(request.POST['form-sales-id'])
        print(request.POST['form-aprv-name'])

        print(request.POST['rsk-rating'])
        print(request.POST['rsk-region'])
        print(request.POST['rsk-custom'])


        print(request.POST.get('ws-firewall-yes', False))
        print(request.POST.get('ws-firewall-no', False)) 
        print(request.POST.get('ws-hostips-yes', False))
        print(request.POST.get('ws-hostips-no', False))
        print(request.POST.get('ws-dacfte-yes', False))
        print(request.POST.get('ws-dacfte-no', False))

        print(request.POST.get('coe-endpoint', False))
        print(request.POST.get('coe-das', False)) 
        print(request.POST.get('coe-infra', False))
        print(request.POST.get('coe-iam', False))
        print(request.POST.get('coe-sioc', False))
        print(request.POST.get('eps-malware', False)) 
        print(request.POST.get('eps-websec', False))
        print(request.POST.get('eps-emailsec', False))
        print(request.POST.get('eps-vulmgmnt', False))
        print(request.POST.get('eps-dlp', False))

        print(request.POST['esc-bs'])
        print(request.POST['esc-bfte'])
        print(request.POST['esc-b7'])
        print(request.POST['esc-tfte'])
        print(request.POST['esc-b77'])
        print(request.POST['esc-ttfte'])

        print(request.POST['malware-winopn'])
        print(request.POST['malware-srvcscp'])
        
        print(request.POST['servers-vendor'])
        print(request.POST['servers-antimware'])
        print(request.POST['servers-noconsole'])

        print(q)
        print(q.id)

    return render(request, 'login.html',{'frm_q': q})