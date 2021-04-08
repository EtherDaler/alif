from django.test import TestCase
import unittest
from .views import *

class AnagrammTest(unittest.TestCase): # Проверка функции нахождения анаграмм
	arr = None
	word = None
	waiting_result = None
	def test_anagramm_base(self):
		self.assertEqual(anagramm_base(self.arr, self.word), self.waiting_result)

check =  AnagrammTest()
check.arr = ["foobar", "raboof", "ooafbr", "test", "sett", "bar", "rab", 1, False, True, 2.54, ["one", "two"]]
check.word = "foobar"
check.waiting_result = ["foobar", "raboof", "ooafbr"]
test_f = AnagrammTest.test_anagramm_base

from django.test.utils import setup_test_environment, teardown_test_environment
# следушие 2 функции нужны, чтобы настроить среду для имитации работы пользователя
teardown_test_environment() 
setup_test_environment()

from django.test import Client
# Этот класс имимтирует пользователя
client = Client()

# Переход между ссылками на сайте
response = client.get('/')
# Получение ответа от сервера (статус подключения)
print("'/' status code: ", response.status_code)

from django.urls import reverse

response = client.get('/get/?word="foobar"')
print("'/get/?word=\"foobar\"' status code: ", response.status_code)
# Получение html кода с сервера
print("/get/ html: ", response.content)

response = client.get('/add/?arr=["first","second"]')
print("/add/?arr=[\"first\",\"second\"]' status code: ", response.status_code)
print("/add/ html: ", response.content)


