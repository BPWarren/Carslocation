from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db import transaction
from .models import Car, Category, Customer, Booking

from .forms import CustomerForm
import os

# Create your views here.


# index view
def index(request):
    categories = Category.objects.all()
    cars = Car.objects.all()
    context = {"categories": categories, "cars": cars}
    return render(request, "store/index.html", context)


# liste wiew
def liste_percategory(request, categoryname):
    category_cars = Car.objects.filter(category__title=categoryname)
    temp = []
    for car in category_cars:
        temp.append(car.brand + " " + car.model + " " + car.category.title)
    return HttpResponse("-".join(temp))


# Car details
@transaction.atomic()
def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    # Car disponible?
    context = {"car": car}
    if request.method == "POST":
        if not car.available:
            return render(request, "store/details.html", context)

        form = CustomerForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            cni = form.cleaned_data["cni"]
            address = form.cleaned_data["address"]

            customer = Customer.objects.filter(email=email)
            # si l'utilisateur n'existe pas
            if not customer.exists():
                customer = Customer.objects.create(
                    name=fullname, email=email, address=address, cni=cni
                )
            else:
                customer = customer[0]
            car = get_object_or_404(Car, id=id)
            Booking.objects.create(customer=customer, car=car)

            car.quantity -= 1
            if car.quantity == 0:
                car.available = False
            car.save()

            context["customer"] = customer
            return render(request, "store/thanks.html", context)
        else:
            context["errors"] = form.errors.items()

    form = CustomerForm()
    context["form"] = form
    return render(request, "store/details.html", context)


# search bar
def search(request):
    pass


# rest of the list
def cars_list(request):
    # intégrer la pagination
    cars = Car.objects.all()

    context = {"cars": cars}

    return render(request, "store/carslist.html", context)
