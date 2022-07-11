from food import Food
from drink import Drink

food1 = Food('ハンバーグ', 500, 330)
food2 = Food('ショートケーキ', 400, 450)
food3 = Food('パフェ', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('コーヒー', 300, 180)
drink2 = Drink('コーラ', 200, 350)
drink3 = Drink('カルピス', 300, 30)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('------------------------')

food_order = int(input('食べ物の番号を選択してください: '))
selected_food = foods[food_order]

drink_order = int(input('飲み物の番号を選択してください: '))
selected_drink = drinks[drink_order]

count = int(input("何セット買いますか？（３つ以上で１割引）: "))

result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print("合計は" + str(result) + "円です")

