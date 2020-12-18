from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

import requests


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn import neighbors
from sqlalchemy import create_engine

# Create your views here.

# 데이터 불러오는 작업
# engine = create_engine('mysql+pymysql://root:1234@localhost/testdb', convert_unicode=True)
# conn = engine.connect()
# library_book_df = pd.read_sql_table('booklovers_librarybook', conn)


def index(request) :
    return render(request, 'index.html')


# ---------- 카테고리 ----------
def category(request) :
    return render(request, 'category.html')


# 연령, 성별, 장르 별 조건을 이용한 데이터 불러오기
def category_info(request) :
    age = request.POST['ageType']
    genre = request.POST['genreType']
    gender = request.POST['genderType']

    if age == '0' :
        to_age = '13'
    elif age == '14' :
        to_age = '19'
    elif age == '20' :
        to_age = '59'
    else :
        to_age = '100'

    api_key = '2de07acdbc8edb45815b0788321c701a3d0881ebcdc8952f7c41c3f7f958a10c'

    start_url = 'http://data4library.kr/api/loanItemSrch?authKey='
    gender_url = '&startDt=2020-01-01&endDt=2020-10-31&gender='
    from_age_url = '&from_age='
    to_age_url = '&to_age='
    kdc_url = '&kdc='
    rest_url = '&pageNo=1&pageSize=5&format=json'

    final_url = start_url + api_key + gender_url + gender + from_age_url + age + to_age_url + to_age + kdc_url + genre + rest_url

    response = requests.get(final_url)
    bookInfo_json = response.json()

    data = []

    # 리스트 안에 딕셔너리가 들어가는 형식 생성
    for i in range(len(bookInfo_json['response']['docs'])) :
        data.append(bookInfo_json['response']['docs'][i]['doc'])

    # print(data)

    return JsonResponse(data, safe = False)


# 선택한 책에 대한 상세정보 데이터 불러오기
def book_info(request) :
    isbn = request.POST['isbn']

    api_key = '2de07acdbc8edb45815b0788321c701a3d0881ebcdc8952f7c41c3f7f958a10c'

    start_url = 'http://data4library.kr/api/srchDtlList?authKey='
    isbn_url = '&isbn13='
    rest_url = '&format=json'

    final_url = start_url + api_key + isbn_url + isbn + rest_url

    response = requests.get(final_url)
    bookInfo_json = response.json()

    # print(bookInfo_json)

    data = []
    data.append(bookInfo_json['response']['detail'][0]['book'])
    # print(data)

    return JsonResponse(data, safe = False)


def content_info(request) :
    book_name = request.POST['bookName']


def popularity_info(request) :
    book_name = request.POST['bookName']

    distance, indices = make_bookfeatures(library_book_df)
    data = print_similar_books(book_name, indices, library_book_df)

    return JsonResponse(data, safe = False)


# kNN을 사용한 군집분석
def make_bookfeatures(df) :
    books_features = pd.concat([df['Ratings_Dist'].str.get_dummies(sep = ","), df['average_rating'], df['loan_count'], df['text_reviews_count']], axis=1)

    min_max_scaler = MinMaxScaler()
    books_features = min_max_scaler.fit_transform(books_features)

    model = neighbors.NearestNeighbors(n_neighbors = 6, algorithm = 'ball_tree')
    model.fit(books_features)
    distance, indices = model.kneighbors(books_features)

    return distance, indices


# 도서 이름으로 인덱스 찾기
def get_index_from_name(name, df):
    return df[df["bookname"] == name].index.tolist()[0]


# 내가 검색한 책의 인기도와 유사한 책 5권 추천
def print_similar_books(query, indices, df) :
    data = []

    if query :
        found_id = get_index_from_name(query, df)

        for id in indices[found_id][1:] :
            dict = {}
            dict['bookname'] = df.iloc[id]["bookname"]
            dict['author'] = df.iloc[id]["author"]
            dict['bookImageURL'] = df.iloc[id]["bookImageUrl"]

            data.append(dict)

    return data


# ---------- MBTI ----------
# exam1_mbti = []
# exam2_mbti = []
# exam3_mbti = []
# exam4_mbti = []
# MBTI = []


def mbti(request) :
    exam1_mbti = []
    exam2_mbti = []
    exam3_mbti = []
    exam4_mbti = []

    return render(request, 'mbti.html', {'exam1_mbti': exam1_mbti, 'exam2_mbti': exam2_mbti, 'exam3_mbti': exam3_mbti, 'exam4_mbti': exam4_mbti})


