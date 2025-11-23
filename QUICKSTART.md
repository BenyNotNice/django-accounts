# Quick Start - Deploy to ArvanCloud

## 🚀 5-Minute Deployment

### 1️⃣ Push to Git (2 minutes)
```bash
# Initialize git (if not done)
git init
git add .
git commit -m "Ready for deployment"

# Create repo on GitHub/GitLab, then:
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### 2️⃣ ArvanCloud Setup (3 minutes)
1. **Login**: [panel.arvancloud.ir](https://panel.arvancloud.ir)
2. **PaaS** → **Create App** → **Docker**
3. **Connect** your Git repository
4. **Add Services**:
   - PostgreSQL (smallest plan)
   - Redis (smallest plan)

### 3️⃣ Environment Variables
Copy the connection strings from services, then add:

```env
SECRET_KEY=<generate with command below>
DEBUG=False
ALLOWED_HOSTS=your-app.iran.liara.run
DATABASE_URL=<from PostgreSQL service>
REDIS_URL=<from Redis service>
KAVEHNEGAR_API_KEY=<your API key>
```

**Generate SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 4️⃣ Deploy
Click **Deploy** button and wait ~2-3 minutes ⏱️

### 5️⃣ Test
Visit your app URL and test the login! 🎉

---

**Need help?** Check `DEPLOY.md` for detailed instructions.
