from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

class TransactionList(ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transacton.objects.all()

class TransactionLineItemsList(ListCreateAPIView):
    serializer_class = TransactionLineItemSerializer
    queryset = TransactionLineItem.objects.all()

class InventoryLineItemsCreate(CreateAPIView):
    serializer_class = InventoryLineItemsSerializer
    queryset = InventoryItem.objects.all()

class DeleteTransaction(RetrieveUpdateDestroyAPIView):
    lookup_field = 'unique_id'
    queryset = Transacton.objects.all()
    serializer_class = TransactionSerializer

    def delete(self, request, *args, **kwargs):
        transactionobj = get_object_or_404(Transacton, unique_id=kwargs['unique_id'])
        line_items = TransactionLineItem.objects.filter(transaction_id=transactionobj.unique_id).last()
        if line_items:
            inventory_obj = InventoryItem.objects.filter(linr_item_id=transactionobj.unique_id).last()
            if inventory_obj:
                return "inventory already created you can't delete this transaction"
            transactionobj.delete()
        return Response("transcation object deleted", status=status.HTTP_204_NO_CONTENT)

class TransactionDetails(ListAPIView):
    lookup_field = 'unique_id'
    queryset = InventoryItem.objects.all()
    serializer_class = TransactionDetailsSerializer