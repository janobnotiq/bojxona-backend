from rest_framework import serializers
from .models import Declaration


class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = [
            "number_gtd",
            "reference_gtd",
            "date_recorded",
            "customs_mode",
            "sender",
            "reciever",
            "country",
            "custom_price",
            "factor_price",
            "quantity",
            "status"
            ]