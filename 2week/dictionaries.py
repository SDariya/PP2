# 1 ex

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# 2 ex

car["year"] = 2020
print(car)

# 3 ex

car["color"] = "red"
print(car)

# 4 ex

car.pop("model")
print(car)

# 5 ex

car.clear()
print(car)