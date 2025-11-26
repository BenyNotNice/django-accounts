# راهنمای استقرار Production در پارس پک

راهنمای کامل برای استقرار پروژه Django Accounts در پارس پک از طریق GitHub

---

## پیش‌نیازها ✅

1. ✅ حساب کاربری پارس پک فعال
2. ✅ کد در GitHub repository
3. ✅ خرید سرویس PaaS پارس پک

---

## مرحله 1: آماده‌سازی GitHub Repository

### 1.1 کامیت تغییرات

```bash
cd /Users/benyamin/Dev/beni/accounts/accounts

# بررسی تغییرات
git status

# اضافه کردن تمام تغییرات
git add -A

# کامیت
git commit -m "Prepare for production deployment

- Configure cache for both dev and production
- Update environment variables
- Add production deployment guides
- Ready for Pars Pack deployment"

# پوش به GitHub
git push origin main
```

### 1.2 تایید فایل‌های ضروری

مطمئن شوید این فایل‌ها در repository شما وجود دارند:
- ✅ `runtime.txt` - نسخه Python
- ✅ `Procfile` - دستورات اجرا
- ✅ `requirements.txt` - وابستگی‌ها
- ✅ `.env.example` - نمونه متغیرهای محیطی
- ✅ `.gitignore` - حاوی `.env` و فایل‌های حساس

---

## مرحله 2: ایجاد سرویس‌های پارس پک

### 2.1 ایجاد PostgreSQL Database

1. وارد پنل پارس پک شوید: https://parspack.com
2. از منوی سمت چپ → **Databases** یا **پایگاه داده**
3. کلیک روی **ایجاد پایگاه داده جدید**
4. انتخاب **PostgreSQL**
5. تنظیمات:
   - نام: `accounts_db` (یا هر نام دیگر)
   - نسخه: جدیدترین نسخه (14 یا 15)
   - منابع: حداقل 256MB RAM
6. روی **ایجاد** کلیک کنید
7. **مهم**: اطلاعات اتصال را کپی و در جای امن ذخیره کنید:
   ```
   Host: pg-xxxxx.parspack.com
   Port: 5432
   Database: accounts_db
   Username: user_xxxxx
   Password: xxxxxxxxxx
   ```

### 2.2 ایجاد Redis Cache

1. در پنل پارس پک → **Databases** یا **Add-ons**
2. کلیک روی **ایجاد Redis جدید**
3. تنظیمات:
   - نام: `accounts_cache` (یا هر نام دیگر)
   - نسخه: جدیدترین نسخه
   - منابع: حداقل 128MB RAM
4. روی **ایجاد** کلیک کنید
5. **مهم**: اطلاعات اتصال را کپی کنید:
   ```
   Host: redis-xxxxx.parspack.com
   Port: 6379
   Password: xxxxxxxxxx (اگر دارد)
   ```

---

## مرحله 3: ایجاد اپلیکیشن PaaS

### 3.1 ایجاد اپلیکیشن جدید

1. در پنل پارس پک → **PaaS** یا **برنامه‌ها**
2. کلیک روی **ایجاد برنامه جدید**
3. انتخاب **Python/Django** (نه Docker!)
4. تنظیمات اولیه:
   - **نام برنامه**: `accounts` (یا هر نام دلخواه)
   - **نوع استقرار**: Git Repository
   - **Platform**: Python
   - **Python Version**: 3.11

### 3.2 اتصال به GitHub

1. در بخش Source Code:
   - **Repository URL**: آدرس GitHub repository خود
   - **Branch**: `main` (یا `master`)
   - اگر repository خصوصی است، token GitHub را وارد کنید

2. تنظیمات Build:
   - **Build Command**: خالی بگذارید (از Procfile استفاده می‌شود)
   - **Start Command**: خالی بگذارید (از Procfile استفاده می‌شود)

---

## مرحله 4: تنظیم Environment Variables

در پنل اپلیکیشن → **Environment Variables** یا **متغیرهای محیطی**

### 4.1 متغیرهای ضروری

#### SECRET_KEY
تولید یک SECRET_KEY جدید:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
سپس در پنل:
```
Key: SECRET_KEY
Value: [کلید تولید شده]
```

#### DEBUG
```
Key: DEBUG
Value: False
```

#### ALLOWED_HOSTS
دامنه اختصاص داده شده از پارس پک را وارد کنید (مثلاً `myapp.parspack.app`):
```
Key: ALLOWED_HOSTS
Value: myapp.parspack.app,*.abrhapaas.com
```

#### DATABASE_URL
از اطلاعات PostgreSQL که در مرحله 2.1 گرفتید:
```
Key: DATABASE_URL
Value: postgresql://user_xxxxx:password@pg-xxxxx.parspack.com:5432/accounts_db
```

#### REDIS_URL
از اطلاعات Redis که در مرحله 2.2 گرفتید:
```
Key: REDIS_URL
Value: redis://redis-xxxxx.parspack.com:6379/0
```
یا اگر password دارد:
```
Value: redis://:password@redis-xxxxx.parspack.com:6379/0
```

### 4.2 متغیرهای اختیاری

#### KAVEHNEGAR_API_KEY (برای ارسال SMS واقعی)
```
Key: KAVEHNEGAR_API_KEY
Value: [API Key از کاوه‌نگار]
```

**نکته**: اگر این را تنظیم نکنید، OTP در لاگ‌های سرور چاپ می‌شود (فقط برای DEBUG=True)

---

## مرحله 5: تنظیمات منابع (Resources)

در پنل اپلیکیشن → **Resources** یا **منابع**

