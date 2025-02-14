# Общее описание решения
Данный репозиторий содержит 4 файла с функциями на языке Python, благодаря которым можно получать площади и периметры некоторых геометрических фигур. Для вычислений в решении используются классические математические формулы.

# Описание каждой функции с примерами вызова
## circle.py:
### 1) area(r) 
Возвращает площадь окружности при заданном значении радиуса окружности

Пример вызова: 

![screen1.png](screen1.png)

Пример вывода:

![screen2.png](screen2.png)

### 2) perimeter(r)
Возвращает периметр окружности при заданном значении радиуса окружности

Пример вызова:

![screen3.png](screen3.png)

Пример вывода:

![screen4.png](screen4.png)

## rectangle.py:
### 1) area(a,b)
Возвращает площадь прямоугольника со сторонами a,b

Пример вызова:

![screen5.png](screen5.png)

Пример вывода:

![screen6.png](screen6.png)

### 2) perimeter(a,b)
Возвращает периметр прямоугольника со сторонами a,b

Пример вызова:

![screen01.png](screen01.png)

Пример вывода:

![screen001.png](screen001.png)

## square.py
### 1) area(a)
Возвращает площадь квадрата со стороной a

Пример вызова:

![screen7.png](screen7.png)

Пример вывода:

![screen8.png](screen8.png)

### 2) perimeter(a)
Возвращает периметр квадрата со стороной a

Пример вызова:

![screen9.png](screen9.png)

Пример вывода:

![screen10.png](screen10.png)

## triangle.py
### 1) area(a,h)
Возвращает площадь треугольника со стороной a и высотой к ней h

Пример вызова:

![screen11.png](screen11.png)

Пример вывода:

![screen12.png](screen12.png)

### 2) perimeter(a,b,c)
Возвращает периметр треугольника со сторонами a,b,c

Пример вызова:

![screen13.png](screen13.png)

Пример вывода:

![screen14.png](screen14.png)

# История изменения проекта с хешами коммитов:

1) Был добавлен новый файл rectangle.py для вычисления периметра и площади прямоугольника. (Хеш коммита - 9a89260)
2) Исправлена ошибка в файле для вычисления периметра и площади прямоугольника. Добавлен файл для вычисления периметра и площади прямоугольника. (Хеш коммита - 82472bc)
3) Добавлен комментарий к работе функций area и perimeter в файле circle.py (Хеш коммита - a63b87f)
4) Добавлен комментарий к работе функций area и perimeter в файле rectangle.py (Хеш коммита - 805fce8)
5) Добавлен комментарий к работе функций area и perimeter в файле square.py (Хеш коммита - ac5747a)
6) Добавлен комментарий к работе функций area и perimeter в файле triangle.py (Хеш коммита - 8a54543)
7) Добавлены unit-тесты для файлов circle.py, rectangle.py, square.py, triangle.py (Хеш коммита - bd616de)

# Unit-tests
Для проверки работы функций были созданы unit-тесты. Для каждого файла был создан файл с названием unittests_<фигура>.py. В каждом файле содержатся тесты 4 типов:
1) тест при вводе аргументов подходящего типа и значения
2) тест при вводе аргументов неподходящего типа
3) тест при вводе нулевого значения аргумента
4) тест при вводе аргументов с минусовым значением (фигуры с минусовыми сторонами не могут существовать)

- ## unittest_circle.py
    пройдено 4 из 8 тестов
- ## unittest_rectangle.p
    пройдено 4 из 12 тестов
- ## unittest_square.py
    пройдено 4 из 8 тестов
- ## unittest_triangle.py
    пройдено 4 из 14 тестов


| тестируемый файл | функция файла | входные данные | результат теста |
|------------------|---------------|----------------|-----------------|
| circle.py        | area          | 6              | passed          |
| circle.py        | area          | 0              | passed          |
| circle.py        | area          | "6"            | failed          |
| circle.py        | area          | -5             | failed          |
| circle.py        | perimeter     | 6              | passed          |
| circle.py        | perimeter     | 0              | passed          |
| circle.py        | perimeter     | "6"            | failed          |
| circle.py        | perimeter     | -5             | failed          |
| rectangle.py     | area          | 4, 3           | passed          |
| rectangle.py     | area          | 4, 0           | passed          |
| rectangle.py     | area          | 0, 3           | passed          |
| rectangle.py     | area          | "4", 3         | failed          |
| rectangle.py     | area          | 4, "3"         | failed          |
| rectangle.py     | area          | -5, 6          | failed          |
| rectangle.py     | perimeter     | 4, 3           | passed          |
| rectangle.py     | perimeter     | 4, 0           | failed          |
| rectangle.py     | perimeter     | 0, 3           | failed          |
| rectangle.py     | perimeter     | "4", 3         | failed          |
| rectangle.py     | perimeter     | 4, "3"         | failed          |
| rectangle.py     | perimeter     | -5, 6          | failed          |
| square.py        | area          | 5              | passed          |
| square.py        | area          | 0              | passed          |
| square.py        | area          | "5"            | failed          |
| square.py        | area          | -5             | failed          |
| square.py        | perimeter     | 5              | passed          |
| square.py        | perimeter     | 0              | passed          |
| square.py        | perimeter     | "5"            | failed          |
| square.py        | perimeter     | -5             | failed          |
| triangle.py      | area          | 4, 3           | passed          |
| triangle.py      | area          | 4, 0           | passed          |
| triangle.py      | area          | 0, 3           | passed          |
| triangle.py      | area          | "4", 3         | failed          |
| triangle.py      | area          | 4, "3"         | failed          |
| triangle.py      | area          | -5, 6          | failed          |
| triangle.py      | perimeter     | 4, 3, 2        | passed          |
| triangle.py      | perimeter     | 4, 3, 0        | failed          |
| triangle.py      | perimeter     | 4, 0, 2        | failed          |
| triangle.py      | perimeter     | 0, 3, 2        | failed          |
| triangle.py      | perimeter     | "4", 3, 2      | failed          |
| triangle.py      | perimeter     | 4, "3", 2      | failed          |
| triangle.py      | perimeter     | 4, 3, "2"      | failed          |
| triangle.py      | perimeter     | -4, 3, 2       | failed          |