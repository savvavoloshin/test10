
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
from pprint import pprint 

import aiohttp
import asyncio

import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from flaskext.mysql import MySQL

from fast_bitrix24 import BitrixAsync

import yaml

from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()

app = Flask(__name__)

with open(THIS_FOLDER / "db_config.yaml", "r") as yamlfile:
    cdata = yaml.load(yamlfile, Loader=yaml.FullLoader)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = cdata[0]['Details']['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = cdata[0]['Details']['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = cdata[0]['Details']['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = cdata[0]['Details']['MYSQL_DATABASE_HOST']
mysql.init_app(app)

app = Flask(__name__)

cache = {}

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

# driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
# access = driveService.permissions().create(
#     fileId = spreadsheetId,
#     body = {'type': 'user', 'role': 'writer', 'emailAddress': 'savva.voloshin@gmail.com'},  # Открываем доступ на редактирование
#     fields = 'id'
# ).execute()

# results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
#         "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
#         "data": [
#             {"range": "Лист номер один!B2:D5",
#             "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
#             "values": [
#                         ["Ячейка B2", "Ячейка C2", "Ячейка D2"], # Заполняем первую строку
#                         ['25', "=6*6", "=sin(3,14/2)"],
#                     ]}
#         ]
#     }).execute()

# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId

@app.route('/')
def hello_world():

    with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
        pprint('log file should be initialized', f)
    
    conn = mysql.connect()
    cursor =conn.cursor()

    create_table_stmt = """
CREATE TABLE IF NOT EXISTS `tblsample` (

  `id` int(11) NOT NULL auto_increment, 
  `name1` varchar(100) NOT NULL default '',
  `name2` varchar(100) NOT NULL default '',
  `phone` varchar(100) NOT NULL default '',
  `comments` varchar(100) NOT NULL default '',
   PRIMARY KEY  (`id`)
);
"""

    cursor.execute(create_table_stmt)
    data = cursor.fetchone()

    insert_some_values_stmt = "INSERT INTO tblsample (name1, name2, phone, comments) VALUES (%s, %s, %s, %s)"
    values = ("John", "Highway", "+7 960 257 8295", "no comments")
    cursor.execute(insert_some_values_stmt, values)

    conn.commit()
    
    return 'Hello from Flask! Mydir: ' + "%s" % THIS_FOLDER + "%s " % str(data)

@app.route('/bitrix24', methods=['POST'])
async def handle_bitrix24():

    # data=request.json

    deal_id = ''
    try:
        deal_id = request.form['data[FIELDS][ID]']
    except:
        try:
            deal_id = request.form['param1']
        except:
            deal_id = ''

    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as client:
        webhook = "https://b24-onzqts.bitrix24.ru/rest/1/glt6iy0bi3ihay6s/"
        b = BitrixAsync(webhook, client=client)

        deal = await b.get_all(
            'crm.deal.list',
            params={
                'select': ['ID', 'CONTACT_ID', 'COMMENTS'],
                'filter': {'ID': deal_id}
        })

        if len(deal) > 0:
            comments = deal[0]['COMMENTS']
            contact_id = deal[0]['CONTACT_ID']

            contact = await b.get_all(
                'crm.contact.list',
                params={
                    'select': ['LAST_NAME', 'NAME', 'PHONE',],
                    'filter': {'ID': '2'}
            })

            name1 = contact[0]['LAST_NAME']
            name2 = contact[0]['NAME']
            phone = contact[0]['PHONE'][0]['VALUE']

            with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
                pprint('handle_bitrix24', f)
                pprint(request.form, f)
        else:
            with open(THIS_FOLDER / 'tmp.log', 'a+') as f:
                pprint('cant handle_bitrix24', f)

    values = [
        [1,2,3,4,5,6,7,8,9]
    ]
    
    body = {'values': values}

    # results = service.spreadsheets().values().append(
    #     spreadsheetId=spreadsheetId,
    #     range="Лист номер один!B2:D5",
    #     valueInputOption="RAW", body=body).execute()
    
    return jsonify({"code":200})


if __name__ == '__main__':
    app.run()