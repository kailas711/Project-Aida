# log in 
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup

# Account details 


# setup Imap server and authenticate using SSL 
imap_server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username,password)

# setup configs 
status , messages = imap.select("INBOX")
# number of top emails to be fetched 
N=3
messages = int(messages[0])
  
def parser_function(body):
    extracted_mails = []
    i=0
    for mail in body:
        Parser = BeautifulSoup(mail, 'html.parser')
        text_extracted = Parser.get_text().strip()[:500]
        extracted_mails.append(f"{i}.  " + text_extracted)
        i+=1
    return extracted_mails


def get_mail_content():

    email_contents = []
    metadata = {}
    for i in range(messages, messages-N, -1):
        # fetch emails by ID 
        res, msg = imap.fetch(str(i),"(RFC822)")
        
        for response in msg:
            if isinstance(response,tuple):

                # parse a bytes email into a message object, it will be encoded
                msg = email.message_from_bytes(response[1])
                
                # decode the mail 
                subject, encoding = decode_header(msg["Subject"])[0]

                # if subject is an instance then decode. 
                # if isinstance(subject, bytes):
                #     subject = subject.decode(encoding)

                # decode email sender 
                sender , encoding = decode_header(msg.get("From"))[0]

                # same if the sender is encoded 
                if isinstance(sender, bytes):
                    sender = sender.decode(encoding)
                
                # if the email is multipart , iterate over the mail.
                if msg.is_multipart():
                    for parts in msg.walk():
                        
                        # extract content type from email.
                        content_type = parts.get_content_type()
                        content_disposition = str(parts.get("Content-Disposition"))
                        
                    # try to extract the body 
                        try:
                            body = parts.get_payload(decode=True).decode()
                          
                            # add to the list 
                            email_contents.append(body)

                        except:
                            pass  
                                    
                # if the msg is not of mutlipart 
                else:
                    content_type = msg.get_content_type()
                    # get mail body 
                    body = msg.get_payload(decode=True).decode()
                    if body not in email_contents:
                        email_contents.append(body)
                metadata[sender] = subject 

    email_contents = parser_function(email_contents)

    return email_contents, metadata

def logout():
    # close and logout from imap server 
    imap.close()
    imap.logout()