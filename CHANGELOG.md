# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Add email verification option
- Implement password-based authentication as alternative
- Add user profile management endpoints
- Implement refresh token rotation
- Add comprehensive API documentation with Swagger/OpenAPI
- Add rate limiting for API endpoints
- Implement logging and monitoring

## [1.0.0] - 2025-01-28

### Added
- Initial release of Django Accounts OTP Authentication System
- Phone number-based user authentication
- OTP (One-Time Password) generation and verification
- JWT token authentication using SimpleJWT
- SMS integration with Kavehnegar API
- Redis caching for OTP storage
- RESTful API endpoints with Django REST Framework
- Custom user model with phone number as primary identifier
- Admin panel integration
- Beautiful UI templates with TailwindCSS and Vazir font
- PostgreSQL support for production
- SQLite support for development
- WhiteNoise for static file serving
- Production deployment configuration for Pars Pack PaaS
- Comprehensive documentation (README, CONTRIBUTING, CODE_OF_CONDUCT)
- Environment variable configuration with .env support
- Docker-ready configuration
- MIT License

### API Endpoints
- `POST /api/auth/send-otp/` - Request OTP code
- `POST /api/auth/verify-otp/` - Verify OTP and get JWT tokens
- `POST /api/auth/token/refresh/` - Refresh access token

### Security Features
- Secure OTP generation with random 4-digit codes
- OTP expiration (2 minutes by default)
- Rate limiting on OTP requests
- JWT token-based authentication
- HTTPS ready for production
- Environment-based configuration
- Secret key management

### Documentation
- Comprehensive README with bilingual support (English/Persian)
- Production deployment guide for Pars Pack PaaS
- Contributing guidelines
- Code of Conduct
- API documentation
- Environment variable templates

### Developer Experience
- Virtual environment support
- Easy local development setup
- Clear project structure
- Type hints and documentation
- Comprehensive .gitignore
- Example environment configuration

## Version History

### Version Numbering

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backward compatible manner
- **PATCH** version for backward compatible bug fixes

### How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

---

## Categories Explained

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Vulnerability fixes

---

<div align="center" dir="rtl">

## تاریخچه تغییرات (فارسی)

### نسخه 1.0.0 - 2025-01-28

#### افزوده شده
- سیستم احراز هویت با OTP
- یکپارچه‌سازی با API کاوه‌نگار
- توکن‌های JWT
- پشتیبانی از Redis
- رابط کاربری زیبا با TailwindCSS
- مستندات کامل به دو زبان

#### امنیت
- تولید امن کد OTP
- انقضای خودکار OTP
- محدودیت درخواست‌ها
- مدیریت امن کلیدهای محرمانه

</div>

---

[Unreleased]: https://github.com/YOUR_USERNAME/django-accounts/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/YOUR_USERNAME/django-accounts/releases/tag/v1.0.0
