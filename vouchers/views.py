"""" Views.py is simply a Python function that takes a web request and returns a web response. Here the response is the
HTML contents of a Web page or a success message. We use view to create web pages, and associate a view to a URL to see
it as a web page.

To call the landing page of the voucher application we have defined the function index which is associated with
index.html web page.

In this view , if the requests is GET, we directly publish the index.html page to the user.
If the requests is POST, we validate the form. If the form is valid, we save the form and also increment the voucher
redemption count.

Finally, if the voucher redemption count has exceeded 3, we throw an error that maximum limit for the voucher code is
reached.

"""

from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse

from vouchers.forms import VoucherDataForm
from vouchers.models import VoucherCode, VoucherCodeCount

import logging

logging.basicConfig(level=logging.INFO, filename="execution.log", format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

CODEDICT = {}


def index(request):
    args = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = VoucherDataForm(request.POST)
        # check whether it's valid.
        if form.is_valid():
            logging.info("Voucher data form is valid.")
            # Get the voucher code detail.
            voucherCode = form.cleaned_data.get('voucherCode')
            # Get all the instances for the relevant vouher code
            voucherCodeObject = VoucherCode.objects.get(voucherCode=voucherCode)
            # Create an instance of VoucherCodeCount for this particular voucher code.
            voucherCodeCountForm = VoucherCodeCount(codeCount=voucherCodeObject)
            # Get the voucher redemption count for the particular voucher code.
            voucherRedemptionCount = VoucherCodeCount.objects.filter(codeCount_id=voucherCode)
            if len(voucherRedemptionCount) == 3:
                messages.error(request, "Error! You have exceeded the maximum redemption(3) of the Voucher Code.")
            else:
                voucherCodeCountForm.save()
                messages.success(request, 'The Discount was applied successfully')
                logging.info("Saving the valid form into the dataase.")
                form.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VoucherDataForm()
    args['form'] = form
    return render(request, 'index.html', args)


def getVoucherCode(request):
    """ 'getVoucherCode' function is called during an ajax call while the user is populating the voucher code.

    This function returns the list of all the voucher code in the database.

    Args:
        request : Web Request.
    Returns:
        codeDict (Dictionary) : Returns Voucher Code with its discount value.
    """
    voucherCode = VoucherCode.objects.all()
    logging.info("List of vouchers in the database are {}".format(voucherCode))
    logging.info("Web Request is {}".format(request))
    global CODEDICT
    for code in voucherCode:
        voucherCode = code.voucherCode
        discount = code.discount
        CODEDICT.update({voucherCode: discount})
    logging.info("Code dictionary containing the voucher code and discount details is {}".format(CODEDICT))
    return JsonResponse(CODEDICT)
