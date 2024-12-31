import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the required scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Provide the correct path to your creds.json
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# Authorize and create the client
client = gspread.authorize(creds)

# Open the spreadsheet (make sure the name matches)
sheet = client.open("google sheet").sheet1

# Get all records (returns a list of dictionaries)
data = sheet.get_all_records()
# print(data)


row = sheet.row_values(3)
# print(row)


col = sheet.col_values(6)
# print(col)

cell = sheet.cell(1,3).value
# print(cell)


cell = sheet.cell(2,3).value
# print(cell)


cell = sheet.cell(10,1).value
# print(cell)


insertrow = ['1234','avikin','13','14','Male','100%','4.2']
sheet.insert_row(insertrow,17)
# print("the row has been added")


sheet.delete_rows(5)
print("the row is deleted")