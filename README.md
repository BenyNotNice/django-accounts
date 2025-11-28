<div align="center">

# Django Accounts - OTP Authentication System

<p align="center">
  <strong>Modern Django authentication system with OTP verification</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#api-endpoints">API</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.0+-green.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

</div>

---

## Overview

A production-ready Django authentication system using OTP (One-Time Password) verification via SMS. Built with modern best practices, this system provides a secure, scalable solution for phone number-based authentication.

### Key Highlights

- **Secure Authentication**: Phone number + OTP verification flow
- **JWT Tokens**: Stateless authentication with SimpleJWT
- **Production Ready**: Configured for deployment on Pars Pack PaaS
- **Modern Stack**: Django 5.0, DRF, Redis, PostgreSQL
- **Beautiful UI**: TailwindCSS with Persian font support (Vazir)
- **SMS Integration**: Kavehnegar API for OTP delivery

---

## Features

- Phone number-based user registration and login
- OTP generation and verification with expiration
- JWT access and refresh token management
- Redis caching for OTP storage and performance
- RESTful API endpoints with Django REST Framework
- Admin panel with custom user model
- WhiteNoise for efficient static file serving
- PostgreSQL database support for production
- Comprehensive error handling and validation
- Persian/Farsi language support

---

## Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Django 5.0+ |
| **API** | Django REST Framework |
| **Authentication** | SimpleJWT |
| **Database** | PostgreSQL (Production), SQLite (Development) |
| **Cache** | Redis |
| **SMS Provider** | Kavehnegar API |
| **Static Files** | WhiteNoise |
| **Frontend** | TailwindCSS + Vazir Font |
| **Deployment** | Pars Pack PaaS |

---

## Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Redis (optional for development, required for production)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/django-accounts.git
cd django-accounts
```

2. **Create virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
```

Edit `.env` and configure your settings:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1
```

Generate a new SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create superuser** (optional)

```bash
python manage.py createsuperuser
```

7. **Collect static files**

```bash
python manage.py collectstatic --noinput
```

8. **Run development server**

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your application running!

---

## API Endpoints

### Send OTP

Request a one-time password for phone verification.

```http
POST /api/auth/send-otp/
Content-Type: application/json

{
  "phone_number": "09123456789"
}
```

**Response:**
```json
{
  "detail": "OTP sent successfully",
  "expires_in": 120
}
```

### Verify OTP

Verify the OTP code and receive JWT tokens.

```http
POST /api/auth/verify-otp/
Content-Type: application/json

{
  "phone_number": "09123456789",
  "code": "1234"
}
```

**Response:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "is_new_user": true
}
```

---

## Project Structure

```
accounts/
├── accounts/                   # Main application
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   └── accounts/
│   │       ├── index.html     # Landing page
│   │       ├── login.html     # Login page
│   │       └── dashboard.html # User dashboard
│   ├── models.py              # Custom User model
│   ├── serializers.py         # DRF serializers
│   ├── services.py            # OTP & SMS services
│   ├── urls.py                # App URL routing
│   └── apps.py                # App configuration
├── config/                     # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI application
├── static/                     # Static files (collected)
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version for PaaS
├── Procfile                   # PaaS deployment commands
├── README.md                  # This file
├── PRODUCTION_SETUP.md        # Production deployment guide
├── LICENSE                    # MIT License
└── CONTRIBUTING.md            # Contribution guidelines
```

---

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DEBUG` | Enable debug mode | Yes | `False` |
| `SECRET_KEY` | Django secret key | Yes | - |
| `DATABASE_URL` | Database connection string | Yes | SQLite in dev |
| `REDIS_URL` | Redis connection URL | Yes | - |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | Yes | - |
| `KAVEHNEGAR_API_KEY` | SMS API key | No | - |

### Development Example

```env
DEBUG=True
SECRET_KEY=django-insecure-dev-key-change-in-production
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Production Example

```env
DEBUG=False
SECRET_KEY=your-strong-production-secret-key
DATABASE_URL=postgresql://user:password@host:5432/dbname
REDIS_URL=redis://redis-host:6379/0
ALLOWED_HOSTS=yourdomain.com,*.parspack.app
KAVEHNEGAR_API_KEY=your-kavehnegar-api-key
```

---

## Deployment

This project is configured for deployment on **Pars Pack PaaS**. For detailed production deployment instructions, see:

**[PRODUCTION_SETUP.md](PRODUCTION_SETUP.md)** (Persian)

### Quick Deployment Checklist

- [ ] Push code to GitHub
- [ ] Create PostgreSQL database on Pars Pack
- [ ] Create Redis cache on Pars Pack
- [ ] Create PaaS application and connect to GitHub
- [ ] Configure environment variables
- [ ] Deploy and verify

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

---

## Testing

Run the test suite:

```bash
python manage.py test
```

---

## Security

- Never commit `.env` files to version control
- Always use `DEBUG=False` in production
- Keep `SECRET_KEY` secure and unique
- Use HTTPS in production
- Regularly update dependencies
- Monitor logs for suspicious activity

If you discover a security vulnerability, please email security@example.com instead of using the issue tracker.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Django community for the amazing framework
- Django REST Framework for the API toolkit
- Kavehnegar for SMS services
- Pars Pack for hosting infrastructure

---

## Support

If you need help or have questions:

- Open an [Issue](https://github.com/YOUR_USERNAME/django-accounts/issues)
- Read the [Production Setup Guide](PRODUCTION_SETUP.md)
- Check the [Django Documentation](https://docs.djangoproject.com/)

---

<div align="center">

**Made with ❤️ for the Iranian developer community**

**ساخته شده با ❤️ برای جامعه توسعه‌دهندگان ایرانی**

[Report Bug](https://github.com/YOUR_USERNAME/django-accounts/issues) • [Request Feature](https://github.com/YOUR_USERNAME/django-accounts/issues)

</div>

---

## Persian Documentation | مستندات فارسی

<div dir="rtl">

## درباره پروژه

یک سیستم احراز هویت مدرن و آماده برای استفاده در پروداکشن با استفاده از OTP (رمز یکبار مصرف) برای Django. این پروژه با بهترین روش‌های توسعه نرم‌افزار ساخته شده و راه‌حل امن و مقیاس‌پذیری برای احراز هویت مبتنی بر شماره موبایل ارائه می‌دهد.

## ویژگی‌های کلیدی

- احراز هویت امن با شماره موبایل و OTP
- توکن‌های JWT برای احراز هویت بدون وضعیت
- آماده برای استقرار در پارس پک
- استک مدرن: Django 5.0، DRF، Redis، PostgreSQL
- رابط کاربری زیبا با TailwindCSS و فونت وزیر
- یکپارچه‌سازی با API کاوه‌نگار

## نصب سریع

### پیش‌نیازها

- Python 3.11 یا بالاتر
- pip
- Redis (اختیاری برای توسعه، الزامی برای پروداکشن)

### مراحل نصب

دستورات نصب در بخش انگلیسی همین سند موجود است.

## استقرار در Production

برای راهنمای کامل استقرار در پارس پک، فایل زیر را مطالعه کنید:

**[راهنمای استقرار Production](PRODUCTION_SETUP.md)**

## مشارکت

از مشارکت شما استقبال می‌کنیم! لطفاً برای تغییرات عمده ابتدا یک Issue باز کنید.

## پشتیبانی

اگر سوال یا مشکلی دارید:
- یک [Issue](https://github.com/YOUR_USERNAME/django-accounts/issues) باز کنید
- [راهنمای استقرار](PRODUCTION_SETUP.md) را مطالعه کنید

</div>
