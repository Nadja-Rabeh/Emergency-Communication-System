import smtplib
from geopy.geocoders import Nominatim

def send_email_alert(contact_email, subject, body):
    sender_email = "your_email@example.com"
    password = "your_password"
    
    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(sender_email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, contact_email, message)
        server.quit()
        print("Emergency alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def get_location():
    geolocator = Nominatim(user_agent="emergency_comm")
    location = geolocator.geocode("Your Address")
    return f"{location.latitude}, {location.longitude}"

if __name__ == "__main__":
    contact_email = "contact@example.com"
    subject = "Emergency Alert"
    location = get_location()
    body = f"Emergency situation! My current location is {location}. Please send help!"
    send_email_alert(contact_email, subject, body)
