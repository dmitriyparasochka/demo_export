import json

from database import Database
from excel import Excel
from salesforceConnector import SalesforceConnector

def lambda_handler(event, context):
    records = Database.get_records()
    excel_file = Excel.create_file(records)
    SalesforceConnector.upload_file(excel_file)

    return {
      "statusCode": 200
    }