from django.urls import path

from .views import ResponseCollectionView, ResponseThanksView

urlpatterns = [
    path('response_collection', ResponseCollectionView.as_view(),
         name='response_collection'),
    path('response_thanks', ResponseThanksView.as_view(), name='response_thanks'),
]
