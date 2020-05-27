# Invoice generator

Script to generate invoices in pdf and send by email.

## Installation

Install project dependencies.

```python
pip install -r requirements.txt

```
## Configure script

Rename the `sample.secrets.toml` file to `.secrets.toml`:

```bash
mv sample.secrets.toml .secrets.toml
```

Open the `.secrets.toml` file, where you have `EMAIL_PASSWORD` enter the password of the email that will send the invoice.

```
EMAIL_PASSWORD = "my_password"
```

Now open the `settings.toml` file and enter the information: 
- email using to send the invoice, 
- email that will receive the invoice, 
- served SMTP, 
- SMTP server port, 
- name of the file that will be generated the invoice, 
- number of days worked and the amount to be received.

```
SENDER_EMAIL = "send_test@test.com"
RECIEVER_EMAIL = "reciever_test@test.com"
NAME_SMTP = "smtp.test.com"
PORT = 465
FILE = "my_invoice.pdf"
DAYS_WORKED= 30
PAYMENT = "3000BRL"
```

## Changing the PDF message and email    

Open the file `/utility/message.py`. It has three variables:

- `body_pdf`: Where will you put the text that goes in the generated pdf. Here are two important things. Field markings: **Pay period** and **Payment**. In the pay period fields you cannot delete the mark `{} - {}`, because going to that location will receive the dates. The **"Pay Period"** name you can change. The same rule applies to the field **Payment**.

- `subject`: Email title.
- `body_email`: Body text of the email to be sent.