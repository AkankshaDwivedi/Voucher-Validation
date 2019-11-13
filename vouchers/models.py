""" In Django, the model is the object that is mapped to the database.
When we create a model, Django create a corresponding table in the database.

So here in models.py file for 'vouchers' application we are creating two tables, i.e 'VoucherCode' and
'VoucherCodeCount'.

'VoucherCode' table had two fields 'voucherCode' and 'discount' which is accessible by the admin for saving the voucher
code with the discount value.

In order to put a check on the number of times the code is redeemed we are using 'VoucherCodeCount' table which has a
mapping to the 'VoucherCode' table and gets updated with every use of the voucher code , with maximum redemption limit
being 3.
"""

from django.db import models


class VoucherCode(models.Model):
    """Table for saving voucher code and the corresponding discount into the database."""
    voucherCode = models.CharField(max_length=200, primary_key=True)
    discount = models.CharField(max_length=200)


class VoucherCodeCount(models.Model):
    """Table to map the voucher code with the number of times it is redeemed."""
    codeCount = models.ForeignKey(VoucherCode, on_delete=models.CASCADE)
