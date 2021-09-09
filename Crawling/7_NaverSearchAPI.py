"""
날짜 : 2021/09/02
이름 : 박시현
내용 : 네이버 Open API를 활용한 크롤링
"""

import datetime, json
import urllib.request

client_id = 'sPEbsiUpUORoWNKR4lYy'
client_secret = 'pwilDRpM8x'

def getRequestUrl(url):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(request)

        if response.getcode() == 200:   #성공
            print('[%s] Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e:
        print(e)
        print('[%s] Error for Url : %s' % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, start, display): #아래 주소들 조립해서 요청 후 json 으로 리턴
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt,
                       'title':title,
                       'description':description,
                       'org_link':org_link,
                       'link':link,
                       'pDate':pDate})
    return

def main():
    node = 'news'

    srcText = input('검색어 입력 : ')
    cnt = 0
    jsonResult = []
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse['total']

    while jsonResponse != None and jsonResponse['display'] != 0:

        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)

    print('전체 검색 건수 : %d' % total)

    # 검색결과 파일생성 json으로 : with open 함수
    with open('./%s_naver_%s.json' % (srcText, node), mode='w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)

    print('가져온 데이터 : %d건' % cnt)
    print('%s_naver_%s.json 파일 생성완료...' % (srcText, node))



if __name__=='__main__':
    main()


