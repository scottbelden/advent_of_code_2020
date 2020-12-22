from collections import defaultdict

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_21_input")

all_ingredients = set()
allergy_mapping = defaultdict(list)
original_ingrediant_counts = defaultdict(int)
for line in lines:
    ingredients, allergens = line.split(" (contains ")
    ingredient_set = set(ingredients.split())
    all_ingredients |= ingredient_set

    for ingredient in ingredient_set:
        original_ingrediant_counts[ingredient] += 1

    for allergen in allergens[:-1].split(", "):
        allergy_mapping[allergen].append(ingredient_set)

resolved_allergens = {}
while True:
    if len(allergy_mapping) == 0:
        break

    for allergen, ingredient_sets in allergy_mapping.items():
        common_ingrediants = set.intersection(*ingredient_sets)
        if len(common_ingrediants) == 1:
            common_ingrediant = common_ingrediants.pop()
            resolved_allergens[common_ingrediant] = allergen

            new_mapping = {}
            for allergen_2, ingredient_sets_2 in allergy_mapping.items():
                if allergen_2 == allergen:
                    continue

                new_mapping[allergen_2] = [
                    ingredient_set - {common_ingrediant}
                    for ingredient_set in ingredient_sets_2
                ]

            break

    allergy_mapping = new_mapping

total = sum(
    count
    for ingredient, count in original_ingrediant_counts.items()
    if ingredient not in resolved_allergens
)


ANSWER1 = answer1(total)

sorted_ingredients = [
    ingredient
    for ingredient, _ in sorted(resolved_allergens.items(), key=lambda item: item[1])
]
ANSWER2 = answer2(",".join(sorted_ingredients))
