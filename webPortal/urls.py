from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quote/first', views.quote_first, name='quote_first'),
    path('quote/second', views.quote_second, name='quote_second'),
    path('quote/final', views.quote_final, name='quote_final'),
    path('approver/search', views.aprv_search, name='aprv_search'),
    path('quote/verify/<str:quote_id>', views.quote_verify, name='quote_verify'),
    path('quote/verify', views.quote_verify_submit, name='quote_verify_submit'),
    path('quote/list', views.quote_list, name='quote_list'),
    path('quote/<str:quote_id>', views.quote_querry, name='quote_qry')

]
