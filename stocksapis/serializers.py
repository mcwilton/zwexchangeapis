from rest_framework import serializers
from .models import Company
from rest_framework import renderers

class CompanySerializer(serializers.HyperlinkedModelSerializer):

    # name = serializers.HyperlinkedRelatedField(many=True, view_name='CompanyDetail', read_only=True)
    # name = serializers.HyperlinkedIdentityField(view_name='CompanyList', format='html')

    class Meta:
        model = Company
        fields = ['id', 'company_name', 'trading_day', 'opening', 'closing', 'volume', 'date_created']

    # diff = serializers.DecimalField(max_digits=10, decimal_places=2)   
    # diff = serializers.SerializerMethodField(method_name='calculate_diff')

    # def calculate_diff(self, opening, closing):
    #     diff = closing - opening
    #     print(diff)
    #     return diff
