import os
import base64
import re
import json
import email
import mimetypes
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the SCOPES for Gmail API access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Authenticate and connect to Gmail API
def authenticate_gmail():
    creds = None
    # Load existing credentials if available
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If no credentials are available, ask for authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

# Search Gmail for emails with attachments that contain 'invoice' in the filename
def search_invoices(service):
    query = 'has:attachment filename:invoice.pdf'  # Looks for attachments with "invoice" in the filename
    results = service.users().messages().list(userId='me', q=query).execute()

    messages = results.get('messages', [])
    return messages

# Download invoice PDFs from emails
def download_invoices(service, messages, save_folder='Invoices'):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for msg in messages:
        msg_id = msg['id']
        message = service.users().messages().get(userId='me', id=msg_id).execute()

        for part in message['payload'].get('parts', []):
            if part['filename'] and 'invoice' in part['filename'].lower() and part['filename'].lower().endswith('.pdf'):
                attachment_id = part['body']['attachmentId']
                attachment = service.users().messages().attachments().get(
                    userId='me', messageId=msg_id, id=attachment_id).execute()

                file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                file_path = os.path.join(save_folder, part['filename'])

                with open(file_path, 'wb') as f:
                    f.write(file_data)
                print(f"Downloaded: {part['filename']}")

# Main function to execute the script
def main():
    service = authenticate_gmail()
    messages = search_invoices(service)

    if not messages:
        print("No invoices found.")
    else:
        print(f"Found {len(messages)} invoice emails. Downloading PDFs...")
        download_invoices(service, messages)
        print("All invoices downloaded successfully.")

if __name__ == '__main__':
    main()


# 
# pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# python download_invoices.py
# 