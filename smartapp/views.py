# from django.shortcuts import render, redirect, get_object_or_404
# from .models import ParkingSpot ,CustomUser
# from .forms import BookingForm
# from django.contrib.auth import authenticate, login, logout
# import razorpay
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt  
# from django.contrib.auth.decorators import login_required

# time_slots = {
#         '0': '11:00 AM - 12:00 PM',
#         '1': '12:00 PM - 1:00 PM',
#         '2': '1:00 PM - 2:00 PM',
#         '3': '2:00 PM - 3:00 PM',
#         '4': '3:00 PM - 4:00 PM',
#         '5': '4:00 PM - 5:00 PM',
#         '6': '5:00 PM - 6:00 PM',
#         '7': '6:00 PM - 7:00 PM',
#         '8': '7:00 PM - 8:00 PM',
#         '9': '8:00 PM - 9:00 PM',
# }

# def list(request):
#     spots=ParkingSpot.objects.all()
#     print(spots)
#     return render(request,'spot_list.html',{'spots':spots})

# def booking(request):
#     return render(request, 'book_spot.html')

# def parking_spot_detail(request, parking_spot_id):
#     time_slots = {
#         '0': '11:00 AM - 12:00 PM',
#         '1': '12:00 PM - 1:00 PM',
#         '2': '1:00 PM - 2:00 PM',
#         '3': '2:00 PM - 3:00 PM',
#         '4': '3:00 PM - 4:00 PM',
#         '5': '4:00 PM - 5:00 PM',
#         '6': '5:00 PM - 6:00 PM',
#         '7': '6:00 PM - 7:00 PM',
#         '8': '7:00 PM - 8:00 PM',
#         '9': '8:00 PM - 9:00 PM',
# }
#     parking_spot = get_object_or_404(ParkingSpot, id=parking_spot_id)
#     name = parking_spot.name

#     available_slots = parking_spot.available
#     center=parking_spot.center
#     newlist = [char for char in available_slots]
#     currentKey=get_key_from_time()
#     time_slots = {key: time_slots[key] for key in time_slots if key not in newlist and key >currentKey}
#     print(time_slots)
    
#     if request.method == 'POST':
#         form = BookingForm(request.POST, slot_info=time_slots)
#         if form.is_valid():
#             selected_slot = form.cleaned_data['available_slots']

#             print(selected_slot)
#             spots=''.join(selected_slot)
            
#             updatedSlots=parking_spot.available + spots
#             request.session['selected_slot']=spots  
#             request.session['center']=center       
#             request.session['parking_spot_id'] = parking_spot_id
#             request.session['updatedSlots'] = updatedSlots
#             return redirect('booking_success',name=name,spots=spots)
#     else:
#         form = BookingForm(slot_info=time_slots)

#     return render(request, 'trial.html', {'form': form, 'name': name})


# def booking_success(request, name,spots):
#     time_slots = {
#         '0': '11:00 AM - 12:00 PM',
#         '1': '12:00 PM - 1:00 PM',
#         '2': '1:00 PM - 2:00 PM',
#         '3': '2:00 PM - 3:00 PM',
#         '4': '3:00 PM - 4:00 PM',
#         '5': '4:00 PM - 5:00 PM',
#         '6': '5:00 PM - 6:00 PM',
#         '7': '6:00 PM - 7:00 PM',
#         '8': '7:00 PM - 8:00 PM',
#         '9': '8:00 PM - 9:00 PM',
# }
#     newlist=[]
#     for i in spots:
#         newlist.append(time_slots[i])
#     print(newlist)
#     request.session['newlist'] = newlist
#     request.session['name'] = name
#     bill=30*(len(spots))
#     razorpaybill=30*(len(spots))*100
#     center=request.session.get('center')
#     return render(request, 'success.html', {'name': name,'spots':newlist,'bill':bill,'center':center,'razorpaybill':razorpaybill})







# def create_order(request):
#     if request.method == 'POST':
#         amount = 50000  # amount in paisa
#         client = razorpay.Client(auth=('rzp_test_GtzVv7rlxPUO82', 'w4Np3Z2QUXErexJUUQWBtdGE'))
#         payment_data = {
#             'amount': 50000,
#             'currency': 'INR',
#             'receipt': 'order_rcptid_11',
#             'payment_capture': 1
#         }
#         order = client.order.create(data=payment_data)

