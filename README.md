# IRIS FAMILY HOSTEL – Django Web Application

A full Django website for **IRIS FAMILY HOSTEL** with:
- Business-style home page
- Public kids section
- Admin-only invoice management (bulk generation for all kids with same Amount & VAT)

## Features

- **Home page** with modern UI (static CSS) and hostel details.
- **Kids**: public list of kids (name, parent, age, room, etc.).
- **Invoices**: Staff-only portal to generate monthly invoices in bulk for all active kids. Prevents duplicates per kid/month/year. Printable invoice page.
- **Authentication**: Built-in Django auth for login/logout. Use Django Admin to add/edit kids.

## Tech

- Django 5 + SQLite (default)
- Minimal dependencies (Pillow for optional kid photos)
- Ready-to-run locally

## Quick Start

> Requires Python 3.10+

```bash
# 1) Create and activate a virtualenv
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

# 2) Install requirements
pip install -r requirements.txt

# 3) Run migrations
python manage.py makemigrations
python manage.py migrate

# 4) Create a superuser (admin)
python manage.py createsuperuser

# 5) (Optional) Seed 14 sample kids
python manage.py seed_kids

# 6) Start the dev server
python manage.py runserver
```

Open http://127.0.0.1:8000/

- Public pages: **Home** `/` and **Kids** `/kids/`
- Admin login: `/accounts/login/` (use your superuser)
- Invoices: `/billing/invoices/` (staff only)
- Bulk generate invoices: `/billing/generate/`

## How Bulk Billing Works

- Go to **Generate Invoices**.
- Enter **Month**, **Year**, **Amount** (e.g. `5000.00`) and **VAT %** (e.g. `13`).
- It will create an invoice per **active kid**.
- If an invoice for a kid already exists for that month/year, it is **skipped**.
- View all invoices at `/billing/invoices/`. Click an invoice to open a printable view.

## Managing Kids

- Add/edit kids via **Django Admin** (`/admin/`).
- Fields: name, parent_name, age, room_number, guardian_contact, admission_date, photo, active.

## Project Structure

```
iris_family_hostel/
├─ manage.py
├─ requirements.txt
├─ iris_hostel/
│  ├─ iris_hostel/
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ asgi.py
│  ├─ core/
│  ├─ kids/
│  └─ billing/
├─ templates/
│  ├─ base.html
│  └─ registration/login.html
├─ static/
│  ├─ css/styles.css
│  └─ images/hero.jpg
```

## Notes

- This app is for local/dev use (DEBUG=True). For production, configure `ALLOWED_HOSTS`, static files and a real secret key.
- Static files are served from `/static/` in development.
- Time zone is set to **Asia/Kathmandu**.

---

Built for IRIS FAMILY HOSTEL.
