# **Service Request Management System**

A Django-based web application for managing customer service requests. The system allows customers to submit service requests, track their requests, and provides an interface for administrators or representatives to manage and respond to these requests.

---

## **Features**

- **Customer Management**:
  - Customers can be linked to Django's built-in `User` model for authentication.
  - Anonymous customers can also create service requests by providing their details.

- **Service Request Submission**:
  - Users can submit service requests with details, attachments, and contact information.
  - Each service request is associated with a customer.

- **Request Tracking**:
  - Customers can track the status of their service requests using their email address.

- **Request Management**:
  - Administrators or representatives can update the status of service requests.
  - Representatives can also add responses to service requests.

- **REST API**:
  - API endpoints allow for updating the status of service requests programmatically.

---

## **Tech Stack**

- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: HTML, CSS (using Django templates)
- **Database**: SQLite (default, can be replaced with PostgreSQL, MySQL, etc.)
- **Other**: Bootstrap (optional for styling)

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/saharshpand3y/gas_utility_company.git
cd gas_utility_company
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run Migrations**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### **5. Create a Superuser**
```bash
python3 manage.py createsuperuser
```

### **6. Start the Development Server**
```bash
python3 manage.py runserver
```
## **Usage**

### **1. Submit a Service Request**
- Visit the http://127.0.0.1:9000/api/service-requests/ endpoint.
- Fill out the form with your name, email, phone number, address, request type, and details.

### **2. Track Service Requests**
- Visit the http://127.0.0.1:9000/api/track-requests/ endpoint.
- Enter your email address to view a list of your service requests and their statuses.

### **3. Manage Requests (Admin Panel)**
- Log in to the Django admin panel at /admin/ using the superuser credentials.
- Manage customers, service requests, and representative responses.

### **4. Update Request Status via API**
- Use the /api/service-requests/<id>/update-status/ endpoint to update the status of a service request.
- Example PATCH request:
```
PATCH /api/service-requests/1/update-status/ HTTP/1.1
Host: 127.0.0.1:9000
Content-Type: application/json

{
    "email": "testuser@example.com",
    "status": "resolved"
}

```

## Project Structure
```
gas_utility_company/
├── gas_utility/  # Project configuration files
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── customer_service/  # Main application
│   ├── migrations/  # Database migrations
│   ├── templates/  # HTML templates
│   │   ├── base.html
│   │   ├── service_requests.html
│   │   ├── track_requests.html
│   │   └── homepage.html
│   ├── static/  # Static files (CSS, JS, images)
│   ├── admin.py  # Admin configuration
│   ├── apps.py  # App configuration
│   ├── forms.py  # Django forms
│   ├── models.py  # Database models
│   ├── serializers.py  # DRF serializers
│   ├── tests.py  # Unit tests
│   ├── urls.py  # Application URLs
│   ├── views.py  # Views and logic
├── db.sqlite3  # SQLite database
├── manage.py  # Django management script
└── README.md  # Project documentation
```
## Acknowledgments
- Django Framework Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
