import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsConnector:
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            'credentials/service_account.json', self.scope
        )
        self.client = gspread.authorize(self.creds)
    
    def get_sensor_data(self, sheet_id='1fXL0wIxqeHEehuy_NoCpjVjjcvnJNnJk9xULSdZjbKo'):
        sheet = self.client.open_by_key(sheet_id)
        worksheet = sheet.worksheet('ProcessedData')
        return worksheet.get_all_records()
