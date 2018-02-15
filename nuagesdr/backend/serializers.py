from rest_framework import serializers
from backend.models import RiskTypesModel, FieldTypesModel, EnumFieldTypesModel

class EnumFieldTypesSerializer (serializers.ModelSerializer):
    class Meta:
        model = EnumFieldTypesModel
        fields = ('enum_value',)
                
                
class FieldTypesSerializer (serializers.ModelSerializer):
    enum_value = EnumFieldTypesSerializer(many=True)

    class Meta:
        model = FieldTypesModel
        fields = ('field_name', 'field_type', 'enum_value')


class RiskTypesSerializer (serializers.ModelSerializer):
    # field_info = serializers.StringRelatedField(many=True)

    field_info = FieldTypesSerializer(many=True)

    class Meta:
        model = RiskTypesModel
        fields = ('risk_type_name', 'field_info')
 
        ## '__all__' 
        ##('risk_type_name')
        ## , 'field_types')


