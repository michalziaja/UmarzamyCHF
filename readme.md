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

3. Services and Technologies:
Form: HTML/JS + API Gateway
Database: Lambda/Python + DynamoDB
