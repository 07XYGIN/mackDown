class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describe_restaurant(self):
        print(self.cuisineType, self.restaurantName)

    def open_restaurant(self):
        print('正在营业')


a = Restaurant('apple', 1)
print(a.restaurantName)
