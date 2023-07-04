class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print("Mobile details:")
        print("Company:", self.company)
        print("Model:", self.model)
        print("Price:", self.price)

# Example usage:
m1 = Mobile()
m1.set_details("Apple", "iPhone 12", 799)

m2 = Mobile()
m2.set_details("Samsung", "Galaxy S21", 699)

m3 = Mobile()
m3.set_details("Google", "Pixel 5", 699)

mobiles = [m1, m2, m3]
most_expensive = max(mobiles, key=lambda m: m.price)
most_expensive.display_details()