def exam2(request):
    exam1_mbti = []
    exam2_mbti = []
    exam3_mbti = []
    exam4_mbti = []

    exam1_Q1 = request.POST.get('exam1_Q1', False)
    exam1_Q2 = request.POST.get('exam1_Q2', False)
    exam1_Q3 = request.POST.get('exam1_Q3', False)
    # exam1_Q1 = request.POST['exam1_Q1']
    # exam1_Q2 = request.POST['exam1_Q2']
    # exam1_Q3 = request.POST['exam1_Q3']
    E = 0
    I = 0

    if exam1_Q1 == "E":
        E += 1
    else:
        I += 1
    if exam1_Q2 == "E":
        E += 1
    else:
        I += 1
    if exam1_Q3 == "E":
        E += 1
    else:
        I += 1

    if E > I :
        exam1_mbti.append("E")
    else:
        exam1_mbti.append("I")
    print(">>>> ", exam1_Q1, exam1_Q2, exam1_Q3)
    print(E, I)
    print(exam1_mbti, exam2_mbti, exam3_mbti, exam4_mbti)
    return render(request, 'examPage2.html', {'exam1_mbti': exam1_mbti, 'exam2_mbti': exam2_mbti, 'exam3_mbti': exam3_mbti, 'exam4_mbti': exam4_mbti})


def exam3(request):
    exam1_mbti = request.POST.get('exam1_mbti', False)
    exam2_mbti = []
    exam3_mbti = []
    exam4_mbti = []

    exam2_Q1 = request.POST.get('exam2_Q1', False)
    exam2_Q2 = request.POST.get('exam2_Q2', False)
    exam2_Q3 = request.POST.get('exam2_Q3', False)
    # exam2_Q1   = request.POST['exam2_Q1']
    # exam2_Q2   = request.POST['exam2_Q2']
    # exam2_Q3   = request.POST['exam2_Q3']
    S = 0
    N = 0

    if exam2_Q1 == "S":
        S += 1
    else:
        N += 1
    if exam2_Q2 == "S":
        S += 1
    else:
        N += 1
    if exam2_Q3 == "S":
        S += 1
    else:
        N += 1

    if S > N :
        exam2_mbti.append("S")
    else:
        exam2_mbti.append("N")
    print(">>>> ", exam2_Q1, exam2_Q2, exam2_Q3)
    print(S, N)
    print(exam1_mbti, exam2_mbti, exam3_mbti, exam4_mbti)
    return render(request, 'examPage3.html', {'exam1_mbti': exam1_mbti, 'exam2_mbti': exam2_mbti, 'exam3_mbti': exam3_mbti, 'exam4_mbti': exam4_mbti})


def exam4(request):
    exam1_mbti = request.POST.get('exam1_mbti', False)
    exam2_mbti = request.POST.get('exam2_mbti', False)
    exam3_mbti = []
    exam4_mbti = []

    exam3_Q1 = request.POST.get('exam3_Q1', False)
    exam3_Q2 = request.POST.get('exam3_Q2', False)
    exam3_Q3 = request.POST.get('exam3_Q3', False)
    # exam3_Q1 = request.POST['exam3_Q1']
    # exam3_Q2 = request.POST['exam3_Q2']
    # exam3_Q3 = request.POST['exam3_Q3']
    T = 0
    F = 0

    if exam3_Q1 == "T":
        T += 1
    else:
        F += 1
    if exam3_Q2 == "T":
        T += 1
    else:
        F += 1
    if exam3_Q3 == "T":
        T += 1
    else:
        F += 1

    if T > F :
        exam3_mbti.append("T")
    else:
        exam3_mbti.append("F")
    print(">>>> ", exam3_Q1, exam3_Q2, exam3_Q3)
    print(T, F)
    print(exam1_mbti, exam2_mbti, exam3_mbti, exam4_mbti)
    return render(request, 'examPage4.html', {'exam1_mbti': exam1_mbti, 'exam2_mbti': exam2_mbti, 'exam3_mbti': exam3_mbti, 'exam4_mbti': exam4_mbti})