#         return render(request, 'suceess.html', {'order': order})
#     return render(request, 'payment.html')


# @csrf_exempt 
# def handle_payment(request):
#     parking_spot_id=request.session.get('parking_spot_id') 
#     userInfo = get_object_or_404(CustomUser, id=request.user.id)
#     name=request.session.get('name')
#     userInfo.slot_booked=name
#     spots=request.session.get('selected_slot')
#     newlist=request.session.get('newlist')
#     center=request.session.get('center')
#     userInfo.slot_booked_time=request.session.get('updatedSlots')
#     updatedSlots=request.session.get('updatedSlots')
#     parking_spot = get_object_or_404(ParkingSpot, id=parking_spot_id)
#     userInfo.location=parking_spot.location
#     userInfo.center=parking_spot.center
#     parking_spot.available=updatedSlots
#     userInfo.save()
#     parking_spot.save()
   
#     return render(request, 'payment.html' ,{'name':name,'newlist':newlist,'center':center})
    

# def payment(request):
#     return render(request,'payment.html')





# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to the desired page after login
#         else:
#             # Handle invalid login
#             return render(request, 'login.html', {'error': 'Invalid login credentials'})
#     else:
#         return render(request, 'login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('login') 
# from .forms  import CustomUserCreationForm

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in
#             # Redirect to the home page or another page
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm() 

#     return render(request, 'signup.html', {'form': form})
# time_slots = {
#         '0': '11:00 AM - 12:00 PM',
#         '1': '12:00 PM - 1:00 PM',
#         '2': '1:00 PM - 2:00 PM',
#         '3': '2:00 PM - 3:00 PM',
#         '4': '3:00 PM - 4:00 PM',
#         '5': '4:00 PM - 5:00 PM',
#         '6': '5:00 PM - 6:00 PM',
#         '7': '6:00 PM - 7:00 PM',
#         '8': '7:00 PM - 8:00 PM',
#         '9': '8:00 PM - 9:00 PM',
# }

# @login_required(login_url='login') 
# def home(request):
#     if request.user.is_authenticated:
#         username = request.user.username
#         email = request.user.email
#         slot_booked = request.user.slot_booked
#         id= request.user.id
#         time= request.user.slot_booked_time
#         if time is not None :
#                 time= request.user.slot_booked_time
#         print("time",time)
#         selected_time_slots =[time_slots[slot] for slot in time]
#         print(selected_time_slots)
#         finalTimes=deleteSpots(time)  
#         userInfo = get_object_or_404(CustomUser, id=request.user.id)
#         userInfo.slot_booked_time=finalTimes
#         center=userInfo.center
#         userInfo.save()
#         print(time)
#         time    
#         context = {
#             'username': username,
#             'email': email,
#             'slot_booked':slot_booked,
#             'center':center,
#             'selected_time_slots':selected_time_slots
#         }

#         return render(request, 'home.html', context)
#     else:
#         return render(request, 'home.html') 

# def map(request):
#     return render(request,'map.html')

# def deleteSpots(time):
#     currentKey=get_key_from_time()
#     finalTimes=remove_characters_less_than(time,currentKey)  
#     return finalTimes
    
# def remove_characters_less_than(input_string, key):
#     result_string = ''.join(char for char in input_string if char >= key)
#     return result_string


# from django.utils.timezone import localtime



# import os
# from django.core.wsgi import get_wsgi_application



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
# application = get_wsgi_application()



# from datetime import datetime, timedelta

# def get_key_from_time():
#     time_slots = {
#         '0': ('11:00 AM', '12:00 PM'),
#         '1': ('12:00 PM', '1:00 PM'),
#         '2': ('1:00 PM', '2:00 PM'),
#         '3': ('2:00 PM', '3:00 PM'),
#         '4': ('3:00 PM', '4:00 PM'),
#         '5': ('4:00 PM', '5:00 PM'),
#         '6': ('5:00 PM', '6:00 PM'),
#         '7': ('6:00 PM', '7:00 PM'),
#         '8': ('7:00 PM', '8:00 PM'),
#         '9': ('8:00 PM', '9:00 PM'),
#     }

#     current_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

  
#     current_time_str = current_time.strftime('%I:%M %p')
#     print(current_time_str)


#     current_time_dt = datetime.strptime(current_time_str, '%I:%M %p')


#     for key, (start_time_str, end_time_str) in time_slots.items():
#         start_time = datetime.strptime(start_time_str, '%I:%M %p')
#         end_time = datetime.strptime(end_time_str, '%I:%M %p')

