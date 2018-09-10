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

    ws_firewall_yes = models.BooleanField(default=False)
    ws_firewall_no = models.BooleanField(default=False)
    ws_hostips_yes = models.BooleanField(default=False)
    ws_hostips_no = models.BooleanField(default=False)
    ws_dacfte_yes = models.BooleanField(default=False)
    ws_dacfte_no = models.BooleanField(default=False)

    coe_endpoint = models.BooleanField(default=False)
    coe_das = models.BooleanField(default=False)
    coe_infra = models.BooleanField(default=False)
    coe_iam = models.BooleanField(default=False)
    coe_sioc = models.BooleanField(default=False)
    eps_malware = models.BooleanField(default=False)
    eps_websec = models.BooleanField(default=False)
    eps_emailsec = models.BooleanField(default=False)
    eps_vulmgmnt = models.BooleanField(default=False)
    eps_dlp = models.BooleanField(default=False)

    esc_bs = models.FloatField(default=0.0)
    esc_bfte = models.FloatField(default=0.0)
    esc_b7 = models.FloatField(default=0.0)
    esc_tfte = models.FloatField(default=0.0)
    esc_b77 = models.FloatField(default=0.0)
    esc_ttfte = models.FloatField(default=0.0)

    malware_winopn = models.CharField(max_length=200)
    malware_srvcscp = models.CharField(max_length=200)
    
    servers_vendor = models.CharField(max_length=200)
    servers_antimware = models.CharField(max_length=200)
    servers_noconsole = models.CharField(max_length=200)
  
    trm_cond = models.CharField(max_length=1000)

class UserQuote(models.Model):
    frm_id = models.UUIDField()
    usr_email = models.CharField(max_length=200)
    frm_stts = models.CharField(max_length=200)
   
class Approver(models.Model):
    usr_email = models.CharField(max_length=200)
    usr_name = models.CharField(max_length=200)
class userRole(models.Model):
    usr_email = models.CharField(max_length=200)
    usr_name = models.CharField(max_length=200)
    usr_role = models.CharField(max_length=200)
   