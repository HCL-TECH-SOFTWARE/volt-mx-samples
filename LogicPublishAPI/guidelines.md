Below are the steps to run this sample

1. Install node js runtime 6.2.2 or above

2. Download zip file and extract

3. Install npm modules dependencies for the sample package

> npm install

4. Run the sample app

> node bin/www

5. Application will start on 9000 port

6. Access APIs with below prefix url

URL : http://localhost:9000/services/mailapp/api/v1/contact

Methods : GET/POST/PUT/DELETE

Payload : 

{
	"firstName" : "Test",
	"lastName" : "User",
	"mobileNumber" : "1234567890",
	"emailId" : "admin@voltmx.com"
} 
