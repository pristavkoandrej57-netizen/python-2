salesData = [
        {"name": "батончики", "price": 60, "quantity": 10},
        {"name": "вода", "price": 50, "quantity": 15},
        {"name": "Яблоки", "price": 50, "quantity": 5},
        {"name": "Апельсины", "price": 70, "quantity": 8},
        {"name": "Бананы", "price": 40, "quantity": 10}
    ]
revenueMap = {}
uniqueNames = set()

for item in salesData:
    name = item["name"]
    totalPrice = item["price"] * item["quantity"]
        
    uniqueNames.add(name)
        
    if name in revenueMap:
        revenueMap[name] += totalPrice
    else:
        revenueMap[name] = totalPrice

for name, total in revenueMap.items():
    print(f"Товар: {name}, Общая выручка: {total}")


if revenueMap:
    best_product = max(revenueMap, key=revenueMap.get)
    print(f"\nСамый прибыльный товар: {best_product} (Выручка: {revenueMap[best_product]})")

print(f"Количество уникальных наименований: {len(uniqueNames)}")