from django.contrib.auth import authenticate
from django.http.request import *
from django.http.response import *
from django.shortcuts import *
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import *


# Create your views here.


def index(request):
    from .forms import UserForm, OrderForm
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.filter(first_name=first_name,
                                   last_name=last_name)
        if not user:
            return render(request, 'register.html', {'form': UserForm(), 'error': True})
        else:
            return render(request, 'user.html', {'user': user, 'form': UserForm(), 'error': True})
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form, 'error': True})


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


class Show(View):
    def list(request):
        users = User.objects.all()
        return render(request, 'list.html', {'users': users, 'form': UserForm})

    def user(request, user_id):
        user = User.objects.get(id=user_id)
        cars = Car.objects.filter(host_id=user_id)
        return render(request, 'user.html', {'user': user, 'cars': cars})

    def register(request):
        from .forms import UserForm, OrderForm
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            email = request.POST.get('email')

            user = User(first_name=first_name,
                        last_name=last_name,
                        date_of_birth=date_of_birth,
                        phone_number=phone_number,
                        address=address,
                        email=email)
            user.save()
            cars = Car.objects.filter(host_id=user.id)
            return render(request, 'user.html', {'user': user, 'cars': cars, 'form': UserForm(), 'error': True})
        else:
            form = UserForm()
        return render(request, 'register.html', {'form': form, 'error': True})

    def home(request):
        from .forms import UserForm
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = User.objects.filter(first_name=first_name,
                                       last_name=last_name)
            if not user:
                return render(request, 'register.html', {'form': UserForm(), 'error': True})
            else:
                return render(request, 'user.html', {'user': user, 'form': UserForm(), 'error': True})
        else:
            form = UserForm()
        return render(request, 'home.html', {'form': UserForm(), 'error': True})

    def new_order(request, car_id, user_id):
        from .forms import OrderForm, UserForm
        form = OrderForm(request.POST)
        if request.method == 'POST':
            date = request.POST.get('date')
            amount = request.POST.get('amount')
            status = request.POST.get('status')

            order = Order(date=date, amount=amount, status=status, car_id=car_id)
            order.save()
            car = Car.objects.filter(id=car_id)
            orders = Order.objects.filter(car_id=car_id)
            return render(request, 'car.html', {'car': car, 'orders': orders, 'form': UserForm(), 'error': True})
        else:
            form = OrderForm()
        return render(request, 'new_order.html', {'car': Car.objects.get(id=car_id), 'form': form, 'error': True})

    def new_car(request, user_id):
        from .forms import CarForm
        form = CarForm()
        print('user_id = ', user_id)
        if request.method == 'POST':
            form = CarForm(request.POST)
            make = request.POST.get('make')
            year = request.POST.get('year')
            vin = request.POST.get('vin')
            model = request.POST.get('model')
            host_id = user_id
            car = Car(host_id=host_id, make=make,
                      year=year, vin=vin,
                      model=model)
            if car.model == None:
                return render(request, 'new_car.html',
                              {'form': form, 'user': User.objects.get(id=user_id), 'error': True})
            else:
                car.save()
            print('i save')
            cars = Car.objects.filter(host_id=host_id)
            return render(request, 'user.html', {'user': User.objects.get(id=user_id), 'cars': cars})
        else:
            form = CarForm()
        return render(request, 'new_car.html', {'form': form, 'user': User.objects.get(id=user_id), 'error': True})

    def car(request, car_id, user_id):
        orders = Order.objects.filter(car_id=car_id)
        car = Car.objects.get(id=car_id)
        print('car_id = ', car.id)
        return render(request, 'car.html', {'car': car, 'form': UserForm, 'orders': orders})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import AdminForm
        return render(request, 'admin_login.html', {'form': AdminForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from .forms import AdminForm
        form = AdminForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        admin: Admin = authenticate(request, username=username, password=password)
        if not admin:
            return render(request, 'index.html', {'form': AdminForm(), 'error': True})
        admin.auth = 1
        login(request, admin)
        return redirect(reverse('index'))



class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('list')


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'date_of_birth', 'address', 'email', 'phone_number']
    template_name_suffix = '_update'
    def get_success_url(self):
        return reverse('list')

class CarDelete(DeleteView):
        model = Car
        success_url = reverse_lazy('list')


class CarUpdate(UpdateView):
    model = Car
    fields = ['year', 'vin', 'make', 'model']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('list')


class OrderUpdate(UpdateView):
    model = Order
    fields = ['status', 'date', 'amount']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('list')
