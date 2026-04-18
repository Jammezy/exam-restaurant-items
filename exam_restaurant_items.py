# Enter you code here

# You can use this if you want
categories_list = ["APPETIZER", "SIDE", "ENTREE", "DESSERT"]

from peewee import *


db = SqliteDatabase('menuitem.db')

# creates a class inheriting from peewee's Model
class MenuItem(Model):
    menu_item_id = AutoField(primary_key=True)
    name = TextField()
    category = TextField()
    price = FloatField()

    class Meta:
        database = db


    @classmethod
    def create(cls, **query):
        price = query.get('price')
        category = query.get('category')

    
        if price >=0 and price <= 50 and (category == "APPETIZER" or category == "SIDE" or category == "ENTREE" or category == "DESSERT"):
            # data has been validated, run the create function (category is already capitalized when the user inputed their data: see option 1 below)
            return super().create(**query)
        
        if price <0 or price > 50:
            print()
            print("Invalid price! Price must be between $0 and $50.")
            print()
            return
        elif category != "APPETIZER" or category != "SIDE" or category != "ENTREE" or category != "DESSERT":
            print()
            print("Invalid category! Category must be either APPETIZER, SIDE, ENTREE, or DESSERT")
            print()
            return
        
        
    def get_info(self):
        return(f"ID: {self.menu_item_id} | Name: {self.name} | Category: {self.category} | Price: ${self.price}")
        


db.connect()
db.create_tables([MenuItem])

# creates a glorious loop
while True:
    # will print every time the loop iterates
    print("Restaurant Menu Manager")
    print("1. Add a menu item")
    print("2. View all menu items")
    print("3. View the most expensive item in each category")
    print("4. Exit")
    user_choice = input("Choose an option (1-4):").strip()

    # Option 1: Add a  menu item
    if user_choice == "1":
        print()
        u_item_name = input("Enter the item name:")
        # by making all the categories upper case, it satisfies the validation for the overridden create function
        u_category = input("Enter the category (APPETIZER, SIDE, ENTREE, DESSERT):").upper()
        # the user will always a proper input here per the directions
        u_price = float(input("Enter the price:"))

        first_obj = MenuItem.create(name = u_item_name, category = u_category, price = u_price)
        if first_obj:
            print()
            print(f"Item '{first_obj.name}' added successfully.")
            print()
    
    # Option 2: View all menu items
    elif user_choice == "2":
        # grab all objects in the database
        all_objs = MenuItem.select()
        # iterates through all the items and runs the specified method
        for item in all_objs:
            print(f"\t{item.get_info()}")
        print()

    elif user_choice == "3":
        x = 0

        # will loop until it's gone through all the items in the categories_list
        for catg in categories_list:
            # selects the most expensive item for a specified category
            expensive = MenuItem.select().where(MenuItem.category == categories_list[x]).order_by(MenuItem.price.desc()).first()
            
            # this assures that an item is in it. If not, it prints nothing an skips to the next category
            if expensive:
                print()
                print(f"Most Expensive {categories_list[x]}")
                print(f"\t{expensive.get_info()}")
            x += 1

        print()

    elif user_choice == "4":
        print()
        print("Goodbye!")
        break

    else:
        print()
        print("Invalid choice. Please try again.")
        print()












