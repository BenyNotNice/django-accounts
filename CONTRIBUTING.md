# Contributing to Django Accounts

First off, thank you for considering contributing to Django Accounts! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Commit Messages](#commit-messages)
- [Questions?](#questions)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**

```markdown
## Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., macOS 13.0]
- Python version: [e.g., 3.11.5]
- Django version: [e.g., 5.0.1]
- Browser (if applicable): [e.g., Chrome 120]

## Additional Context
Add any other context, screenshots, or logs about the problem.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title** describing the enhancement
- **Detailed description** of the proposed functionality
- **Use cases** explaining why this would be useful
- **Possible implementation** if you have ideas

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write a clear commit message** following our guidelines
6. **Submit the pull request**

**Pull Request Checklist:**

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex code
- [ ] Documentation updated (if applicable)
- [ ] No new warnings generated
- [ ] Tests added/updated (if applicable)
- [ ] All tests pass locally
- [ ] Commit messages follow guidelines

## Development Setup

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/django-accounts.git
cd django-accounts
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

### 8. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names

### Django Best Practices

- Follow [Django coding style](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/)
- Use Django's built-in features when possible
- Keep views thin, use service layers for business logic
- Use Django's ORM, avoid raw SQL unless necessary

### Code Organization

```python
# Imports order:
# 1. Standard library imports
import os
import sys

# 2. Related third-party imports
from django.db import models
from rest_framework import serializers

# 3. Local application imports
from accounts.models import User
```

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `UserManager`, `OTPService`)
- **Functions/Methods**: `snake_case` (e.g., `send_otp`, `verify_code`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_OTP_ATTEMPTS`)
- **Files**: `snake_case.py` (e.g., `user_service.py`)

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Writing Tests

- Write tests for new features
- Update tests when modifying existing features
- Aim for high test coverage
- Use descriptive test names

```python
class UserModelTestCase(TestCase):
    def test_create_user_with_phone_number(self):
        """Test creating a user with a valid phone number"""
        user = User.objects.create_user(
            phone_number='09123456789'
        )
        self.assertEqual(user.phone_number, '09123456789')
        self.assertTrue(user.is_active)
```

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good commit messages
feat(auth): add OTP verification endpoint
fix(models): correct phone number validation regex
docs(readme): update installation instructions
refactor(services): simplify OTP generation logic

# Bad commit messages
fix bug
update code
changes
asdfgh
```

### Detailed Example

```
feat(auth): add rate limiting for OTP requests

Add rate limiting to prevent abuse of OTP sending endpoint.
Users are now limited to 3 OTP requests per phone number
within a 10-minute window.

- Implement Redis-based rate limiting
- Add configuration for rate limit settings
- Update API documentation
- Add tests for rate limiting behavior

Closes #123
```

## Pull Request Process

1. **Update Documentation**: Ensure README.md and relevant docs are updated
2. **Add Tests**: Include tests for your changes
3. **Update CHANGELOG.md**: Add your changes under "Unreleased"
4. **Self-Review**: Review your own code before submitting
5. **Request Review**: Request review from maintainers
6. **Address Feedback**: Make requested changes promptly
7. **Merge**: Once approved, a maintainer will merge your PR

## Questions?

- Check the [README](README.md) for general information
- Look through [existing issues](https://github.com/YOUR_USERNAME/django-accounts/issues)
- Open a new issue with the "question" label

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- CHANGELOG.md for significant contributions
- README.md acknowledgments section

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

<div align="center" dir="rtl">

## راهنمای مشارکت به فارسی

### چگونه مشارکت کنیم؟

1. **Fork** کردن repository
2. ایجاد **branch** جدید برای ویژگی یا اصلاح
3. **Commit** کردن تغییرات با پیام‌های واضح
4. **Push** کردن به branch خود
5. ایجاد **Pull Request**

### استانداردهای کد

- رعایت [PEP 8](https://pep8.org/)
- استفاده از نام‌های توصیفی برای متغیرها
- نوشتن تست برای ویژگی‌های جدید
- به‌روزرسانی مستندات در صورت نیاز

### سوال دارید؟

در صورت داشتن سوال، می‌توانید یک Issue جدید باز کنید.

</div>

---

Thank you for contributing to Django Accounts!
