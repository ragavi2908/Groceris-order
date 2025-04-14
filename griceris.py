print("Welcome to Smart Grocery Store")


gender_select = input("What gender you are: ")
gender = ("1.female", "2.male")
print("2.male" in gender)  


groceries = {"rice": 60, "milk": 45,"sugar": 40,"toothpaste": 55,"soap": 30}


gst_rates = {"food": 5,"personal care": 12}

item_category = {"rice": "food","milk": "food", "sugar": "food","toothpaste": "personal care","soap": "personal care"}

item = input("Enter the grocery item you want to buy: ").lower()
if item in groceries:
    print(f"{item.title()} is available at ₹{groceries[item]} per unit.")
    
    quantity = int(input("Enter quantity: "))
    base_price = groceries[item] * quantity
    
    category = item_category[item]
    gst_percent = gst_rates[category]
    gst_amount = base_price * gst_percent / 100
    total_price = base_price + gst_amount

    print("\n------ Bill Summary ------")
    print(f"Item         : {item.title()}")
    print(f"Category     : {category.title()}")
    print(f"Quantity     : {quantity}")
    print(f"Base Price   : ₹{base_price}")
    print(f"GST ({gst_percent}%) : ₹{gst_amount:.2f}")
    print(f"Total Amount : ₹{total_price:.2f}")
else:
    print(f'sorry your{item} is not available in the store')
