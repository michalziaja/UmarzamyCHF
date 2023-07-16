import boto3
import PyPDF2
import io
import re

def normalize_text(text):
   
    return re.sub(r'\s+', ' ', text).strip()

def search_pdf_for_phrase(pdf_data, phrase):
    pdf_reader = PyPDF2.PdfReader(pdf_data)
    num_pages = len(pdf_reader.pages)

    normalized_phrase = normalize_text(phrase)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = normalize_text(page.extract_text())

        if normalized_phrase in text:
            return True  

    return False  

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'umarzamyuploads3-s3uploadbucket-r8j533eoxlz4'
    pdf_key = 'test.pdf'
    search_phrase = """Wysokość zobowiązania będzie ustalana jako równowartość wymaganej
                        spłaty wyrażonej w CHF – po jej przeliczeniu według kursu sprzedaży walut
                        określonego w „Bankowej tabeli kursów walut dla kredytów dewizowych
                        oraz indeksowanych kursem walut obcych” do CHF obowiązującego w dniu
                        spłaty."""

    try:
        response = s3.get_object(Bucket=bucket_name, Key=pdf_key)
        pdf_data = response['Body'].read()

        pdf_stream = io.BytesIO(pdf_data)

        if search_pdf_for_phrase(pdf_stream, search_phrase):
            print(f"Fraza '{search_phrase}' została znaleziona w pliku PDF.")
            result = "Klauzula abuzywna znaleziona."
        else:
            print(f"Fraza '{search_phrase}' nie została znaleziona w pliku PDF.")
            result = "Nie znaleziono."

        print("Status: ok")

    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")
        result = "Wystąpił błąd."

    return {
        'statusCode': 200,
        'body': result
    }
