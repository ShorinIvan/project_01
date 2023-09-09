# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random 
import datetime 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_songs = random.sample(my_favorite_songs , 3)
sum_time=datetime.timedelta()
song = [
       str(random_songs[0][1]),
       str(random_songs[1][1]),
       str(random_songs[2][1])       
]


for time in song:
    minutes, seconds = time.split(".")
    minutes, seconds = int(minutes), int(seconds)
    sum_time+= datetime.timedelta(minutes=minutes,seconds=seconds)

print("Три песни звучат", sum_time, "минут")


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
time = list(my_favorite_songs_dict.items())
three_song = random.sample(time, 3)
total_time_2 = [
    str(three_song[0][1]),
    str(three_song[1][1]),
    str(three_song[2][1])

]

    


delta_2=datetime.timedelta()

for time in total_time_2:
    minutes, seconds = time.split(".")
    minutes, seconds = int(minutes), int(seconds)
    delta_2 += datetime.timedelta(minutes=minutes, seconds=seconds)
print("Три песни звучат", delta_2, "минут")




# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
