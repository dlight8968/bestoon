from django.conf.urls import url , include
from . import views

urlpatterns = [
  url (r'^submit/expence/$' , views.submit_expence , name="submit_expence"),
  url (r'^submit/income/$' , views.submit_income , name="submit_income")

]
