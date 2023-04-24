import xlsxwriter
from io import BytesIO

class Excel:
    def create_file(records):
      output = BytesIO()
      workbook = xlsxwriter.Workbook(output, {'in_memory': True})

      worksheet = workbook.add_worksheet("Account")
      worksheet.write(0, 0, "Accounts")

      for index, record in enumerate(records):
        if index == 0:
          for findex, field in enumerate(record.keys()):
            worksheet.write(1, findex, field)

        for findex, field in enumerate(record.keys()):
          worksheet.write(index+2, findex, records[index][field])

      workbook.close()
      excel_data = output.getvalue()
      return excel_data