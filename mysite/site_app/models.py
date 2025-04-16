from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(55)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    country_user = models.CharField(max_length=32,null=True,blank=True)
    ROLE_CHOICES = (
        ('client','client'),
        ('owner','owner')
    )
    role_status = models.CharField(choices=ROLE_CHOICES,max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

class City(models.Model):
    city_name = models.CharField(max_length=35)
    city_image = models.ImageField(upload_to='city_images')

    def __str__(self):
        return f'{self.city_name},{self.city_image}'



class Hotel(models.Model):
   hotel_name = models.CharField(max_length=100,unique=True)
   owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
   hotel_year = models.DateTimeField(auto_now_add=True)
   hotel_description = models.TextField()
   hotel_stars = models.IntegerField(choices=[(i,str(i)) for i in range(1,5)],null=True,blank=True)
   country = models.CharField(max_length=50)
   city_name = models.ForeignKey(City,on_delete=models.CASCADE)
   address = models.CharField(max_length=50)
   created_date = models.DateTimeField(auto_now_add=True)
   hotel_video = models.FileField(upload_to='videos')

   def __str__(self):
         return f'{self.hotel_name} : {self.city_name} : {self.address}'


class HotelImage(models.Model):
    hotel_name = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='hotels')
    hotel_image = models.ImageField(upload_to='hotel_image')
    hotel_video = models.FileField(upload_to='hotel_video')

    def __str__(self):
           return f'{self.hotel_name} : {self.hotel_image}'


class Room(models.Model):
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField(null=True,blank=True)
    STATUS_CHOICES = (
        ('vip','vip'),
        ('стандарт','стандарт'),
        ('двухместный', 'двухместный'),
        ('семейный', 'семейный'),
    )
    room_status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    ROOM_CHOICES = (
        ('свободен','свободен'),
        ('занят','занят'),
        ('ожидание','ожидание'),
        ('бронь','бронь')
    )
    room_type = models.CharField(max_length=100,choices=ROOM_CHOICES, default='свободен')
    room_price = models.PositiveSmallIntegerField()
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotel_room} '

class RoomImage(models.Model):
    hotel_room = models.ForeignKey(Room,on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image')
    room_video = models.FileField(upload_to='room_video')

    def __str__(self):
           return f'{self.hotel_room}'

class Booking(models.Model):
    hotel_booking = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client = models.ForeignKey(Profile,on_delete=models.CASCADE)
    hotel_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    STATUS_BOOKING = (
        ('подтверждено','подтверждено'),
        ('отменено','отменено'),
        ('ожидание', 'ожидание'),
    )
    booking_status = models.CharField(max_length=20, choices=STATUS_BOOKING)

    def __str__(self):
        return f'{self.client} : {self.hotel_booking}'

class Review(models.Model):
    client = models.OneToOneField(Profile,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.client} : {self.hotel}'

class Rating(models.Model):
    client = models.OneToOneField(Profile, on_delete=models.CASCADE)
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_rating = models.IntegerField(choices=[(i,str(i)) for i in range(1,10)],null=True,blank=True)

    def __str__(self):
        return f'{self.client} : {self.hotel_room} : "{self.hotel_rating}" '





