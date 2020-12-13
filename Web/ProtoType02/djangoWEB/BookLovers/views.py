from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

# Create your views here.


def index(request) :
    return render(request, 'index.html')


def category(request) :
    return render(request, 'category.html')


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


def mbti(request) :
    return render(request, 'mbti.html')


def healing(request) :
    return render(request, 'healing.html')


# def exam1(request):
#     print(">>>>>>>>>>>>>>>>>>>> exam1 request")
#     return render(request, 'examPage1.html')


# def exam2(request):
#     exam1_Q1 = request.POST['exam1_Q1']
#     exam1_Q2 = request.POST['exam1_Q2']
#     exam1_Q3 = request.POST['exam1_Q3']
#     E = 0
#     I = 0
#
#     if exam1_Q1 == "E":
#         E += 1
#     else:
#         I += 1
#     if exam1_Q2 == "E":
#         E += 1
#     else:
#         I += 1
#     if exam1_Q3 == "E":
#         E += 1
#     else:
#         I += 1
#
#     if E > I :
#         exam1_mbti.append("E")
#     else:
#         exam1_mbti.append("I")
#     print(">>>> ", exam1_Q1, exam1_Q2, exam1_Q3)
#     print(E, I, exam1_mbti)
#     return render(request, 'examPage2.html')


# def exam3(request):
#     exam2_Q1   = request.POST['exam2_Q1']
#     exam2_Q2   = request.POST['exam2_Q2']
#     exam2_Q3   = request.POST['exam2_Q3']
#     S = 0
#     N = 0
#
#     if exam2_Q1 == "S":
#         S += 1
#     else:
#         N += 1
#     if exam2_Q2 == "S":
#         S += 1
#     else:
#         N += 1
#     if exam2_Q3 == "S":
#         S += 1
#     else:
#         N += 1
#
#     if S > N :
#         exam2_mbti.append("S")
#     else:
#         exam2_mbti.append("N")
#     print(">>>> ", exam2_Q1, exam2_Q2, exam2_Q3)
#     print(S, N, exam1_mbti, exam2_mbti)
#     return render(request, 'examPage3.html')


# def exam4(request):
#     exam3_Q1 = request.POST['exam3_Q1']
#     exam3_Q2 = request.POST['exam3_Q2']
#     exam3_Q3 = request.POST['exam3_Q3']
#     T = 0
#     F = 0
#
#     if exam3_Q1 == "T":
#         T += 1
#     else:
#         F += 1
#     if exam3_Q2 == "T":
#         T += 1
#     else:
#         F += 1
#     if exam3_Q3 == "T":
#         T += 1
#     else:
#         F += 1
#
#     if T > F :
#         exam3_mbti.append("T")
#     else:
#         exam3_mbti.append("F")
#     print(">>>> ", exam3_Q1, exam3_Q2, exam3_Q3)
#     print(T, F, exam1_mbti, exam2_mbti, exam3_mbti)
#     return render(request, 'examPage4.html')


# def result(request):
#     exam4_Q1 = request.POST['exam4_Q1']
#     exam4_Q2 = request.POST['exam4_Q2']
#     exam4_Q3 = request.POST['exam4_Q3']
#     J = 0
#     P = 0
#
#     if exam4_Q1 == "J":
#         J += 1
#     else:
#         P += 1
#     if exam4_Q2 == "J":
#         J += 1
#     else:
#         P += 1
#     if exam4_Q3 == "J":
#         J += 1
#     else:
#         P += 1
#
#     if J > P:
#         exam4_mbti.append("J")
#     else:
#         exam4_mbti.append("P")
#
#     mbti = str(exam1_mbti + exam2_mbti + exam3_mbti + exam4_mbti)
#
#     print(">>>> ", exam4_Q1, exam4_Q2, exam4_Q3)
#     print(J, P, exam1_mbti, exam2_mbti, exam3_mbti, exam4_mbti, mbti)
#     return render(request, 'resultPage.html')


# def wordcloud(request) :
#     return render(request, 'wordcloud.html')


def keyword_info(request, keyword) :
    healing_keyword = keyword

    pass