#         if start_time <= current_time_dt <= end_time:
#             print("Current Key:", key)
#             return key


#     return None


# def dyp(request):
#     return render(request,'dyp.html')
# def about(request):
#     return render(request,'about.html')
# def services(request):
#     return render(request,'services.html')
# def profile(request):
#     return render(request,'profile.html')




# from .forms import ContactForm

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = request.POST['name']
#             email = request.POST['email']
#             message = request.POST['message']
#             form.save()
#             return render(request, 'contact.html', {'thank': "Message Sent SuccessFully !"}) # Replace 'thank_you' with your thank you page name or URL
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import ParkingSpot ,CustomUser
from .forms import BookingForm
from django.contrib.auth import authenticate, login, logout
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt  
from django.contrib.auth.decorators import login_required

time_slots = {
        '0': '11:00 AM - 12:00 PM',
        '1': '12:00 PM - 1:00 PM',
        '2': '1:00 PM - 2:00 PM',
        '3': '2:00 PM - 3:00 PM',
        '4': '3:00 PM - 4:00 PM',
        '5': '4:00 PM - 5:00 PM',
        '6': '5:00 PM - 6:00 PM',
        '7': '6:00 PM - 7:00 PM',
        '8': '7:00 PM - 8:00 PM',
        '9': '8:00 PM - 9:00 PM',
}

def list(request):
    spots=ParkingSpot.objects.all()
    print(spots)
    return render(request,'spot_list.html',{'spots':spots})

def booking(request):
    return render(request, 'book_spot.html')

def parking_spot_detail(request, parking_spot_id):
    time_slots = {
        '0': '11:00 AM - 12:00 PM',
        '1': '12:00 PM - 1:00 PM',
        '2': '1:00 PM - 2:00 PM',
        '3': '2:00 PM - 3:00 PM',
        '4': '3:00 PM - 4:00 PM',
        '5': '4:00 PM - 5:00 PM',
        '6': '5:00 PM - 6:00 PM',
        '7': '6:00 PM - 7:00 PM',
        '8': '7:00 PM - 8:00 PM',
        '9': '8:00 PM - 9:00 PM',
}
    parking_spot = get_object_or_404(ParkingSpot, id=parking_spot_id)
    name = parking_spot.name

    available_slots = parking_spot.available
    center=parking_spot.center
    newlist = [char for char in available_slots]
    currentKey=get_key_from_time()
    time_slots = {key: time_slots[key] for key in time_slots if key not in newlist and key >currentKey}
    print(time_slots)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, slot_info=time_slots)
        if form.is_valid():
            selected_slot = form.cleaned_data['available_slots']

            print(selected_slot)
            spots=''.join(selected_slot)
            
            updatedSlots=parking_spot.available + spots
            request.session['selected_slot']=spots  
            request.session['center']=center       
            request.session['parking_spot_id'] = parking_spot_id
            request.session['updatedSlots'] = updatedSlots
            return redirect('booking_success',name=name,spots=spots)
    else:
        form = BookingForm(slot_info=time_slots)

    return render(request, 'trial.html', {'form': form, 'name': name})


def booking_success(request, name,spots):
    time_slots = {
        '0': '11:00 AM - 12:00 PM',
        '1': '12:00 PM - 1:00 PM',
        '2': '1:00 PM - 2:00 PM',
        '3': '2:00 PM - 3:00 PM',
        '4': '3:00 PM - 4:00 PM',
        '5': '4:00 PM - 5:00 PM',
        '6': '5:00 PM - 6:00 PM',
        '7': '6:00 PM - 7:00 PM',
        '8': '7:00 PM - 8:00 PM',
        '9': '8:00 PM - 9:00 PM',
}
    newlist=[]
    for i in spots:
        newlist.append(time_slots[i])
    print(newlist)
    request.session['newlist'] = newlist
    request.session['name'] = name
    bill=30*(len(spots))
    razorpaybill=30*(len(spots))*100
    center=request.session.get('center')
    return render(request, 'success.html', {'name': name,'spots':newlist,'bill':bill,'center':center,'razorpaybill':razorpaybill})







