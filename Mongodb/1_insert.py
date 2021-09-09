"""
날짜 : 2021/09/07
이름 : 박시현
내용 : 파이썬 MongoDB Insert 실습하기
"""

from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계- mongodb 접속
conn = mongo('mongodb://maro:1234@192.168.56.101:27017')

# 2단계 - DB 선택
db = conn.get_database('maro')

# 3단계 - Collection(테이블) 선택
collection = db.get_collection('Member')

# 4단계 - 쿼리실행
collection.insert_one({'uid': 'a101',
                       'name': '김유신',
                       'hp':'010-1234-1001',
                       'pos':'사원',
                       'dep':101,
                       'rdate':datetime.now()})

collection.insert_one({'uid':'a109',
                       'name':'김순수',
                       'hp':'010-5648-5638',
                       'dep':102})

# 5단계 - MongoDB 종료
conn.close()

print('Insert 완료...')
