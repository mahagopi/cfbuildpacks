from django import forms
from .models import Quotation

import uuid

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotation
        #fields = ['form_id','servers_noconsole']
        fields = ['form_id','form_status','requestor_name','requestor_email','submission_date','valid_upto','sales_connect','form_rfs','form_acc_name','form_cstmr_id','form_sales_id','form_aprv_name','rsk_rating','rsk_region','rsk_custom','ws_firewall_yes','ws_firewall_no','ws_hostips_yes','ws_hostips_no','ws_dacfte_yes','ws_dacfte_no','coe_endpoint','coe_das','coe_infra','coe_iam','coe_sioc','eps_malware','eps_websec','eps_emailsec','eps_vulmgmnt','eps_dlp','esc_bs','esc_bfte','esc_b7','esc_tfte','esc_b77','esc_ttfte','malware_winopn','malware_srvcscp','servers_vendor','servers_antimware','servers_noconsole','trm_cond']

class QuoteForm_first(forms.ModelForm):

    class Meta:
        model = Quotation
        #fields = ['form_id','servers_noconsole']
        fields = ['coe_endpoint', 'coe_das','coe_infra','coe_iam','coe_sioc','form_id','form_status','requestor_name','requestor_email','submission_date','valid_upto','sales_connect','form_rfs','form_acc_name','form_cstmr_id','form_sales_id','form_aprv_name','rsk_rating','rsk_region','rsk_custom']

    
        def __init__(self, *args):
            
            self.fields['coe_endpoint'].initial  = False
            self.fields['coe_das'].initial  = False
            self.fields['coe_infra'].initial  = False
            self.fields['coe_iam'].initial  = False
            self.fields['coe_sioc'].initial  = False

class QuoteForm_second(forms.ModelForm):

    class Meta:
        model = Quotation
        #fields = ['form_id','servers_noconsole']
        fields = ['coe_endpoint', 'coe_das','coe_infra','coe_iam','coe_sioc','form_id','form_status','requestor_name','requestor_email','submission_date','valid_upto','sales_connect','form_rfs','form_acc_name','form_cstmr_id','form_sales_id','form_aprv_name','rsk_rating','rsk_region','rsk_custom','servers_vendor','servers_antimware','servers_noconsole','malware_winopn','malware_srvcscp', 'esc_bs', 'esc_bfte','esc_b7','esc_tfte','esc_b77','esc_ttfte', 'eps_malware', 'eps_websec', 'eps_emailsec', 'eps_vulmgmnt', 'eps_dlp', 'coe_endpoint', 'coe_das','coe_infra','coe_iam','coe_sioc', 'ws_firewall_yes', 'ws_firewall_no','ws_hostips_yes', 'ws_hostips_no', 'ws_dacfte_yes', 'ws_dacfte_no']    

        def __init__(self, *args):
            
            self.fields['ws_firewall_yes'].initial  = False
            self.fields['ws_firewall_no'].initial  = False
            self.fields['ws_hostips_yes'].initial  = False
            self.fields['ws_hostips_no'].initial  = False
            self.fields['ws_dacfte_yes'].initial  = False
            self.fields['ws_dacfte_no'].initial  = False
            self.fields['coe_endpoint'].initial  = False
            self.fields['coe_das'].initial  = False
            self.fields['coe_infra'].initial  = False
            self.fields['coe_iam'].initial  = False
            self.fields['coe_sioc'].initial  = False
            self.fields['eps_malware'].initial  = False
            self.fields['eps_websec'].initial  = False
            self.fields['eps_emailsec'].initial  = False
            self.fields['eps_vulmgmnt'].initial  = False
            self.fields['eps_dlp'].initial  = False
