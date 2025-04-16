from django_filters.rest_framework import FilterSet
from .models import Hotel, Room

class HotelFilter(FilterSet):
    class Meta :
        model = Hotel
        fields = {
            'city_name' : ['exact']
    }
class RoomFilter(FilterSet):
    class Meta :
        model = Room
        fields = {
            'room_price': ['gt','lt']
    }