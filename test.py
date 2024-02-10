# from fast_bitrix24 import Bitrix

# # замените на ваш вебхук для доступа к Bitrix24
# webhook = "https://b24-onzqts.bitrix24.ru/rest/1/glt6iy0bi3ihay6s/"
# b = Bitrix(webhook)
# # список сделок в работе, включая пользовательские поля
# # deals = b.get_all(
# #     'crm.deal.list',
# #     params={
# #         'select': ['*', 'UF_*'],
# #         'filter': {'CLOSED': 'N'}
# # })

# # contacts = b.get_by_ID(
# # 'crm.deal.contact.items.get',
# # [d['ID'] for d in deals])

# # contact = b.get_by_ID('crm.deal.contact.fields', '20')
# # contact = b.get_by_ID('crm.deal.contact.fields')
# # contact = b.get_all('crm.contact.list')

# # cc = b.get_all(
# #     'crm.contact.list',
# #     params={
# #         'select': ['*', 'PHONE']
# # })

# # print(deals)
# # print()
# # print(contacts)
# # print()
# print(cc)

import yaml

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '181483331264'
# app.config['MYSQL_DATABASE_DB'] = 'mysql'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db_config = [
    {
        'Details': {
        'MYSQL_DATABASE_USER' : 'root',
        'MYSQL_DATABASE_PASSWORD': '181483331264',
        'MYSQL_DATABASE_DB' : 'mysql',
        'MYSQL_DATABASE_HOST': 'localhost',
        }
    }
]

with open("db_config.yaml", 'w') as yamlfile:
    data = yaml.dump(db_config, yamlfile)
    print("Write successful")

with open("db_config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")

print(data)
print(data[0]['Details']['MYSQL_DATABASE_USER'])