### توصیه شده برای شروع:
- **RAM**: 512MB (حداقل) یا 1GB (پیشنهادی)
- **CPU**: 0.5 Core (حداقل) یا 1 Core (پیشنهادی)
- **Storage**: 1GB (کافی است)

### Scale Up در صورت نیاز:
- اگر ترافیک بالا رفت → افزایش RAM و CPU
- اگر فایل‌های media زیاد شد → افزایش Storage

---

## مرحله 6: Deploy اپلیکیشن

1. در پنل اپلیکیشن، روی **Deploy** یا **استقرار** کلیک کنید
2. منتظر بمانید تا build و deploy کامل شود (2-5 دقیقه)
3. لاگ‌های build را بررسی کنید:
   - نصب dependencies از `requirements.txt`
   - اجرای migrations از `Procfile`
   - جمع‌آوری static files

### اگر build موفق بود:
- وضعیت اپلیکیشن: **Running** یا **در حال اجرا**
- یک URL دریافت می‌کنید: `https://myapp.parspack.app`

### اگر build با خطا مواجه شد:
- لاگ‌های خطا را بررسی کنید
- بخش "عیب‌یابی" در انتهای این سند را ببینید

---

## مرحله 7: تنظیم دامنه (اختیاری)

### استفاده از دامنه شخصی:

1. در پنل اپلیکیشن → **Domains** یا **دامنه**
2. کلیک روی **افزودن دامنه**
3. دامنه خود را وارد کنید: `accounts.yourdomain.com`
4. یک CNAME record در تنظیمات DNS دامنه خود ایجاد کنید:
   ```
   Type: CNAME
   Name: accounts
   Value: [آدرس از پارس پک]
   ```
5. فعال‌سازی SSL رایگان (Let's Encrypt)
6. دامنه جدید را به `ALLOWED_HOSTS` اضافه کنید

---

## مرحله 8: تست اپلیکیشن

### 8.1 بررسی صفحه اصلی
```
https://myapp.parspack.app/
```
باید صفحه index نمایش داده شود.

### 8.2 تست صفحه Login
```
https://myapp.parspack.app/login/
```
شماره موبایل وارد کنید و OTP درخواست دهید.

### 8.3 بررسی Admin Panel
```
https://myapp.parspack.app/admin/
```

اگر هنوز superuser ندارید، از Console در پنل پارس پک:
```bash
python manage.py createsuperuser
```

### 8.4 چک کردن لاگ‌ها
در پنل → **Logs** یا **گزارش‌ها**
- OTP codes (اگر SMS تنظیم نشده)
- خطاها و warnings
- درخواست‌های HTTP

---

## عیب‌یابی (Troubleshooting)

### خطا: Build Failed

#### علت 1: requirements.txt
```bash
# در local تست کنید:
pip install -r requirements.txt
```

#### علت 2: Python version
- مطمئن شوید `runtime.txt` درست است: `python-3.11`

### خطا: Application Crashed

#### علت 1: Environment Variables
- تمام متغیرهای ضروری را چک کنید
- `SECRET_KEY` نباید خالی باشد
- `DATABASE_URL` باید به PostgreSQL واقعی اشاره کند

#### علت 2: Database Connection
```bash
# از Console پارس پک تست کنید:
python manage.py dbshell
# یا
python manage.py migrate
```

#### علت 3: Redis Connection
- مطمئن شوید `REDIS_URL` درست است
- یا Redis service را در پارس پک restart کنید

### خطا: Static Files نمایش داده نمی‌شوند

```bash
# از Console:
python manage.py collectstatic --noinput
```

مطمئن شوید `Procfile` شامل این دستور است:
```
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
```

### خطا: 500 Internal Server Error

1. لاگ‌ها را بررسی کنید (Logs section)
2. `DEBUG=True` موقتاً فعال کنید (فقط برای debug!)
3. خطای دقیق را پیدا کنید
4. بعد از fix، حتماً `DEBUG=False` کنید

---

## چک‌لیست نهایی Production

قبل از Go Live:

- [ ] `DEBUG=False` تنظیم شده
- [ ] `SECRET_KEY` قوی و منحصر به فرد است
- [ ] `ALLOWED_HOSTS` شامل دامنه production است
- [ ] PostgreSQL متصل و migrations اجرا شده
- [ ] Redis متصل و کار می‌کند
- [ ] Static files جمع‌آوری شده‌اند
- [ ] SSL/HTTPS فعال است
- [ ] Admin panel قابل دسترسی است
- [ ] OTP system کار می‌کند
- [ ] Logs بررسی شده و خطایی وجود ندارد
- [ ] Backup از database گرفته شده

---

## Monitoring و Maintenance

### روزانه:
- بررسی لاگ‌ها برای خطاها
- مانیتور کردن استفاده از منابع (CPU, RAM)

### هفتگی:
- بررسی Database size
- بررسی تعداد کاربران جدید

### ماهانه:
- Backup از database
- Update dependencies (در صورت نیاز)
- بررسی امنیتی

---

## پشتیبانی

### مستندات پارس پک:
- https://docs.parspack.com/paas/

### پشتیبانی پارس پک:
- تیکت: https://parspack.com/support
- تلگرام: @parspack_support

### Django Documentation:
- https://docs.djangoproject.com/

---

## نکات امنیتی مهم

1. **هرگز** `.env` را commit نکنید
2. **هرگز** `DEBUG=True` در production نگذارید
3. **همیشه** از HTTPS استفاده کنید
4. **مرتباً** backup از database بگیرید
5. **محدود کنید** دسترسی به admin panel
6. **مانیتور کنید** لاگ‌ها برای فعالیت‌های مشکوک

---

**موفق باشید! 🚀**

اگر سوالی دارید یا به کمک نیاز دارید، به تیم پشتیبانی پارس پک مراجعه کنید.
