from django.conf.urls import url
from . import views

transaction_urls = [
    url(r'^transaction_document$',views.TransactionList.as_view()),
    url(r'^transaction_line_items$',views.TransactionLineItemsList.as_view()),
    url(r'^inventory_line_items$',views.InventoryLineItemsCreate.as_view()),
    url(r'^delete_transaction/(?P<unique_id>[0-9]+)/',views.DeleteTransaction.as_view()),
    url(r'^transaction/(?P<unique_id>[0-9]+)/',views.TransactionDetails.as_view()),
]
