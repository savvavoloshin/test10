from pprint import pprint 
from fast_bitrix24 import Bitrix

# замените на ваш вебхук для доступа к Bitrix24
webhook = "https://b24-onzqts.bitrix24.ru/rest/1/glt6iy0bi3ihay6s/"
b = Bitrix(webhook)
# список сделок в работе, включая пользовательские поля
deal_id = '14'
deal = b.get_all(
    'crm.deal.list',
    params={
        'select': ['ID', 'CONTACT_ID', 'COMMENTS'],
        'filter': {'ID': deal_id}
})

# pprint(deal)
comments = deal[0]['COMMENTS']
contact_id = deal[0]['CONTACT_ID']

contact = b.get_all(
    'crm.contact.list',
    params={
        'select': ['LAST_NAME', 'NAME', 'PHONE',],
        'filter': {'ID': '2'}
})

name1 = contact[0]['LAST_NAME']
name2 = contact[0]['NAME']
phone = contact[0]['PHONE'][0]['VALUE']

# pprint(contact)

pprint([comments,phone,name1,name2])

# contacts = b.get_by_ID(
# 'crm.deal.contact.items.get',
# [d['ID'] for d in deals])

# contact = b.get_by_ID('crm.deal.contact.fields', '20')
# contact = b.get_by_ID('crm.deal.contact.fields')
# contact = b.get_all('crm.contact.list')

# cc = b.get_all(
#     'crm.contact.list',
#     params={
#         'select': ['*', 'PHONE']
# })

# print(deals)
# print()
# print(contacts)
# print()
# pprint(deal)

# import yaml

# db_config = [
#     {
#         'Details': {
#         'MYSQL_DATABASE_USER' : 'root',
#         'MYSQL_DATABASE_PASSWORD': '181483331264',
#         'MYSQL_DATABASE_DB' : 'mysql',
#         'MYSQL_DATABASE_HOST': 'localhost',
#         }
#     }
# ]

# with open("db_config.yaml", 'w') as yamlfile:
#     data = yaml.dump(db_config, yamlfile)
#     print("Write successful")

# with open("db_config.yaml", "r") as yamlfile:
#     data = yaml.load(yamlfile, Loader=yaml.FullLoader)
#     print("Read successful")