# UmarzamyCHF
The project will include the creation of simple website for people who have loans for the purchase of real estate, settled in CHF.

In short.
The user will be able to check whether his contract with the bank contains prohibited clauses that will enable him to win in court and write off the loan.

As I currently spend most of my time learning and working in the AWS environment, I will try to use as much of the services available there as possible - even if they are not the best financially or effective.


My plan:

1. Contact form:
Each contact will be saved with a sequential number in the database.
A message with a thank you note will be sent to the provided email address.
An email notification about a new entry will be sent to the administrator's email address.

2. Contract verification:
A PDF file attached on the website will be scanned for prohibited clauses.
If the searched text fragment is found, a notification will be displayed,
confirmed with a message, and logged in the database.

3. Services and Technologies

Form: HTML/JS + API Gateway

Database: Lambda/Python + DynamoDB
  
Email delivery: Lambda/Python + SNS Topic
  AWS allows sending messages only to subscribers (the administrator) by default, so the message for the user will be sent using Python.
  
File attachments: API + S3 - I would like the file to be transferred to an S3 bucket 	with a predefined name, e.g., "file.pdf."

File verification: Lambda/Python - the file will be searched for specified records, 	and after displaying the result, it will be deleted.

EDIT: 
What i have already?
Contact form works and Lambda correctly save data into DynamoDB

Emails are send from my gmail accout -> i will set up SNS leater

PROBLEMS FOR NOW:
1. I stuck on uploading file to S3 by API - i have CORS error..
2. I made simple text search code in python, but when i try use pharse from text.txt file, code is searching only from one line.

EDIT: 
1. Foud solution how to upload file to s3. Insted of ulopad directly PUT method by API REST i use presignURL and HTTP API
https://aws.amazon.com/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/
2. I add layer to my lambda function, so i can use PyPDF2 libraly to search PDF file. 

