# =========================
# CLASS RESTAURANT
# =========================

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):          #untuk menginisialisasi keadaan (state)
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Nama Restoran:", self.restaurant_name)
        print("Jenis Masakan:", self.cuisine_type)

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} sedang buka.")
    print("---------------------------")
   

restoran1 = Restaurant("Sate Khas Bg Rey", "Sate")
restoran2 = Restaurant("Nasi Padang Kita", "Nasi Padang")
restoran3 = Restaurant("Ayam Geprek Nagih", "Ayam geprek")

restoran1.describe_restaurant()
restoran1.open_restaurant()
print()

restoran2.describe_restaurant()
restoran2.open_restaurant()
print()

restoran3.describe_restaurant()
restoran3.open_restaurant()


print()
print()
print()


# =========================
# CLASS USER
# =========================

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
       
    def describe_user(self):
        print("Nama Depan:", self.first_name)
        print("Nama Belakang:", self.last_name)
        print("Email:", self.email)
        print("Usia:", self.age)

    def greet_user(self):
        print(f"Halo {self.first_name} {self.last_name}, selamat datang!")
        print("---------------------------")


user1 = User("Raihan", "Elfarid", "raihan.elfarid@gmail.com", 19)
user2 = User("Alya", "Putri", "alya.putri@gmail.com", 20)

user1.greet_user()
user1.describe_user()

print()
print()

user2.greet_user()
user2.describe_user()



