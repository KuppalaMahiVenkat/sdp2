from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('login', views.login),
    path('signup', views.signup),
    path('aboutus', views.aboutus),
    path('service', views.service),
    path('post', views.createpost),
    path('sign', views.signup2),
    path('log', views.login1),
    path('invalid', views.invalid),
    path('exist', views.exist),
    path('access',views.access),
    path('logout',views.logout),
    path('banking',views.banking),
    path('personalbanking', views.personalbanking),
    path('personal', views.personal2),
    path('transaction', views.transaction),
    path('view1',views.viewtrans),
    path('mobilebanking',views.mobilebanking),
    path('electricitybill',views.electricalbill),
    path('mobilerecharge',views.mobilerecharge),
    path('eb',views.electricbill),
    path('mb',views.mobilebill2),
    path('finance',views.finance),
    path('loan',views.loanapplication1),
    path('insurance', views.insurance),
    path('loan1',views.loan),
    path('plans', views.plans),
    path('ins', views.ins2),
]