import psutil
import smtplib
from email.message import EmailMessage
DISK = psutil.disk_usage('/')
THRESHOLD = 80  # Percent
if DISK.percent > THRESHOLD:
    MSG = EmailMessage()
    MSG.set_content(f"Warning: Disk usage at {DISK.percent}% (Free: {DISK.free / (1024**3):.2f} GB)")
    MSG['Subject'] = 'System Monitoring Alert'
    MSG['From'] = 'tsikyloharantsoa@gmail.com'  # Replace with your Gmail
    MSG['To'] = 'tsikyloharantsoa@gmail.com'    # Replace with recipient
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SERVER:
            SERVER.login('tsikyloharantsoa@gmail.com', 'aaqndmzlqbkkizub')  # Replace with App Password
            SERVER.send_message(MSG)
        print("Alert email sent!")
    except Exception as e:
        print(f"Email failed: {e}")
else:
    print(f"Disk usage OK: {DISK.percent}%")
