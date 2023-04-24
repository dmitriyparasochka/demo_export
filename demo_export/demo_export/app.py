import base64
import json

from database import Database
from excel import Excel
from salesforceConnector import SalesforceConnector

def lambda_handler(event, context):
    records = Database.get_records()
    excel_file = Excel.create_file(records)
    # SalesforceConnector.upload_file(excel_file) ??? TODO

    base64_data = base64.b64encode(excel_file).decode()
    return {
        'statusCode': 200,
        'body': json.dumps({'file': base64_data})
    }