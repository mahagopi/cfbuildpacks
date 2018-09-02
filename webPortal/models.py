from django.db import models
import uuid

# Create your models here.
class Quotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    form_id = models.CharField(max_length=200)
    form_status = models.CharField(max_length=200)
    requestor_name = models.CharField(max_length=200)
    requestor_email = models.CharField(max_length=200)
    submission_date = models.DateField()
    valid_upto = models.DateField()
    sales_connect = models.CharField(max_length=200)
    form_rfs = models.CharField(max_length=200)

    form_acc_name = models.CharField(max_length=200)
    form_cstmr_id = models.CharField(max_length=200)
    form_sales_id = models.CharField(max_length=200)
    form_aprv_name = models.CharField(max_length=200)

    rsk_rating = models.CharField(max_length=200)
    rsk_region = models.CharField(max_length=200)
    rsk_custom = models.CharField(max_length=200)

    ws_firewall_yes = models.CharField(max_length=200)
    ws_firewall_no = models.CharField(max_length=200)
    ws_hostips_yes = models.CharField(max_length=200)
    ws_hostips_no = models.CharField(max_length=200)
    ws_dacfte_yes = models.CharField(max_length=200)
    ws_dacfte_no = models.CharField(max_length=200)

    coe_endpoint = models.CharField(max_length=200)
    coe_das = models.CharField(max_length=200)
    coe_infra = models.CharField(max_length=200)
    coe_iam = models.CharField(max_length=200)
    coe_sioc = models.CharField(max_length=200)
    eps_malware = models.CharField(max_length=200)
    eps_websec = models.CharField(max_length=200)
    eps_emailsec = models.CharField(max_length=200)
    eps_vulmgmnt = models.CharField(max_length=200)
    eps_dlp = models.CharField(max_length=200)

    esc_bs = models.FloatField(default=None)
    esc_bfte = models.FloatField(default=None)
    esc_b7 = models.FloatField(default=None)
    esc_tfte = models.FloatField(default=None)
    esc_b77 = models.FloatField(default=None)
    esc_ttfte = models.FloatField(default=None)

    malware_winopn = models.CharField(max_length=200)
    malware_srvcscp = models.CharField(max_length=200)
    
    servers_vendor = models.CharField(max_length=200)
    servers_antimware = models.CharField(max_length=200)
    servers_noconsole = models.CharField(max_length=200)
  
    trm_cond = models.CharField(max_length=200)

class UserQuote(models.Model):
    frm_id = models.UUIDField()
    usr_email = models.CharField(max_length=200)
    frm_stts = models.CharField(max_length=200)
   