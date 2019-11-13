"""" Forms.py is where the django documentation recommends you place all your forms code; to keep your code easily
maintainable. Also, since its a convention mentioned in the documentation, it helps when you are collaborating with
others because that is where others will expect to look for your code dealing with forms.

The clean() method is responsible for running validate(). If, at any time, its raise ValidationError, the validation
stops and that error is raised. This method returns the clean data, which is then inserted into the cleaned_data
dictionary of the form.
"""

from django import forms

from vouchers.models import VoucherCode
import vouchers.views as views

import logging

logging.basicConfig(level=logging.INFO, filename="execution.log", format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class VoucherDataForm(forms.ModelForm):
        class Meta:
            model = VoucherCode
            fields = '__all__'

        def clean(self):
            """ 'Clean' method validates the form, at any time, its raise ValidationError, the validation stops and
            that error is raised. This method returns the clean data, which is then inserted into the cleaned_data
            dictionary of the form."""

            logging.info("Executing clean method for form validation.")
            cleaned_data = self.cleaned_data
            voucherCode = self.cleaned_data.get('voucherCode')
            discount = self.cleaned_data.get('discount')
            # Voucher and discount as received from the user.
            userCodeDict = {voucherCode: discount}

            viewsCodeDict = views.CODEDICT
            dbDiscount = 0
            if voucherCode in viewsCodeDict:
                dbDiscount = viewsCodeDict[voucherCode]
            # Voucher and discount as received from the database.
            dbCodeDict = {voucherCode: dbDiscount}

            if userCodeDict != dbCodeDict:
                raise forms.ValidationError("The voucher code and the discount value do not match.")

            if (voucherCode == '') or (discount is None):
                raise forms.ValidationError("Both voucher code and discount details are required for submitting the "
                                            "form.")

            logging.info("Clean data after form validation is {}".format(cleaned_data))
            return cleaned_data
