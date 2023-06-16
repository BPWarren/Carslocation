"""
Name :ABODJI Kondi Kalèd
purpose : creation of many database object in a single operation without django shell
"""
# Imports
from .models import Car, Booking, Customer, Rating, Comment, Category

# Category
create_category = [
    Category(
        title="sport",
        urls=[
            "/static/store/images/sport1.jpg",
            "/static/store/images/sport2.jpg",
            "/static/store/images/sport3.jpg",
        ],
    ),
    Category(
        title="pickup",
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
    Category(
        title="van",
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
    Category(
        title="familial",
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
    Category(
        title="racing",
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
    Category(
        title="camping car",
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
]
created_category = Category.objects.bulk_create(create_category)


# Customer objects List
customers_to_create = [
    Customer(name="Warren", email="warren@gmail.com", address="Jarama", cni="EB4121"),
    Customer(
        name="Hellen", email="helen@gmail.com", address="Karama Av jk", cni="Vb4121"
    ),
    Customer(name="Dig Herman", email="dig@gmail.com", address="U_arama", cni="El121"),
    Customer(name="Hijo", email="hijo@gmail.com", address="Curcuma", cni="NM4121"),
    Customer(name="Single", email="si@gmail.com", address="Jarama", cni="EB4121"),
]

# Registration of the data
created_customers = Customer.objects.bulk_create(customers_to_create)

# Cars
car_to_create = [
    Car(
        model="C4",
        brand="Citroen",
        category=created_category[0],
        price=4000,
        quantity=5,
        urls=[
            "/static/store/images/pickup1.jpg",
            "/static/store/images/pickup2.jpg",
            "/static/store/images/pickup3.jpg",
        ],
    ),
    Car(
        model="V8",
        brand="Lambo",
        category=created_category[0],
        price=10000,
        quantity=2,
        urls=[
            "/static/store/images/sport1.jpg",
            "/static/store/images/sport2.jpg",
            "/static/store/images/sport3.jpg",
        ],
    ),
    Car(
        model="Yoga L",
        brand="RaRo",
        category=created_category[1],
        price=6000,
        quantity=5,
        urls=["/img1", "img2", "img3"],
    ),
]

created_cars = Car.objects.bulk_create(car_to_create)
# Rating
create_rate = [
    Rating(rate=2, rated_car=created_cars[0]),
    Rating(rate=4, rated_car=created_cars[0]),
    Rating(rate=2.5, rated_car=created_cars[0]),
    Rating(rate=2, rated_car=created_cars[1]),
    Rating(rate=2, rated_car=created_cars[1]),
]
created_rate = Rating.objects.bulk_create(create_rate)
# Comment
create_comment = [
    Comment(comment="This is a wordeful car", commented_car=created_cars[0]),
    Comment(comment="My wife liked that car", commented_car=created_cars[0]),
    Comment(comment="I wante it again", commented_car=created_cars[0]),
    Comment(comment="Always dreaming about", commented_car=created_cars[1]),
    Comment(comment="This is a wordeful car", commented_car=created_cars[1]),
]
created_com = Comment.objects.bulk_create(create_comment)
# Booking
book_to_create = [
    Booking(customer=customers_to_create[0], car=created_cars[0]),
    Booking(customer=customers_to_create[1], car=created_cars[1]),
    Booking(customer=customers_to_create[0], car=created_cars[2]),
]

created_book = Booking.objects.bulk_create(book_to_create)
print(created_book)