def result(request):
    exam1_mbti = request.POST.get('exam1_mbti', False)
    exam2_mbti = request.POST.get('exam2_mbti', False)
    exam3_mbti = request.POST.get('exam3_mbti', False)
    exam4_mbti = []

    exam4_Q1 = request.POST.get('exam4_Q1', False)
    exam4_Q2 = request.POST.get('exam4_Q2', False)
    exam4_Q3 = request.POST.get('exam4_Q3', False)
    # exam4_Q1 = request.POST['exam4_Q1']
    # exam4_Q2 = request.POST['exam4_Q2']
    # exam4_Q3 = request.POST['exam4_Q3']
    J = 0
    P = 0

    if exam4_Q1 == "J":
        J += 1
    else:
        P += 1
    if exam4_Q2 == "J":
        J += 1
    else:
        P += 1
    if exam4_Q3 == "J":
        J += 1
    else:
        P += 1

    if J > P:
        exam4_mbti.append("J")
    else:
        exam4_mbti.append("P")

    # add_mbti += exam1_mbti + exam2_mbti + exam3_mbti + exam4_mbti
    # mbti = "".join(add_mbti)
    mbti = ""
    mbti += exam1_mbti[2] + exam2_mbti[2] + exam3_mbti[2] + exam4_mbti[0]


    print(">>>> ", exam4_Q1, exam4_Q2, exam4_Q3)
    print(J, P, mbti)
    print(exam1_mbti[2], exam2_mbti[2], exam3_mbti[2], exam4_mbti[0])
    print(exam1_mbti, exam2_mbti, exam3_mbti, exam4_mbti)
    return render(request, 'resultPage.html', {'mbti' : mbti})


def result_ajax(request):
    MBTI = request.POST['MBTI']
    book = pd.read_excel('C:/Users/lby52/data/final/mbti_revise/INTP_book_list_df_revise.xlsx', encoding='utf-8')

    data = []
    for i in range(len(book)) :
        dict = {}

        dict['No'] = str(book.loc[i]['No.'])
        dict['title'] = book.loc[i]['title']
        dict['author'] = book.loc[i]['author']
        dict['publisher'] = book.loc[i]['publisher']
        dict['image'] = book.loc[i]['image']
        data.append(dict)

    return JsonResponse(data, safe = False)


def otherBook(request):
    mbti = request.POST['mbti']
    book = pd.read_excel(f'C:/Users/lby52/data/final/mbti_revise/{mbti}_book_list_df_revise.xlsx', encoding='utf-8')

    data = []
    for i in range(len(book)):
        dict = {}

        dict['No'] = str(book.loc[i]['No.'])
        dict['title'] = book.loc[i]['title']
        dict['author'] = book.loc[i]['author']
        dict['publisher'] = book.loc[i]['publisher']
        dict['image'] = book.loc[i]['image']
        data.append(dict)

    # print(">>>>>>>>>>>>>>>>>>>>>> " , mbti)
    return render(request, 'result_otherBook.html', {'data' : data, 'mbti' : mbti})


# def wordcloud(request) :
#     return render(request, 'wordcloud.html')


# ---------- Healing ----------
def healing(request) :
    return render(request, 'healing.html')


def keyword_info(request) :
    healing_keyword = request.POST['keyword']
    # print(healing_keyword)

    book = HealingBook.objects.all()

    cnt = 0
    score_dict = {}
    healing_keyword_book = []

    # 클릭한 키워드가 들어가있는 도서 리스트 추출
    for i in range(len(book)) :
        if healing_keyword in book[i].keyword :
            healing_keyword_book.append(book[i])
            score_dict[str(cnt)] = float(book[i].positive_score)
            cnt += 1

    # 긍정점수를 기준으로 내림차순 정렬
    score_list = sorted(score_dict.items(), key=lambda x : x[1], reverse=True)

    data = []

    # 긍정점수 상위 5개 도서에 대한 정보 저장
    for i in range(5) :
        book_dict = {}
        book_dict['title'] = healing_keyword_book[int(score_list[i][0])].title
        book_dict['author'] = healing_keyword_book[int(score_list[i][0])].author
        book_dict['publisher'] = healing_keyword_book[int(score_list[i][0])].publisher
        book_dict['image'] = healing_keyword_book[int(score_list[i][0])].image
        book_dict['positive_score'] = round(float(healing_keyword_book[int(score_list[i][0])].positive_score), 2)

        data.append(book_dict)

    # print(data)

    return JsonResponse(data, safe = False)


# ---------- similarity ----------
def similarity(request) :
    return render(request, 'similarity.html')


def search(request) :
    word = request.POST['word']
    # print(word)
    pass


# 인덱스 찾기
# def get_index_from_name(name) :
#     return df[df['bookname'] == name].index.tolist()[0]


# 특정단어를 통해 책 찾기
# def get_id_from_partial_name(partial) :
#     for name in all_books_names :
#         if partial in name:
#             print(name)
