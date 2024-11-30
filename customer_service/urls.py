from django.urls import path
from . import views
from .views import UpdateServiceRequestStatusView

urlpatterns = [
    path('service-requests/', views.service_request_view, name='service_requests'),
    path('track-requests/', views.track_requests_view, name='track_requests'),
    path('service-requests/<int:pk>/update-status/', UpdateServiceRequestStatusView.as_view(), name='update-service-request-status'),
]