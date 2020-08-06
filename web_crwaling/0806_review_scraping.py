import requests
from bs4 import BeautifulSoup

response = requests.get('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(response.text, 'html.parser')

movies_list = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li')

final_movie_data = []

for movie in movies_list:
    a_tag = movie.select_one('dl > dt > a')

    movie_title = a_tag.contents[0]
    movie_code = a_tag['href'].split('code=')[1]

    movie_data = {
        'title': movie_title,
        'code': movie_code
    }

    final_movie_data.append(movie_data)

#print(final_movie_data)


headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=188909',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=AVT2EGRQCUAF6; ASID=dc5f2a110000017342585abc0000004b; NRTK=ag^#all_gr^#4_ma^#2_si^#2_en^#2_sp^#2; NaverSuggestUse=use^%^26unuse; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.1.1931894410.1595229296; _ga_7VKFYR6RV1=GS1.1.1596179180.4.1.1596179183.57; JSESSIONID=79C1C2AEEB5DD0296D04D38181773E2F; nid_inf=-1521211186; NID_JKL=h4H7abAB+HT4ZStodPMtTnqmbfeZ9+TQJOZZEqSBThw=; nx_ssl=2; BMR=; page_uid=UyWGcsp0JXVssf9KFF8sssssthd-327236; csrf_token=d8c81082-cb04-4ec8-932c-6bbf97532e0f',
}

params = (
        ('code', 188909),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://movie.naver.com/movie/bi/mi/review.nhn?code=188909', headers=headers)


response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
review_soup=BeautifulSoup(response.text,'html.parser')
review_data=review_soup.select('body > div > div > div.score_result > ul > li')


#print(review_data)

num=0
for review in review_data:
    star=review.select_one('div.star_score > em').text
    try:
        reply = review.select_one(f'div.score_reple > p > span#_filtered_ment_{num} > span > a')['data-src']
      
    except:
        reply = review.select_one(f'div.score_reple > p > span#_filtered_ment_{num}').text.strip()
    
    num+=1

    print(star,reply)
