# Voucher-Validation

## Description : This is a demo application built uisng Django. 

## Functionality Covered: 
(1) Created a html page with a form with field `Voucher Code` for user to enter the voucher code and get the discount value.
(2) The form will validate the voucher code from the database details and update the user if the voucher code is valid or not.
(3) It will then show the amount of discount user is getting as per the voucher he/she has selceted.
(4) Each voucher code can be used 3 times only. Error is thrown to the user metioning that the maximun redemption for the code is done.
(5) Create an apps call `vouchers
(6) Designed and created model for Voucher and Vouchercount(To keep a track of how many times the code is redeemed).
(7) Created Django admin `http://localhost/site-admin/` to setup voucher data and discount detail.

## Configuration : Please set up the settings.py file as per the user requirement.

### How to run Once the app starts, go to the web browser and visit http://localhost:8000/index/

(1) python manage.py createsuperuser:
Create an admin login to set the data for the voucher code and discount value.
Username: admin
Login to `http://localhost/site-admin/ to set the data.
 
(2) python manage.py makemigrations vouchers: 
Whenever you make a change to a model, even if it is updating the description on a field. Run this command so that all the changes are taken into account.Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

(3) python manage.py migrate: 
Run this command to apply the changes to your data.

(4) python manage.py runserver: 
Start the server, login using admin and populate the voucher code details and access http://localhost:8000/index/ to validtae the steps covered in functionality covered.

