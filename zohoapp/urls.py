from django.urls import path,include,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from .views import EmailAttachementView

urlpatterns = [
    
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('forgotpassword' , views.forgotpassword,name='forgotpassword'),  
    path('setnewpassword' , views.setnewpassword,name='setnewpassword'),   

    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('sample/',views.sample,name="sample"),
    path('view_vendor_list/',views.view_vendor_list,name='view_vendor_list'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('sendmail/<int:pk>',views.sendmail,name='sendmail'),
    path('edit_vendor/<int:pk>',views.edit_vendor,name='edit_vendor'),
    path('edit_vendor_details/<int:pk>',views.edit_vendor_details,name='edit_vendor_details'),
    path('upload_document/<int:pk>',views.upload_document,name='upload_document'),
    path('download_doc/<int:pk>',views.download_doc,name='download_doc'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('retainer_invoices/',views.retainer_invoice,name='retainer_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('create_invoice_draft/',views.create_invoice_draft,name='create_invoice_draft'),
    path('create_invoice_send/',views.create_invoice_send,name='create_invoice_send'),
    path('view_invoice/<int:pk>',views.invoice_view,name='invoice_view'),
    path('retainer_template/<int:pk>',views.retainer_template,name='retainer_template'),
    path('retainer_invoice_edit/<int:pk>',views.retainer_edit_page,name='retainer_edit_page'), 
    path('retainer_invoice_update/<int:pk>',views.retainer_update,name='retainer_update'),
    path('send_mail/<int:pk>',views.mail_send,name='mail_send'),
    path('retaineritem_delete/<int:pk>',views.retaineritem_delete,name='retaineritem_delete'),
    path('retainer_delete/<int:pk>',views.retainer_delete,name='retainer_delete'),
    path('allestimates',views.allestimates,name='allestimates'),
    path('newestimate/',views.newestimate,name='newestimate'),
    path('createestimate/',views.createestimate,name='createestimate'),
    path('itemdata_est/',views.itemdata_est,name='itemdata_est'),
    path('create_and_send_estimate/',views.create_and_send_estimate,name='create_and_send_estimate'),
    path('estimateslip/<int:est_id>',views.estimateslip,name='estimateslip'),
    path('editestimate/<int:est_id>',views.editestimate,name='editestimate'),
    path('updateestimate/<int:pk>',views.updateestimate,name='updateestimate'),
    path('converttoinvoice/<int:est_id>',views.converttoinvoice,name='converttoinvoice'),
    path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    path('add_customer_for_estimate/',views.add_customer_for_estimate,name='add_customer_for_estimate'),
    path('entr_custmr_for_estimate/',views.entr_custmr_for_estimate,name='entr_custmr_for_estimate'),
    path('payment_term_for_estimate/',views.payment_term_for_estimate,name='payment_term_for_estimate'),
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    # path('edited/<int:id>',views.edited,name='edited'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('deleteestimate/<int:est_id>',views.deleteestimate,name='deleteestimate'),
    path('additem_est',views.additem_est,name='additem_est'),
    path('additem_page_est',views.additem_page_est,name='additem_page_est'),
    path('add_unit_est',views.add_unit_est,name='add_unit_est'),
    path('add_sales_est',views.add_sales_est,name='add_sales_est'),
    path('add_account_est',views.add_account_est,name='add_account_est'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
    path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice'),
    path('addprice',views.addprice,name='addprice'),
    path('addpl',views.addpl,name='addpl'),
    path('viewpricelist',views.viewpricelist,name='viewpricelist'),
    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('editlist/<int:id>',views.editlist,name='editlist'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('active_status/<int:id>',views.active_status,name='active_status'),
    path('createpl',views.createpl,name='createpl'),
    path('banking_home',views.banking_home,name='banking_home'),
    path('create_banking',views.create_banking,name='create_banking'),
    path('save_banking',views.save_banking,name='save_banking'),
    path('view_bank/<int:id>',views.view_bank,name='view_bank'),
    path('banking_edit/<int:id>',views.banking_edit,name='banking_edit'),
    path('save_edit_bnk/<int:id>',views.save_edit_bnk,name='save_edit_bnk'),
    path('save_banking_edit/<int:id>',views.save_banking_edit,name='save_banking_edit'),
    path('save_bank',views.save_bank,name='save_bank'),
    path('banking_delete/<int:id>',views.banking_delete,name='banking_delete'),

    ####challan
    path('create_delivery_chellan',views.create_delivery_chellan,name='create_delivery_chellan'),
    path('delivery_chellan_home',views.delivery_chellan_home,name='delivery_chellan_home'),
    path('add_customer_for_challan',views.add_customer_for_challan,name='add_customer_for_challan'),
    path('entr_custmr_for_challan',views.entr_custmr_for_challan,name='entr_custmr_for_challan'),
    path('additem_page_challan',views.additem_page_challan,name='additem_page_challan'),
    path('additem_challan',views.additem_challan,name='additem_challan'), 
    path('delivery_challan_view/<int:id>',views.delivery_challan_view,name='delivery_challan_view'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)