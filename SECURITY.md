# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Django Accounts seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please do NOT:

- Open a public GitHub issue
- Discuss the vulnerability in public forums, social media, or mailing lists
- Exploit the vulnerability in any way

### Please DO:

**Report security vulnerabilities via email to: security@example.com**

Please include the following information in your report:

1. **Description**: A clear description of the vulnerability
2. **Impact**: The potential impact of the vulnerability
3. **Steps to Reproduce**: Detailed steps to reproduce the issue
4. **Proof of Concept**: If possible, include a proof of concept
5. **Suggested Fix**: If you have ideas on how to fix it (optional)
6. **Your Contact Info**: So we can follow up with you

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Communication**: We will keep you informed about the progress of fixing the vulnerability
- **Fix Timeline**: We aim to release a fix within 90 days of disclosure
- **Credit**: With your permission, we will publicly credit you for the discovery

## Security Best Practices

When using Django Accounts in production, please follow these security best practices:

### Environment Configuration

- **Never commit `.env` files** to version control
- **Always use `DEBUG=False`** in production
- **Keep `SECRET_KEY` secure** and unique per environment
- **Use strong, random secrets** for all security-sensitive settings
- **Rotate secrets regularly** (SECRET_KEY, API keys, etc.)

### Database & Cache

- **Use strong database passwords** with high entropy
- **Enable SSL/TLS** for database connections in production
- **Secure Redis** with authentication and network restrictions
- **Regular backups** of production databases
- **Encrypt backups** and store them securely

### Network & Infrastructure

- **Always use HTTPS** in production (enable SSL/TLS)
- **Set security headers** (HSTS, CSP, X-Frame-Options, etc.)
- **Enable CSRF protection** (enabled by default in Django)
- **Use secure cookies** (`SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`)
- **Implement rate limiting** on authentication endpoints
- **Use a WAF** (Web Application Firewall) if possible

### Authentication & Authorization

- **Implement OTP expiration** (default: 2 minutes)
- **Limit OTP attempts** to prevent brute force attacks
- **Rotate JWT tokens** regularly
- **Use short-lived access tokens** with refresh token rotation
- **Monitor for suspicious activity** (multiple failed attempts, etc.)
- **Implement account lockout** after repeated failures

### Dependencies

- **Keep dependencies updated** regularly
  ```bash
  pip list --outdated
  pip install --upgrade <package>
  ```
- **Run security audits**
  ```bash
  pip install safety
  safety check
  ```
- **Monitor security advisories** for Django and dependencies
- **Subscribe to Django security mailing list**

### Code Security

- **Validate all user input** rigorously
- **Sanitize output** to prevent XSS attacks
- **Use parameterized queries** (Django ORM does this by default)
- **Avoid SQL injection** (never use raw SQL with user input)
- **Implement proper access controls** on all endpoints
- **Log security events** (failed logins, suspicious activity)

### Monitoring & Logging

- **Enable comprehensive logging**
- **Monitor logs regularly** for security incidents
- **Set up alerts** for suspicious patterns
- **Implement audit trails** for sensitive operations
- **Use log aggregation** tools (ELK, Splunk, etc.)
- **Regularly review** access patterns and user behavior

### Deployment

- **Use environment variables** for all secrets
- **Enable automatic security updates** on servers
- **Minimize attack surface** (disable unused services)
- **Implement principle of least privilege** for all accounts
- **Regular security audits** and penetration testing
- **Incident response plan** in place

## Known Security Considerations

### OTP via SMS

- **SMS is not the most secure** method for 2FA
- **Consider adding** TOTP (Time-based OTP) as an alternative
- **SIM swapping attacks** are possible
- **For high-security applications**, consider hardware tokens or authenticator apps

### Rate Limiting

- **Current implementation** uses basic rate limiting
- **Consider using** Django Ratelimit or similar for production
- **Implement** distributed rate limiting with Redis

### Session Management

- **JWT tokens are stateless** and cannot be invalidated
- **Consider implementing** a token blacklist for logout
- **Short token expiration** mitigates this risk

## Security Checklist for Production

Before deploying to production, ensure:

- [ ] `DEBUG=False` is set
- [ ] `SECRET_KEY` is strong and unique
- [ ] `ALLOWED_HOSTS` is properly configured
- [ ] HTTPS/SSL is enabled
- [ ] Security headers are configured
- [ ] Database uses strong password
- [ ] Redis is secured with authentication
- [ ] `.env` file is not in version control
- [ ] `.gitignore` includes all sensitive files
- [ ] Dependencies are up to date
- [ ] Security audit has been performed
- [ ] Monitoring and logging are enabled
- [ ] Backup strategy is in place
- [ ] Incident response plan exists
- [ ] Rate limiting is configured
- [ ] CSRF protection is enabled
- [ ] Secure cookies are enabled

## Security Updates

We will publish security advisories as GitHub Security Advisories. Subscribe to notifications for this repository to stay informed.

## Compliance

This project follows:

- OWASP Top 10 guidelines
- Django security best practices
- CWE (Common Weakness Enumeration) standards

## Third-Party Security

We rely on several third-party packages. Their security is crucial to our project:

- **Django**: Follow the [Django security policy](https://docs.djangoproject.com/en/stable/internals/security/)
- **Django REST Framework**: Monitor [DRF security updates](https://www.django-rest-framework.org/community/release-notes/)
- **SimpleJWT**: Check [SimpleJWT security](https://github.com/jazzband/djangorestframework-simplejwt)

## Bug Bounty

Currently, we do not have a formal bug bounty program. However, we greatly appreciate security researchers who responsibly disclose vulnerabilities.

## Contact

For security-related questions or concerns:
- **Email**: security@example.com
- **PGP Key**: [Coming soon]

For general questions, please use GitHub Issues (but NOT for security vulnerabilities).

---

<div align="center" dir="rtl">

## خط‌مشی امنیتی (فارسی)

### گزارش آسیب‌پذیری‌های امنیتی

لطفاً آسیب‌پذیری‌های امنیتی را از طریق ایمیل به security@example.com گزارش دهید.

**لطفاً از ایجاد issue عمومی در GitHub خودداری کنید.**

### بهترین روش‌های امنیتی

- همیشه از `DEBUG=False` در production استفاده کنید
- هرگز فایل `.env` را commit نکنید
- از HTTPS در production استفاده کنید
- کلیدهای محرمانه را امن نگه دارید
- به‌طور منظم وابستگی‌ها را به‌روزرسانی کنید
- لاگ‌ها را برای فعالیت‌های مشکوک بررسی کنید

</div>

---

**Thank you for helping keep Django Accounts and our users safe!**
