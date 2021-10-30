This is a Python client library for generating emails and getting email box messages based on using [1secmail](https://www.1secmail.com/api/) API.
### Installation
use pip:

``pip install secmail``
### Usage
```py
import secmail

sec = secmail.SecMail()
email = sec.generate_email(count=1)
print(email)
```
If you set the count the more than 1 it will return a list of email
