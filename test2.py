from pprint import pprint
from bitrix24 import *

webhook = "https://b24-onzqts.bitrix24.ru/rest/1/glt6iy0bi3ihay6s/"
bx24 = Bitrix24(webhook)

pprint(bx24.callMethod('crm.deal.list'))