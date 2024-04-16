products = []

def add_product():
    new_product = {}
    new_product["name"] = input("Enter the name of the product: ")
    new_product["description"] = input("Enter the description of the product: ")
    new_product["price"] = float(input("Enter the value of the product: "))
    availability = input("Is the product available for sale? (yes/no) ")
    new_product["available"] = (availability.lower() == "yes")
    products.append(new_product) 

def display_products():
    for i, product in enumerate(products):
        print(f"Product {i+1} information:")
        print("Name: ", product["name"])
        print("Description: ", product["description"])
        print("Price: ", product["price"])
        print("Available: ", product["available"])
        print("------------------------------")

def smallest():
    products.sort(key=lambda x: x["price"])
    return products

def main():
    while True:
        print("1. Add a product")
        print("2. Listing")
        print("3. Order smallest")
        print("4. Exit")
        option = int(input("Enter the number of the option: "))
        if option == 1:
            add_product()
            display_products()
        elif option == 2:
            display_products()
        elif option == 3:
            smallest()
        elif option == 4:
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()