import smtplib
import email.message

def enviar_email():
  corp_email = "Testando email"


  msg = email.message.Message();
  msg['Subject'] = 'TESTE'
  msg['From'] = 'miichaels23@gmail.com'
  msg['to'] = 'fh.brocco@gmail.com'
  password = 'iyaigdsspzfudtjt'
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corp_email )

  s = smtplib.SMTP("smtp.gmail.com: 587")
  s.starttls()

  #login Credentials for seting the email
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('uft-8'))
  print('Email enviado');

enviar_email()
  