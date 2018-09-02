from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quote/', views.quote, name='quote'),
    path('quote/preview', views.quote_prvw, name='quote_prvw'),
    path('save', views.quote_save, name='quote_save'),
    path('quote/list', views.quote_list, name='quote_list'),
    path('quote/confirm/<str:quote_id>', views.quote_confirm, name='quote_confirm'),
    path('confirm/', views.quote_ssconfirm, name='quote_ssconfirm'),
    path('quote/<str:quote_id>', views.quote_querry, name='quote_qry'),
    path('check/1', views.chk_quote, name='quotwe')

]
