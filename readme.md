The project will include the creation of simple website for people who have loans for the purchase of real estate, settled in CHF.

In short.
The user will be able to check whether his contract with the bank contains prohibited clauses that will enable him to win in court and write off the loan.

As I currently spend most of my time learning and working in the AWS environment, I will try to use as much of the services available there as possible - even if they are not the best financially or effective.


My plan:

Homepage
	Contact form:
		Each contact will be saved with a sequential number in the database.
		A message with a thank you note will be sent to the provided email address.
		An email notification about a new entry will be sent to the administrator's email address.
	 Contract verification:
		A PDF file attached on the website will be scanned for prohibited clauses.
		If the searched text fragment is found, a notification will be displayed, confirmed with a message, and logged in the database.

Services and Technologies:

	Form: HTML/JS + API Gateway
	Database: Lambda/Python + DynamoDB
	Email delivery: Lambda/Python + SNS Topic
		AWS allows sending messages only to subscribers (the administrator) by default, so the message for the user will be sent using Python.
	File attachments: API + S3 - I would like the file to be transferred to an S3 bucket 	with a predefined name, e.g., "file.pdf."
	File verification: Lambda/Python - the file will be searched for specified records, 	and after displaying the result, it will be deleted.