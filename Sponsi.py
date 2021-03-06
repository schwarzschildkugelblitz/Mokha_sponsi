import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "moksha@nsut.ac.in"
receiver_email = "contactharshitbatra@gmail.com"
password = "Moksha@2021"

message = MIMEMultipart("alternative")
message["Subject"] = "Sponsorship Proposal for Moksha - Innovision 2022"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<html>

<body>
    Respected Sir/Madam,
    <br>
    <br>

    Netaji Subhas University of Technology (erstwhile NSIT), Delhi, which was founded in 1983 as Delhi Institute of
    Technology (DIT) which is spread over an area of 145 acres and has a 20,000+ strong community of students and alumni
    connected through a global network, is holding its Annual Cultural Fest Moksha from March 24-26, 2022.
    <br>
    <br>

    <b>About Moksha</b>
    <br>

    Moksha, Netaji Subhas University of Technology's (NSUT) (previously NSIT, University of Delhi) annual cultural
    festival, began in 2003. It is a three-day national cultural event hosted at NSUT during the month of March. Moksha
    brings together colleges from all around India, making it one of North India's greatest college festivals. In recent
    years, Moksha has seen large attendance and involvement in a variety of events and competitions that have been
    reported by both print and internet media. Participants range from Delhi University colleges to other IITs in the
    multitude of events held.
    <br>
    Over the course of three days, Moksha sees an average of over 50,000 students. <b>Shaan, Edward Maya, Akcent, The
        Indian Ocean, Salim–Sulaiman, Monali Thakur, Kailash Kher, Mohit Chauhan, Nucleya, Bohemia, Sunburn Campus,
        Tomorrowland's DJs,</b> and many more exotic artists have performed at the festival.
    <br>
    <br>


    <b>About Innovision</b>
    <br>


    The NSUT technical festival is well-known in the Indian technical festival circuit for receiving unprecedented
    amounts of print and electronic media coverage. Due to the success of past incarnations, the idea was expanded to
    include not only technology but also managerial activities, resulting in a footfall of over 50,000 students.

    Innovision has been acclaimed as one of the top festivals in the Delhi circuit for gaining exposure and penetration
    among the youthful generation from our country's premier educational institutions, such as IIT Delhi, IIT Mumbai,
    IIT Roorkee, IIIT Hyderabad, IIIT Delhi, and Delhi Technological University (erstwhile DCE).
    <br>
    Please check the <a href="https://en.wikipedia.org/wiki/Moksha_%28festival%29">Wikipedia page</a> for more info
    about Moksha and the attached link of the brochure.
    <br>
    <b>Tentative Headliners for Moksha - Innovision 2022</b>
    <br>
    1. Felicity (DJ Night): <b>Ritviz</b>
    <br>
    2. Pop Night (Band Night): <b>Anuv Jain</b>
    <br>
    3. Humour Fest: <b>Anubhav Singh Bassi, Harsh Gujral</b>
    <br>
    4. Fahrenite (Bollywood Night): <b>B Praak</b>
    <br>


    Looking forward to an opportunity to discuss a formal proposal enlisting the deliverables with your esteemed firm.
    <br>
    Warm Regards,
    <br>
    Manasvi Jain
    <br>
    Sponsorship Head– Team Moksha
    <br>
    (+919910522576)
    <br>
    <br>
    <br>
    <br>
    Moksha'19 Aftermovie Link:
    <br>
    <a href="https://drive.google.com/file/d/1JqoKLBJ9KN7Q3eJz4mfHD12N3Tg198uu/view?usp=sharing">https://drive.google.com/file/d/1JqoKLBJ9KN7Q3eJz4mfHD12N3Tg198uu/view?usp=sharing</a>
    <br>
    <br>
    Moksha’22 Brochure Link:
    <br>
    <a href=" https://drive.google.com/file/d/1vyGmOQI-BdRt3VGa-RLOCQojIC9284xc/view?usp=sharing">https://drive.google.com/file/d/1vyGmOQI-BdRt3VGa-RLOCQojIC9284xc/view?usp=sharing</a>
    <br>
    <br>
    Moksha’22 Sponsorship Matrix:
    <br>
    <a href="https://drive.google.com/file/d/15W-8NG_Qvpl0wh2uQ1YXt1KqjBZQrhYH/view?usp=sharing">https://drive.google.com/file/d/15W-8NG_Qvpl0wh2uQ1YXt1KqjBZQrhYH/view?usp=sharing</a>
</body>

</html>
"""
part2 = MIMEText(html, "html")

message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())