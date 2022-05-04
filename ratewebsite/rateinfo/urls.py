from django.urls import path
from rateinfo.views import (
    RestaurantList,
    RestaurantDetail,
    RestaurantCreate,
    RestaurantUpdate,
    RestaurantDelete,
    HolderList,
    HolderDetail,
    HolderCreate,
    HolderUpdate,
    HolderDelete,
    TypeList,
    TypeDetail,
    TypeCreate,
    PlaceList,
    PlaceDetail,
    PlaceCreate,
    PlaceUpdate,
    PlaceDelete,
    CustomerList,
    CustomerDetail,
    CustomerCreate,
    CustomerDelete,
    CustomerUpdate, TypeUpdate, TypeDelete, CommentList, CommentDetail, CommentCreate, CommentUpdate, CommentDelete,
    SectionList, SectionDetail, SectionCreate, SectionUpdate, SectionDelete,
    signup,
)
# from .views import SignUpView

urlpatterns = [
    path('signup/',
         signup,
         name='signup_urlpattern',
         ),
    path('restaurant/',
         RestaurantList.as_view(),
         name='rateinfo_restaurant_list_urlpattern'),
    path('restaurant/<int:pk>',
         RestaurantDetail.as_view(),
         name='rateinfo_restaurant_detail_urlpattern'),
    path('restaurant/create',
         RestaurantCreate.as_view(),
         name='rateinfo_restaurant_create_urlpattern'),
    path('restaurant/update/<int:pk>',
         RestaurantUpdate.as_view(),
         name='rateinfo_restaurant_update_urlpattern'),
    path('restaurant/delete/<int:pk>',
         RestaurantDelete.as_view(),
         name='rateinfo_restaurant_delete_urlpattern'),
    path('holder/',
         HolderList.as_view(),
         name='rateinfo_holder_list_urlpattern'),
    path('holder/create',
         HolderCreate.as_view(),
         name='rateinfo_holder_create_urlpattern'),
    path('holder/<int:pk>',
         HolderDetail.as_view(),
         name='rateinfo_holder_detail_urlpattern'),
    path('holder/update/<int:pk>',
         HolderUpdate.as_view(),
         name='rateinfo_holder_update_urlpattern'),
    path('holder/delete/<int:pk>',
         HolderDelete.as_view(),
         name='rateinfo_holder_delete_urlpattern'),
    path('type/',
         TypeList.as_view(),
         name='rateinfo_type_list_urlpattern'),
    path('type/<int:pk>',
         TypeDetail.as_view(),
         name='rateinfo_type_detail_urlpattern'),
    path('type/create',
         TypeCreate.as_view(),
         name='rateinfo_type_create_urlpattern'),
    path('type/update/<int:pk>',
         TypeUpdate.as_view(),
         name='rateinfo_type_update_urlpattern'),
    path('type/delete/<int:pk>',
         TypeDelete.as_view(),
         name='rateinfo_type_delete_urlpattern'),
    path('place/',
         PlaceList.as_view(),
         name='rateinfo_place_list_urlpattern'),
    path('place/<int:pk>',
         PlaceDetail.as_view(),
         name='rateinfo_place_detail_urlpattern'),
    path('place/create',
         PlaceCreate.as_view(),
         name='rateinfo_place_create_urlpattern'),
    path('place/update/<int:pk>',
         PlaceUpdate.as_view(),
         name='rateinfo_place_update_urlpattern'),
    path('place/delete/<int:pk>',
         PlaceDelete.as_view(),
         name='rateinfo_place_delete_urlpattern'),
    path('place/<int:pk>',
         PlaceDetail.as_view(),
         name='rateinfo_place_detail_urlpattern'),
    path('customer/',
         CustomerList.as_view(),
         name='rateinfo_customer_list_urlpattern'),
    path('customer/<int:pk>',
         CustomerDetail.as_view(),
         name='rateinfo_customer_detail_urlpattern'),
    path('customer/create',
         CustomerCreate.as_view(),
         name='rateinfo_customer_create_urlpattern'),
    path('customer/update/<int:pk>',
         CustomerUpdate.as_view(),
         name='rateinfo_customer_update_urlpattern'),
    path('customer/delete/<int:pk>',
         CustomerDelete.as_view(),
         name='rateinfo_customer_delete_urlpattern'),
    path('comment/',
         CommentList.as_view(),
         name='rateinfo_comment_list_urlpattern'),
    path('comment/<int:pk>',
         CommentDetail.as_view(),
         name='rateinfo_comment_detail_urlpattern'),
    path('comment/create',
         CommentCreate.as_view(),
         name='rateinfo_comment_create_urlpattern'),
    path('comment/update/<int:pk>',
         CommentUpdate.as_view(),
         name='rateinfo_comment_update_urlpattern'),
    path('comment/delete/<int:pk>',
         CommentDelete.as_view(),
         name='rateinfo_comment_delete_urlpattern'),
    path('section/',
         SectionList.as_view(),
         name='rateinfo_section_list_urlpattern'),
    path('section/<int:pk>',
         SectionDetail.as_view(),
         name='rateinfo_section_detail_urlpattern'),
    path('section/create',
         SectionCreate.as_view(),
         name='rateinfo_section_create_urlpattern'),
    path('section/update/<int:pk>',
         SectionUpdate.as_view(),
         name='rateinfo_section_update_urlpattern'),
    path('section/delete/<int:pk>',
         SectionDelete.as_view(),
         name='rateinfo_section_delete_urlpattern'),
]