def create_order(request):
    if request.method == 'POST':
        amount = 50000  # amount in paisa
        client = razorpay.Client(auth=('rzp_test_GtzVv7rlxPUO82', 'w4Np3Z2QUXErexJUUQWBtdGE'))
        payment_data = {
            'amount': 50000,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': 1
        }
        order = client.order.create(data=payment_data)

        return render(request, 'suceess.html', {'order': order})
    return render(request, 'payment.html')


@csrf_exempt 
def handle_payment(request):
    parking_spot_id=request.session.get('parking_spot_id') 
    userInfo = get_object_or_404(CustomUser, id=request.user.id)
    name=request.session.get('name')
    userInfo.slot_booked=name
    spots=request.session.get('selected_slot')
    newlist=request.session.get('newlist')
    center=request.session.get('center')
    userInfo.slot_booked_time=request.session.get('updatedSlots')
    updatedSlots=request.session.get('updatedSlots')
    parking_spot = get_object_or_404(ParkingSpot, id=parking_spot_id)
    userInfo.location=parking_spot.location
    userInfo.center=parking_spot.center
    parking_spot.available=updatedSlots
    userInfo.save()
    parking_spot.save()
   
    return render(request, 'payment.html' ,{'name':name,'newlist':newlist,'center':center})
    

def payment(request):
    return render(request,'payment.html')





def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login') 
from .forms  import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            # Redirect to the home page or another page
            return redirect('login')
    else:
        form = CustomUserCreationForm() 

    return render(request, 'signup.html', {'form': form})
time_slots = {
        '0': '11:00 AM - 12:00 PM',
        '1': '12:00 PM - 1:00 PM',
        '2': '1:00 PM - 2:00 PM',
        '3': '2:00 PM - 3:00 PM',
        '4': '3:00 PM - 4:00 PM',
        '5': '4:00 PM - 5:00 PM',
        '6': '5:00 PM - 6:00 PM',
        '7': '6:00 PM - 7:00 PM',
        '8': '7:00 PM - 8:00 PM',
        '9': '8:00 PM - 9:00 PM',
}

@login_required(login_url='login') 
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        slot_booked = request.user.slot_booked
        id= request.user.id
        time= request.user.slot_booked_time
        print("time",time)
        selected_time_slots =[time_slots[slot] for slot in time]
        print(selected_time_slots)
        finalTimes=deleteSpots(time)  
        userInfo = get_object_or_404(CustomUser, id=request.user.id)
        userInfo.slot_booked_time=finalTimes
        center=userInfo.center
        userInfo.save()
        print(time)
        time    
        context = {
            'username': username,
            'email': email,
            'slot_booked':slot_booked,
            'center':center,
            'selected_time_slots':selected_time_slots
        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html') 

def map(request):
    return render(request,'map.html')

def deleteSpots(time):
    currentKey=get_key_from_time()
    finalTimes=remove_characters_less_than(time,currentKey)  
    return finalTimes
    
def remove_characters_less_than(input_string, key):
    result_string = ''.join(char for char in input_string if char >= key)
    return result_string


from django.utils.timezone import localtime



import os
from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
application = get_wsgi_application()



from datetime import datetime, timedelta

def get_key_from_time():
    time_slots = {
        '0': ('11:00 AM', '12:00 PM'),
        '1': ('12:00 PM', '1:00 PM'),
        '2': ('1:00 PM', '2:00 PM'),
        '3': ('2:00 PM', '3:00 PM'),
        '4': ('3:00 PM', '4:00 PM'),
        '5': ('4:00 PM', '5:00 PM'),
        '6': ('5:00 PM', '6:00 PM'),
        '7': ('6:00 PM', '7:00 PM'),
        '8': ('7:00 PM', '8:00 PM'),
        '9': ('8:00 PM', '9:00 PM'),
    }

    current_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
  
    current_time_str = current_time.strftime('%I:%M %p')
    print(current_time_str)


    current_time_dt = datetime.strptime(current_time_str, '%I:%M %p')


    for key, (start_time_str, end_time_str) in time_slots.items():
        start_time = datetime.strptime(start_time_str, '%I:%M %p')
        end_time = datetime.strptime(end_time_str, '%I:%M %p')

        if start_time <= current_time_dt <= end_time:
            print("Current Key:", key)
            return key


    return None


def dyp(request):
    return render(request,'dyp.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def profile(request):
    return render(request,'profile.html')




from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            form.save()
            return render(request, 'contact.html', {'thank': "Message Sent SuccessFully !"}) # Replace 'thank_you' with your thank you page name or URL
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

