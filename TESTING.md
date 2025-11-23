# Testing the Dashboard

## How to Test the Login Flow

1. **Navigate to Login Page:**
   - Open your browser and go to: http://127.0.0.1:8000/login/

2. **Enter Phone Number:**
   - Enter any valid Iranian phone number (e.g., `09123456789`)
   - Click "ارسال کد تایید"

3. **Get OTP Code:**
   - Check your terminal where `python manage.py runserver` is running
   - Look for a line like: `Development Mode - OTP for 09123456789: XXXX`
   - Copy the 4-digit code

4. **Enter OTP:**
   - Enter the 4-digit code in the OTP input field
   - Click "ورود"

5. **View Dashboard:**
   - You should be automatically redirected to: http://127.0.0.1:8000/dashboard/
   - The dashboard will show:
     - Welcome message with your phone number
     - Account status (new or existing user)
     - Current time
     - Access and Refresh tokens (truncated)
     - Buttons to return to home or logout

## Dashboard Features

- **Welcome Card:** Shows your phone number and login status
- **Stats Cards:** Display account status, login time, and access level
- **Token Information:** Shows your JWT access and refresh tokens
- **Navigation:** Buttons to return home or logout
- **Auto-redirect:** If you visit the dashboard without tokens, you'll be redirected to login

## Logout

Click the "خروج" button to:
- Clear your tokens from localStorage
- Redirect back to the login page
