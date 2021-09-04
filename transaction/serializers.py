from rest_framework import serializers
from .models import *
import json


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacton
        fields = "__all__"

class TransactionLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLineItem
        fields = "__all__"

class InventoryLineItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = "__all__"

class TransactionDetailsSerializer(serializers.ModelSerializer):
    linr_item_id = TransactionLineItemSerializer()
    transcation_details = serializers.SerializerMethodField()
    class Meta:
        model = InventoryItem
        fields = "__all__"

    def get_transcation_details(self,obj):
        transaction_obj = Transacton.objects.filter(unique_id=obj.linr_item_id.transaction_id.unique_id).values()
        return transaction_obj