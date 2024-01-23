import collections

ingredients = ['bread', 'bread', 'tofu', 'rice', 'kale', 'kale', 'kale']
def max_repeated_ingredients(ingredients: list[str]) -> str:
 return max(collections.Counter(ingredients).values())

print(max_repeated_ingredients(ingredients))


def MaxRepeated(ingredients: list[str]) -> str:
  max_ingredient = -1
  ingredients_count = {}
  for ingredient in ingredients:
    if ingredient not in ingredients_count:
      ingredients_count[ingredient] = 1
    else:
      ingredients_count[ingredient] += 1
    if ingredients_count[ingredient] > max_ingredient:
      max_ingredient = ingredients_count[ingredient]  
  return max_ingredient
print(MaxRepeated(ingredients))
