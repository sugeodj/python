import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, recipient_email, recipient_name, subject, message, attachment_paths):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change the SMTP server accordingly if not using Gmail
        server.starttls()
        server.login(sender_email, sender_password)

        # Create a multi-part email object
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = recipient_email
        email["Subject"] = subject

        # Create the email body
        body = f"Dear {recipient_name},\n\n"
        body += f"I hope this email finds you well. My name is Daniel Geovanovich, and I am reaching out to express my strong interest in pursuing a career in the IT field, preferably as a junior developer.\n\n"
        body += "Whilst currently studying a Bachelor of Information Technology degree, with a focus on Networking, Cybersecurity, and Software Development, I possess a solid foundation in problem-solving, programming, and network fundamentals.\n\n"

        # Add paragraphs from the message list
        for paragraph in message:
            body += f"{paragraph}\n\n"

        body += "Thank you for considering my application. I have a strong interest in your company and would appreciate the opportunity to discuss further how my skills and experience align with your requirements. I am available at your convenience for an interview or any additional information you may need.\n\n"
        body += "Looking forward to hearing from you.\n\n"
        body += "Kind regards,\n"
        body += "Daniel Geovanovich\n"
        body += "Email: dgeovanovich@gmail.com\n"
        body += "Phone: 0438 857 084\n"
        body += "LinkedIn: linkedin.com/in/daniel-geovanovich-09a8911b6\n\n"
        body += "You can find a Cover Letter as well as my CV attached."

        # Add the message body
        email.attach(MIMEText(body, "plain"))

        # Attach files
        for attachment_path in attachment_paths:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(file.read(), Name=attachment_path)
            attachment["Content-Disposition"] = f"attachment; filename={attachment_path}"
            email.attach(attachment)

        # Send the email
        server.sendmail(sender_email, recipient_email, email.as_string())
        server.quit()

        print(f"Email sent to {recipient_email} successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email to {recipient_email}: {str(e)}")


def automate_emails(sender_email, sender_password, subject, message, attachment_paths):
    with open('lists/emails.txt', 'r') as file:
        emails = file.read().splitlines()

    for email in emails:
        recipient_email = email
        recipient_name = email.split('@')[0]
        send_email(sender_email, sender_password, recipient_email, recipient_name, subject, message, attachment_paths)


# Configuration
sender_email = "dgeovanovich@gmail.com"  # Enter your email address
sender_password = "jeipexbcitwrfqza"  # Enter your email password or app password
subject = "IT Job Application: Daniel Geovanovich"  # Enter the email subject
message = [
    "I have attached my cover letter and resume for your review, which provide more detailed information about my skills and experience. I would be grateful if you could take a moment to go through them.",
    "Throughout my academic journey, I have gained valuable experience and showcased my technical abilities through various projects. For instance, I developed a Live Tobacco Prices website that involved web scraping, data analysis, and website design. This project received an overwhelming positive response from the community, demonstrating my creativity and dedication to delivering high-quality results.",
    "Additionally, I implemented a Plex Media Streaming server using a Raspberry Pi, which allowed for seamless local streaming of media content. This project enhanced my skills in server setup and configuration, further strengthening my technical expertise.",
    "One of my most significant achievements was the development of an Income Tax Calculator software program using Visual Basic. This project earned me an outstanding grade of A+ and showcased my ability to work independently while applying my programming and data analysis skills. The calculator offered precise tax calculations, improved accuracy rates, and enhanced user satisfaction compared to previous tools.",
    "In addition to my technical proficiency, I have gained practical experience in fast-paced environments through my work as a Production Team Member at McDonald's. This experience has honed my problem-solving skills, adaptability, and ability to work collaboratively within a team.",
    "I am currently taking the Harvard CS50x course, which is expanding my knowledge and skills in computer science. Additionally, I have completed three courses on freeCodeCamp, earning certifications in Responsive Web Design, JavaScript Algorithms and Data Structures, and Python for Data Analysis. You can find the certificates for these courses at the following links:",
    "- [Responsive Web Design Certificate](https://www.freecodecamp.org/certification/dANNexe/responsive-web-design)",
    "- [JavaScript Algorithms and Data Structures Certificate](https://www.freecodecamp.org/certification/dANNexe/javascript-algorithms-and-data-structures)",
    "- [Python for Data Analysis Certificate](https://www.freecodecamp.org/certification/dANNexe/scientific-computing-with-python-v7)",
    "I am eager to contribute my skills and continue developing my technical expertise in a challenging role within your organization. With a passion for project-based work and a drive to succeed, I believe I can make a positive impact.",
]

attachment_paths = ["files/cover_letter.pdf", "files/cv_resume.pdf", "files/fcc_javacert.pdf", "files/fcc_webcert.pdf", "files/fcc_pycert.pdf"]  # Enter the paths to the files to attach

# Send the automated emails
automate_emails(sender_email, sender_password, subject, message, attachment_paths)
