#!/usr/bin/env python
import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail

try:
    print("Probando envío de email directo...")
    
    send_mail(
        'Test Email - Portfolio Direct',
        'Este es un email de prueba directo desde el script.\n\nName: Test User\nEmail: test@example.com\nSubject: Test Subject\nMessage: This is a test message.',
        settings.EMAIL_HOST_USER,
        ['isaialmeraz2003@gmail.com'],
        fail_silently=False,
    )
    
    print("✅ Email directo enviado exitosamente!")
    
except Exception as e:
    print(f"❌ Error al enviar email directo: {e}")
