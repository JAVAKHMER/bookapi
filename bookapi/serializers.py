
from rest_framework.serializers import HyperlinkedModelSerializer
from bookapi.models import Books
class BookSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model=Books
        fields=("id","title","isbn","language")
        