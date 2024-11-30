from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, ServiceRequest
from .forms import ServiceRequestForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UpdateServiceRequestStatusSerializer
from datetime import datetime
from django.contrib.auth.models import User

def create_customer_view(request):
    user = request.user 
    if not Customer.objects.filter(user=user).exists():
        Customer.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            phone='1234567890', 
            address='123 Test St', 
        )
        return render(request, 'success.html', {'message': 'Customer created successfully!'})
    else:
        return render(request, 'error.html', {'message': 'Customer already exists!'})


def homepage_view(request):
    return render(request, 'homepage.html') 


class UpdateServiceRequestStatusView(APIView):
    def patch(self, request, pk):
        try:
            service_request = ServiceRequest.objects.get(pk=pk)
        except ServiceRequest.DoesNotExist:
            return Response({"error": "Service request not found."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the data
        serializer = UpdateServiceRequestStatusSerializer(service_request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def service_request_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            customer, created = Customer.create_customer(
                name=name,
                email=email,
                phone=phone,
                address=address
            )

            service_request.customer = customer
            service_request.name = name 
            service_request.email = email
            service_request.save()

            return redirect('track_requests')
    else:
        form = ServiceRequestForm()

    return render(request, 'service_requests.html', {'form': form})


def track_requests_view(request):
    email = request.GET.get('email')
    service_requests = None

    if email:
        try:
            customer = Customer.objects.get(email=email)
            service_requests = ServiceRequest.objects.filter(customer=customer)
        except Customer.DoesNotExist:
            return render(request, 'track_requests.html', {
                'error': 'No customer profile found for the provided email address.'
            })

    return render(request, 'track_requests.html', {'requests': service_requests})