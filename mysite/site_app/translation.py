from .models import Hotel, Room
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description','address')

@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('hotel_room', )





