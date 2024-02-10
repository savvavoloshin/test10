from fast_bitrix24 import Bitrix

# замените на ваш вебхук для доступа к Bitrix24
webhook = "https://b24-onzqts.bitrix24.ru/rest/1/glt6iy0bi3ihay6s/"
b = Bitrix(webhook)
# список сделок в работе, включая пользовательские поля
# deals = b.get_all(
#     'crm.deal.list',
#     params={
#         'select': ['*', 'UF_*'],
#         'filter': {'CLOSED': 'N'}
# })

# contacts = b.get_by_ID(
# 'crm.deal.contact.items.get',
# [d['ID'] for d in deals])

# contact = b.get_by_ID('crm.deal.contact.fields', '20')
# contact = b.get_by_ID('crm.deal.contact.fields')
# contact = b.get_all('crm.contact.list')

cc = b.get_all(
    'crm.contact.list',
    params={
        'select': ['*', 'PHONE']
})

# print(deals)
# print()
# print(contacts)
# print()
print(cc)