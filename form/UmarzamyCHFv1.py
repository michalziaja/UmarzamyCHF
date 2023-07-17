import json
import smtplib
from email.mime.text import MIMEText
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('baza_chf')

def send_email(sender, recipient, subject, message):
  
    # SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'michalziaja88'
    smtp_password = 'xxxxxxxxxxx'

        
    # Create email
    msg = MIMEText(message)
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

      
    # Send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, msg.as_string())
        print('Wiadomość e-mail została wysłana.')
    except Exception as e:
        print('Wystąpił błąd podczas wysyłania wiadomości e-mail:', str(e))
        raise

def lambda_handler(event, context):
    
    response = table.scan()

    items = response['Items']
    items.sort(key=lambda x: int(x['id']), reverse=True)
    
    if items:
        last_id = int(items[0]['id'])
        current_id = last_id + 1
    else:
        current_id = 1

    
    imie = str(event["imie"])
    nazwisko = str(event["nazwisko"])
    telefon = str(event["telefon"])
    email = str(event["email"])
    przedrostek = str(event['przedrostek'])
    
   
    # Save data in DynamoDB
    response = table.put_item(
        Item={
            'id': int(current_id),
            '1': przedrostek,
            '2_imie': imie,
            '3_nazwisko': nazwisko,
            '4_telefon': telefon,
            '5_email': email
        }
    )

    # Check
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        message = 'Dane zapisane. ID formularza: ' + str(current_id)
    else:
        message = 'Wystąpił błąd podczas zapisywania danych'


    # Send email to user
    subject_user = 'Potwierdzenie wysłania formularza'
    message_user = 'Dziękujemy za wysłanie formularza.'

    sender = 'michalziaja88@gmail.com' 
    recipient = email

    try:
        send_email(sender, recipient, subject_user, message_user)


        # Send email to administrator
        subject_admin = 'Nowe dane z formularza'
        message_admin = f'Otrzymano nowe dane z formularza:\n\n' \
                        f'Przedrostek: {przedrostek}\n' \
                        f'Imię: {imie}\n' \
                        f'Nazwisko: {nazwisko}\n' \
                        f'Email: {email}\n' \
                        f'Telefon: {telefon}'

        recipient_admin = 'michalziaja88@gmail.com'  
        send_email(sender, recipient_admin, subject_admin, message_admin)


        # Response to API
        response = {
            'statusCode': 200,
            'body': json.dumps(message)
        }
        return response
    except Exception as e:
        print('Wystąpił błąd:', str(e))
        
        
        # Response with error
        response = {
            'statusCode': 500,
            'body': json.dumps('Wystąpił błąd. Spróbuj ponownie.')
        }
        return response
