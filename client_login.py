import requests
from xml.etree import ElementTree as ET

# Define the WSDL URL and the endpoint URL
wsdl_url = "http://10.129.110.171:3002/wsdl?wsdl"
endpoint_url = "http://10.129.110.171:3002/wsdl"

# Create a SOAP request payload for the Login operation
soap_request = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://tempuri.org/">
  <soap:Body>
    <tns:LoginRequest>
      <username>admin</username>
      <password>your_password</password>  <!-- Replace with the actual password -->
    </tns:LoginRequest>
  </soap:Body>
</soap:Envelope>
"""

# Define the headers for the SOAP request
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "Login",  # SOAP action for the Login operation
}

# Send the SOAP request to the endpoint URL
response = requests.post(endpoint_url, data=soap_request, headers=headers)

# Check the response status
if response.status_code == 200:
    # Parse the SOAP response
    root = ET.fromstring(response.content)
    result = root.find(".//tns:result").text
    if result == "Login Successful":
        print("Login Successful")
    else:
        print("Login Failed")
else:
    print("HTTP request failed with status code:", response.status_code)
