
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify


import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

cache = {}

from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
# my_file = THIS_FOLDER / 'credentials.json'

CREDENTIALS_FILE = THIS_FOLDER / 'credentials.json'

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе

service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 

spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                            'sheetId': 0,
                            'title': 'Лист номер один',
                            'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
}).execute()

spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла

driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'savva.voloshin@gmail.com'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()

results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": "Лист номер один!B2:D5",
            "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
            "values": [
                        ["Ячейка B2", "Ячейка C2", "Ячейка D2"], # Заполняем первую строку
                        ['25', "=6*6", "=sin(3,14/2)"],
                    ]}
        ]
    }).execute()

print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

def myinit():
    global cache
    cache['foo'] = 0

@app.route('/')
def hello_world():

    with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
        f.write('log file should be initialized\n')
    
    return 'Hello from Flask! Mydir: ' + "%s" % THIS_FOLDER

@app.route('/bitrix24', methods=['POST'])
def handle_bitrix24():

    with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
        f.write('handle_bitrix24 \n')

    data=request.json

    with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
        f.write('data should appears below \n')
        f.write(jsonify(data).get_data(as_text=True))


    values = [
        [1,2,3,4,5,6,7,8,9]
    ]
    
    body = {'values': values}

    results = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range="Лист номер один!B2:D5", valueInputOption="RAW", body=body).execute()
    
    return jsonify(data)


if __name__ == '__main__':
    myinit()  # initialize by default
    app.run()