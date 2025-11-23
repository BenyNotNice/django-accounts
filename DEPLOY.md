# Django Accounts - Deployment Guide for ArvanCloud

This guide will walk you through deploying your Django OTP authentication app to ArvanCloud (Abre Arvan) using Docker.

## Prerequisites
- ✅ ArvanCloud account ([panel.arvancloud.ir](https://panel.arvancloud.ir))
- ✅ Git repository (GitHub/GitLab)
- ✅ KavehNegar API key for SMS

## Step 1: Prepare Your Code

### 1.1 Initialize Git Repository (if not already done)
```bash
cd /Users/benyamin/Dev/beni/accounts/accounts
git init
git add .
git commit -m "Initial commit - Django OTP app ready for deployment"
```

### 1.2 Create a GitHub/GitLab Repository
1. Go to GitHub.com or GitLab.com
2. Create a new repository (e.g., `django-accounts`)
3. **Do NOT initialize with README** (you already have code)

### 1.3 Push Your Code
```bash
git remote add origin https://github.com/YOUR_USERNAME/django-accounts.git
git branch -M main
git push -u origin main
```

## Step 2: Set Up ArvanCloud PaaS

### 2.1 Login to ArvanCloud
1. Go to [panel.arvancloud.ir](https://panel.arvancloud.ir)
2. Navigate to **PaaS** section from the sidebar

### 2.2 Create New Application
1. Click **"ایجاد اپلیکیشن جدید"** (Create New Application)
2. Choose **Docker** as the platform
3. Connect your Git repository:
   - Select GitHub or GitLab
   - Authorize ArvanCloud to access your repository
   - Select your `django-accounts` repository
   - Branch: `main`

### 2.3 Configure Build Settings
ArvanCloud will automatically detect your `Dockerfile` and use it to build your app.

- **Build Method**: Docker (auto-detected)
- **Port**: 8000 (ArvanCloud will map this automatically)

## Step 3: Add Required Services

### 3.1 Add PostgreSQL Database
1. In your app dashboard, go to **"سرویس‌ها"** (Services)
2. Click **"افزودن سرویس"** (Add Service)
3. Select **PostgreSQL**
4. Choose a plan (start with the smallest for testing)
5. Note the connection details provided

### 3.2 Add Redis Cache
1. Click **"افزودن سرویس"** (Add Service)
2. Select **Redis**
3. Choose a plan
4. Note the connection URL

## Step 4: Configure Environment Variables

In your app settings, go to **"متغیرهای محیطی"** (Environment Variables) and add:

| Variable | Value | Example |
|----------|-------|---------|
| `SECRET_KEY` | Generate a secure random string | `django-insecure-abc123xyz...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | Your domain | `myapp.iran.liara.run,myapp.com` |
| `DATABASE_URL` | From PostgreSQL service | `postgres://user:pass@host:5432/dbname` |
| `REDIS_URL` | From Redis service | `redis://host:6379/0` |
| `KAVEHNEGAR_API_KEY` | Your KavehNegar API key | `YOUR_API_KEY` |

### How to Generate SECRET_KEY
Run this in your terminal:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Step 5: Deploy!

1. Click **"استقرار"** (Deploy) button
2. ArvanCloud will:
   - Pull your code from Git
   - Build the Docker image
   - Run migrations automatically (via `entrypoint.sh`)
   - Start your application

3. Monitor the build logs to ensure everything completes successfully

## Step 6: Verify Deployment

### 6.1 Check Application Status
- Your app should show as **"در حال اجرا"** (Running)
- You'll get a URL like: `https://your-app.iran.liara.run`

### 6.2 Test Your Application
1. Visit your app URL
2. Test the login page at `/`
3. Try sending an OTP to verify SMS integration works

## Step 7: Custom Domain (Optional)

### 7.1 Add Your Domain
1. Go to **"دامنه‌ها"** (Domains)
2. Click **"افزودن دامنه"** (Add Domain)
3. Enter your domain (e.g., `accounts.mysite.com`)

### 7.2 Configure DNS
Add a CNAME record in your domain's DNS settings:
```
Type: CNAME
Name: accounts (or your subdomain)
Value: [provided by ArvanCloud]
```

### 7.3 Enable SSL
ArvanCloud provides free SSL certificates. Enable it in the domain settings.

## Troubleshooting

### Build Fails
- Check build logs in ArvanCloud dashboard
- Ensure `requirements.txt` has all dependencies
- Verify `Dockerfile` syntax

### Database Connection Error
- Verify `DATABASE_URL` is correctly set
- Check PostgreSQL service is running
- Ensure connection string format is correct

### Redis Connection Error
- Verify `REDIS_URL` is correctly set
- Check Redis service is running

### Static Files Not Loading
- Ensure `ALLOWED_HOSTS` includes your domain
- Check that `whitenoise` is in `requirements.txt`
- Verify `entrypoint.sh` runs `collectstatic`

### Migrations Not Applied
- Check deployment logs for migration output
- Manually run: Use ArvanCloud's console to run `python manage.py migrate`

## Updating Your Application

When you make changes:
1. Commit and push to Git:
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```
2. ArvanCloud will auto-deploy (if auto-deploy is enabled)
3. Or manually click **"استقرار مجدد"** (Redeploy)

## Monitoring & Logs

- **Logs**: View real-time logs in ArvanCloud dashboard
- **Metrics**: Monitor CPU, memory, and request metrics
- **Alerts**: Set up alerts for downtime or errors

## Cost Optimization

- Start with smallest plans for database and Redis
- Scale up based on actual usage
- Monitor resource usage in dashboard

## Security Checklist

- ✅ `DEBUG = False` in production
- ✅ Strong `SECRET_KEY`
- ✅ `ALLOWED_HOSTS` properly configured
- ✅ Database credentials in environment variables
- ✅ SSL/HTTPS enabled
- ✅ `.env` file not in Git repository

## Support

- **ArvanCloud Docs**: [docs.arvancloud.ir](https://docs.arvancloud.ir)
- **Support**: Available in ArvanCloud panel
- **Community**: ArvanCloud community forums

---

**Your app is now live! 🎉**
