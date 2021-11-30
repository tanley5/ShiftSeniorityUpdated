from django.urls import path

from .views import ResponseThanksView
from .utilities.custom_url_views import urlpatterns as custom_url_patterns

urlpatterns = [
    # path('response_collection', ResponseCollectionView.as_view(),
    #      name='response_collection'),
    path('response_thanks', ResponseThanksView.as_view(), name='response_thanks'),
] + custom_url_patterns
