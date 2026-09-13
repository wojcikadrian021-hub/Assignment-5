from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[:3])


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""

while response != "N":
    print("Input a preference:")
    preference = input()

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        matches = count_matches(product["tags"], customer_tags)

        if matches > 0:
            recommendations.append({
                "name": product["name"],
                "matches": matches
            })

    recommendations.sort(key=lambda x: x["matches"], reverse=True)

    return recommendations


# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)

print("\nRecommended Products:")

for product in recommendations:
    print(f'- {product["name"]} ({product["matches"]} match(es))')


# DESIGN MEMO
#
# For this program I used lists, sets, loops, and intersections. I used a list
# at first to store the preferences that the customer enters. I then changed
# the list into a set because sets get rid of duplicate values and make it
# easier to compare the preferences with the product tags. I also changed the
# product tags into sets for the same reason.
#
# I used an intersection to see which tags were the same between the customer
# preferences and the product tags. I then used len() to count how many of
# those tags matched. I used a loop to go through every product in the list
# and check it one at a time. If a product had at least one matching tag, it
# was added to the recommendation list. The products were then sorted so the
# ones with the most matches showed up first.
#
# If there were over 1,000 products, I think this could start getting slower
# because the program checks every single product. I would probably need a
# better way to store and search all of the products. A database could probably
# help with this because it would make it easier to find products without
# going through everything one by one. The basic idea would still work, but
# it would need a better way to handle a lot more data.
