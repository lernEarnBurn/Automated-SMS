def mockSend(firstName, businessName, phoneNumber, approvalAmount):
   message = f"hello {firstName} your business {businessName} has been approved {approvalAmount}"
   return 'sent ' + message + ' to ' + phoneNumber


def formatPhoneNum(num):
   return