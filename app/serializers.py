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
        

#         {
#     "number_gtd":272772,
#     "reference_gtd":121,
#     "date_recorded":16,
#     "customs_mode":"IM 40",
#     "sender":"Shanhay LLC",
#     "reciever":"Hasanboy savdo MCHJ",
#     "country":"Xitoy",
#     "custom_price":0,
#     "factor_price":123,
#     "quantity":1,
#     "status":"Finished"
# }