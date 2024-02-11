README.md

Примечания.

1) не входя в детали, желаю отметить потребовавшиеся пакеты:
pip install --upgrade google-api-python-client
pip install oauth2client
pip install google-auth-oauthlib
 * не прокатило pip install fast_bitrix24
pip install bitrix24-rest

1.1)
 * не прокатило pip install flask-mysql // на хостинге в бесплатном варианте доступен только mysql, поэтому mysql
pip install pyyaml
 * не прокатило pip install flask[async]
pip install psycopg2-binary

2) данные собираюсь доставать через входящий "вебхук" для bitrix... С помощью вышеуказанного модуля fast_bitrix24