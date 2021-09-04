from django.db import models
import uuid
from datetime import date

# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)


class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)


class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)


class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)

# Create your models here.
class Transacton(models.Model):
    status = [
        (1, 'PENDING'),
        (2, 'COMPLETED'),
        (3, "CLOSE")
    ]
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4,primary_key=True)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchMaster,on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentMaster,on_delete=models.CASCADE)
    transaction_number = models.CharField(max_length=100,unique=True)
    transaction_status = models.PositiveSmallIntegerField(choices=status)
    remarks = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if self.transaction_number:
            datet = date.today().year
            count = Transacton.objects.all().count()+1
            count + 1
            year = Transacton.objects.all().last()
            if year:
                yearcheck = year.transaction_number.split("/")
                if yearcheck != datet:
                    count = Transacton.objects.all().count() + 1
                    count + 1
            trn_format = "{}/{}/{}".format(self.transaction_number,count,datet)
            self.transaction_number = trn_format
        super(Transacton, self).save(*args, **kwargs)

class TransactionLineItem(models.Model):
    units = [
        (1, 'KG'),
        (2, 'METRE')
    ]
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    transaction_id = models.ForeignKey(Transacton, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    required_on_date = models.DateTimeField()
    quantity = models.DecimalField(max_digits=100,decimal_places=2)
    rate_per_unit = models.PositiveIntegerField()
    unit = models.PositiveSmallIntegerField(choices=units)

class InventoryItem(models.Model):
    units = [
        (1, 'KG'),
        (2, 'METRE')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    linr_item_id = models.ForeignKey(TransactionLineItem, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    gross_quantity = models.DecimalField(max_digits=100,decimal_places=2)
    net_quantity = models.DecimalField(max_digits=100,decimal_places=2)
    unit = models.PositiveSmallIntegerField(choices=units)