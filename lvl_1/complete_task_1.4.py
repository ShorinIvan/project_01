# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [{'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [{'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175},]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

sneakers=titles['Кроссовки тип 3 (Adidas)']
qp_sneakers=store[sneakers][0]
q_sneakers=qp_sneakers['quantity']
p_sneakers=qp_sneakers['price']
tprice_sneakers=q_sneakers*p_sneakers
print(f'Кроссовки тип 3 (Adidas) - {q_sneakers} шт, стоймость {tprice_sneakers} руб')

ball = titles['Мячик тип 2 (Adidas)']
qp_ball1 = store[ball][0]
qp_ball2 = store[ball][1]
q_ball = qp_ball1['quantity']+qp_ball2['quantity']
tprice_ball =qp_ball1['quantity'] * qp_ball1['price']+qp_ball2['quantity']*qp_ball2['price']
print(f'Мячик тип 2 (Adidas) - {q_ball} шт, стоимость {tprice_ball} руб')

cap = titles['Кепка тип 1 (Adidas)']
qp_cap1 = store[cap][0]
qp_cap2 = store[cap][1]
q_cap = qp_cap1['quantity']+qp_cap2['quantity']
tprice_cap = qp_cap1['quantity']*qp_cap1['price']+qp_cap2['quantity']*qp_cap2['price']
print(f'Кепка тип 1 (Adidas) - {q_cap} шт, стоимость {tprice_cap} руб')

belt = titles['Ремень тип 2 (Nike)']
qp_belt1 = store[belt][0]
qp_belt2 = store[belt][1]
q_belt = qp_belt1['quantity']+qp_belt2['quantity']
tprice_belt = qp_belt1['quantity']*qp_belt1['price']+qp_belt2['quantity']*qp_belt2['price']
print(f'Ремень тип 2 (Nike) - {q_belt} шт, стоимость {tprice_belt} руб')


shirt = titles['Футболка тип 1 (Adidas)']
qp_shirt1 = store[shirt][0]
qp_shirt2 = store[shirt][1]
qp_shirt3 = store[shirt][2]
q_shirt = qp_shirt1['quantity']+qp_shirt2['quantity']+qp_shirt3['quantity']
tprice_shirt= qp_shirt1['quantity']*qp_shirt1['price']+qp_shirt2['quantity']*qp_shirt2['price']+qp_shirt3['quantity']*qp_shirt3['price']
print(f'Футболка тип 1 (Adidas) - {q_shirt}, шт, стоимость {tprice_shirt} руб')

hat = titles['Шапка тип 5 (Puma)']
qp_hat = store[hat][0]
q_hat = qp_hat['quantity']
p_hat = qp_hat['price']
tprice_hat = q_hat*p_hat
print(f'Шапка тип 5 (Puma) - {q_hat} шт, стоимость {tprice_hat} руб')






