import smtplib

EMAIL = "YOUR EMAIL ID"
PASSWORD = "YOUR PASSWORD"

class NotificationManager:
    def send_emails(self, emails, names, message, booking_link):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for i in range(len(emails)):
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=emails[i],
                    msg=f"Subject:New Low Price Flight!\n\nHi {names[i]},\n{message}\nBooking link: {booking_link}".encode('utf-8'))