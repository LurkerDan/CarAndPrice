from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleSheet:
    def google_request(self, body_request):
        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SAMPLE_SPREADSHEET_ID = '1sdY_ZW84oyITDcF1TqtCl6M8urR1JCLlN3cgNROs5ww'
        creds = None
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='list1!A1',
                                        valueInputOption='USER_ENTERED',
                                        body={'values': body_request}).execute()
        return request
