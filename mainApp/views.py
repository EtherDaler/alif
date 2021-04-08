from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse 
from .serializers import DictionarySerializer
from .models import Dictionary
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return HttpResponse("Чтобы добавить в базу данных нашего словаря анаграммы, перейдите по ссылке /add \n и укажите в качестве параметра переменную arr и массив (например localhost:8080/add?arr=[\"foobar\",\"aabb\",...], который нужно определить.\n Чтобы найти анаграммы перейдите по /get и в качестве параметров укажите переменную word и слово(например localhost:8080/get?word=foobar)")

def anagramm_base(arr, word):

  res = []

  if type(word) is str and type(arr) is list:

    new_word = word.strip().lower()

    for i in arr:

      if type(i) is str:

        count = 0
        arr_word = i.strip().lower()

        if len(new_word) == len(arr_word):

          for j in new_word:

            if j in arr_word:

              count += 1

          if count == len(new_word):

            res.append(i)
      else:

        return None

    if len(res) > 0:

      return res

  return None



def get(request):
	word = str(request.GET.get('word'))
	if request.method == 'GET':
		word = list(word)
		if word[0] == "\"":
			del word[0]
		if word[-1] == "\"":
			del word[-1]
		word = ''.join(word)
		arr = []
		dic =  Dictionary.objects.all()
		for i in dic:
			arr.append(i.name)
		res = anagramm_base(arr, word)
		return JsonResponse({'result': res})

@csrf_exempt
def add(request):
	arr = list(request.GET.get('arr'))
	if request.method == 'GET':
		i = 0
		while i <= len(arr) -1 :
			if arr[i] == "\"": 
				del arr[i]
			i += 1

		str_from_arr = ''.join(arr)

		if str_from_arr[0] == "[" and str_from_arr[-1] == "]":
			str_from_arr = str_from_arr[1:-1]
		elif  str_from_arr[0] != "[" and str_from_arr[-1] == "]":
			str_from_arr = str_from_arr[:-1]
		elif  str_from_arr[0] == "[" and str_from_arr[-1] != "]":
			str_from_arr = str_from_arr[1:]
		elif  str_from_arr[0] != "[" and str_from_arr[-1] != "]":
			str_from_arr = str_from_arr[:]

		final_arr = str_from_arr.split(",")

		for i in final_arr:
			Dictionary.objects.create(name = i)
		return JsonResponse({"success": True, "your_words": final_arr})
	return JsonResponse({"success":False})


