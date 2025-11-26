# Django Accounts - OTP Authentication System

یک سیستم احراز هویت مدرن با OTP (رمز یکبار مصرف) برای Django

## ویژگی‌ها

- ✅ احراز هویت با شماره موبایل و OTP
- ✅ ارسال SMS از طریق کاوه‌نگار
- ✅ JWT Authentication با Simple JWT
- ✅ REST API با Django REST Framework
- ✅ Cache با Redis
- ✅ رابط کاربری مدرن با TailwindCSS
- ✅ آماده برای استقرار در پارس پک

## نصب و راه‌اندازی محلی

### پیش‌نیازها
- Python 3.11+
- pip
- (اختیاری) Redis برای cache

### مراحل نصب

1. کلون کردن repository:
```bash
git clone https://github.com/YOUR_USERNAME/django-accounts.git
cd django-accounts
```

2. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

3. تنظیم environment variables:
```bash
cp .env.example .env
# ویرایش .env و تنظیم متغیرها
```

4. تولید SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. مایگریشن دیتابیس:
```bash
python manage.py migrate
```

6. جمع‌آوری فایل‌های استاتیک:
```bash
python manage.py collectstatic --noinput
```

7. اجرای سرور:
```bash
python manage.py runserver
```

اپلیکیشن در `http://localhost:8000` در دسترس خواهد بود.

## استقرار در Production

برای استقرار در پارس پک، راهنمای کامل را در فایل زیر مطالعه کنید:

📖 **[PRODUCTION_SETUP.md](PRODUCTION_SETUP.md)**

### خلاصه مراحل استقرار:

1. Push کد به GitHub
2. ایجاد PostgreSQL و Redis در پارس پک
3. ایجاد اپلیکیشن PaaS و اتصال به GitHub
4. تنظیم Environment Variables
5. Deploy!

## ساختار پروژه

```
accounts/
├── accounts/              # اپلیکیشن اصلی
│   ├── models.py         # مدل کاربر
│   ├── views.py          # API Views
│   ├── serializers.py    # DRF Serializers
│   ├── services.py       # سرویس‌های SMS و OTP
│   └── templates/        # صفحات HTML
├── config/               # تنظیمات Django
│   ├── settings.py       # تنظیمات اصلی
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI config
├── requirements.txt      # وابستگی‌های Python
├── runtime.txt          # نسخه Python
├── Procfile             # دستورات PaaS
└── .env.example         # نمونه متغیرهای محیطی
```

## API Endpoints

### ارسال OTP
```http
POST /api/auth/send-otp/
Content-Type: application/json

{
  "phone_number": "09123456789"
}
```

### تایید OTP
```http
POST /api/auth/verify-otp/
Content-Type: application/json

{
  "phone_number": "09123456789",
  "code": "1234"
}
```

پاسخ موفق:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "is_new_user": true
}
```

## تنظیمات Environment Variables

### محیط Development:
```env
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-dev-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

### محیط Production:
```env
DEBUG=False
DATABASE_URL=postgresql://user:pass@host:port/dbname
REDIS_URL=redis://host:port/0
SECRET_KEY=your-strong-production-secret-key
ALLOWED_HOSTS=yourdomain.com,*.parspack.app
KAVEHNEGAR_API_KEY=your-api-key
```

## تکنولوژی‌ها

- **Backend**: Django 5.0+
- **API**: Django REST Framework
- **Authentication**: Simple JWT
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Cache**: Redis
- **SMS**: Kavehnegar API
- **Static Files**: WhiteNoise
- **Frontend**: TailwindCSS + Vazir Font
- **Deployment**: Pars Pack PaaS

## مشارکت

1. Fork کنید
2. یک branch جدید بسازید (`git checkout -b feature/amazing-feature`)
3. تغییرات خود را commit کنید (`git commit -m 'Add amazing feature'`)
4. Push کنید (`git push origin feature/amazing-feature`)
5. یک Pull Request باز کنید

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

## پشتیبانی

اگر سوالی دارید یا به کمک نیاز دارید:
- Issues را در GitHub باز کنید
- به مستندات [PRODUCTION_SETUP.md](PRODUCTION_SETUP.md) مراجعه کنید

---

**ساخته شده با ❤️ برای جامعه توسعه‌دهندگان ایرانی**
