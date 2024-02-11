README.md

Примечания.

1) не входя в детали, желаю отметить потребовавшиеся пакеты:
pip install --upgrade google-api-python-client
pip install oauth2client
pip install google-auth-oauthlib
pip install fast_bitrix24 * не прокатило
pip install bitrix24-rest

1.1)
pip install flask-mysql // на хостинге в бесплатном варианте доступен только mysql, поэтому mysql
pip install pyyaml
pip install flask[async] 

2) данные собираюсь доставать через входящий "вебхук" для bitrix... С помощью вышеуказанного модуля fast_bitrix24