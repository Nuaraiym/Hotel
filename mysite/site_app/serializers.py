from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'created_date', 'phone_number', 'role_status','country_user']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name','city_image']

class CityDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name','city_image']


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HotelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_images','hotel_name','country','address']

class HotelDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name','country','address','owner','hotel_description','hotel_stars','country',
                  'city_name','address','created_date','hotel_video']


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'

class RoomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel_room','room_number']

class RoomDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel_room','room_number','room_status','room_type','room_price','room_description',]

class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'

class  BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Booking
        fields = '__all__'

class BookingListSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Booking
        fields = ['id','client']

class BookingDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Booking
        fields = ['client','hotel_room']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



