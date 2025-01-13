from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import random

def send_verification_email(email: str) -> int:
    """Send a visually appealing verification email with a code."""
    # Generate a random verification code
    code = random.randint(1000, 9999)  # 6-digit code
    
    # Email details
    subject = "Verify Your Email Address"
    from_email = "raices naturales"  # Sender's email address

    # Plain text fallback (for clients that don't support HTML emails)
    text_content = f"Use the following code to verify your email address: {code}"

    # HTML email content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
            <h2 style="text-align: center; color: #333;">Email Verification</h2>
            <p style="font-size: 16px; color: #555;">
                Hello, 
            </p>
            <p style="font-size: 16px; color: #555;">
                Thank you for signing up. To complete your registration, please use the verification code below:
            </p>
            <div style="text-align: center; margin: 20px 0;">
                <span style="display: inline-block; font-size: 24px; color: #333; font-weight: bold; padding: 10px 20px; border: 1px solid #ddd; border-radius: 4px; background: #f3f3f3;">
                    {code}
                </span>
            </div>
            <p style="font-size: 16px; color: #555;">
                If you didn't request this, please ignore this email.
            </p>
            <p style="font-size: 14px; color: #888; text-align: center;">
                &copy; 2025 Your Company Name. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """

    # Create email
    email_message = EmailMultiAlternatives(subject, text_content, from_email, [email])
    email_message.attach_alternative(html_content, "text/html")  # Attach HTML content

    # Send the email
    email_message.send()

    return code
