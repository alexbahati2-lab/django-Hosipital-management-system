🏥 Hospital Management System (HMS) — Project Roadmap & Development Guide
Tech Stack (Current Phase)

Backend: Django (Python)

Auth: Django Custom User Model + Role-Based Permissions

Database: SQLite (development) → PostgreSQL (production)

Frontend: Django Templates + Bootstrap

Deployment Target: Local Network → Cloud / Offline Sync later

✅ 1. Project Overview

The Hospital Management System (HMS) is designed to simplify and digitize hospital workflows from patient registration to discharge. The system supports multiple staff roles, each with controlled access to specific modules:

Role	Responsibilities
Admin	Manage system users, departments, reports
Receptionist	Register patients, schedule appointments
Doctor	View records, update diagnosis, write prescriptions
Nurse	Update vitals, assist doctor workflows
Lab Technician	Manage lab test orders & results
Pharmacist	Dispense drugs, manage pharmacy inventory
Accountant	Billing, invoices, payments & reports
📁 2. Project Folder Structure (Django Standard)
hospital_management/
│
├── venv/                    # Virtual environment
├── manage.py
├── hms/                     # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                # Authentication & user roles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/accounts/
│       ├── login.html
│       └── register_user.html
│
├── patients/                # Patient records module
├── appointments/            # Booking & scheduling
├── doctors/                 # Doctors module
├── pharmacy/                # Pharmaceuticals & inventory
├── laboratory/              # Lab tests results
├── billing/                 # Invoices & payments
│
└── templates/               # Shared UI templates
    ├── base.html
    ├── dashboard_admin.html
    ├── dashboard_doctor.html
    └── dashboard_reception.html


Each module will be added one by one, not all at once, to avoid confusion and errors.

🧰 3. Setup Instructions (Developer Workstation)

Terminal Commands

mkdir hospital_management
cd hospital_management

python -m venv venv
venv\Scripts\activate      # Windows

pip install django
django-admin startproject hms .

python manage.py startapp accounts
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open browser:

http://127.0.0.1:8000/

🔐 4. Authentication Plan (Phase 1)

Use a custom user model with role field.

Roles:
admin, doctor, nurse, receptionist, pharmacist, lab_tech, accountant

Features:

Login & Logout pages

Dashboard redirects based on role

Role-based access decorators

This prevents future redesign problems.

🧱 5. Module Development Plan (Build Order)
Phase	Module	Reason
1	Authentication (DONE FIRST)	Foundation for permissions
2	Patient Registration + Record Management	Core functionality
3	Appointments/Scheduling	Reception workflow
4	Doctor Dashboard + Consultations	Treatment workflow
5	Pharmacy	Medicine management & prescriptions
6	Laboratory	Test requests and results
7	Billing & Payments	Financial workflows
8	Roles + Reporting + Logging	Final polishing & compliance
We build one module completely before moving to the next.
🛰️ 6. Deployment & Scalability (Future Phases)
Stage	Environment	Notes
1	Local PC or Laptop	Small clinic, offline mode supported
2	Local Area Network (LAN)	Multi-computer setup
3	Cloud server (AWS / DigitalOcean)	Multi-branch hospital access
4	Mobile App (Flutter/Web)	Connect to backend via REST API
🌐 7. Offline + Online Hybrid (Later Upgrade)

We will introduce:

Local SQLite cache storage

Sync services via Django REST API

Background connectivity monitor

This allows hospitals in rural areas to still operate without internet.

🧾 8. Pricing Guide (Kenya Market)
Hospital Level	Description	Recommended Charge (KES)
Level 2-3 (Small Clinic)	Basic reception + doctor + pharmacy	65,000 – 180,000
Level 4-5 (Sub-County / Private Hospital)	Full HMS with lab, billing	250,000 – 600,000
Level 6 (Referral / Large Hospital)	Enterprise + API + backup	800,000 – 2.5M+

Monthly support/maintenance: KES 5,000 – 25,000 depending on size.

⭐ 9. Goals of This Project

Build a professional-grade HMS suitable for real hospitals.

Ensure the system works online + offline.

Provide clean UI for staff with low digital skills.

Create a product you can sell sustainably in Kenya and globally.