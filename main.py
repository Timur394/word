words = {
            "криндж": "Что-то очень странное или стыдное",
            "лол": "Что-то очень смешное",
            "рандом": "случайно",
            "мем": "шутка-анекдот",
            "изи": "легко"
            }
word = input("Введите непонятное слово: ").lower()
if word in words:
    print("Перевод:", words[word])
else:
     print("Нету такого слова тута:")
