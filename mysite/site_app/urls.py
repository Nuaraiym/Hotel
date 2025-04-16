from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()

router.register(r'users', ProfileViewSet, basename='user_list'),
router.register(r'city', CityViewSet, basename='city_list'),
router.register(r'review', ReviewViewSet, basename='review_list'),
router.register(r'rating', RatingViewSet, basename='rating_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('booking/', BookingListAPIView.as_view(), name='booking_list'),
    path('booking/<int:pk>/', BookingDetailAPIView.as_view(), name='booking_detail'),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
]
