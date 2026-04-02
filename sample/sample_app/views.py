from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from sample_app.models import deliv_form, bid_table
import requests
# Create your views here.

def test(request):
	return HttpResponse("Test Page")
def home(request):
	import datetime
	import pytz

	x =datetime.datetime.now()
	x = pytz.utc.localize(x)
	trl_obj1 = bid_table.objects.all().order_by('bid_amount')

	trl_obj = deliv_form.objects.all().order_by('-time_stamp')
	return render(request,'sample_app/home.html',{'trl_obj':trl_obj,'res':x, 'trl_obj1':trl_obj1})

def register(request):
	return render(request,'sample_app/register.html')

def post(request):
	import datetime
	import pytz
	x =datetime.datetime.now()
	x = pytz.utc.localize(x)
	list_deliv_form_id=[]
	trl_obj = deliv_form.objects.all().order_by('-time_stamp')
	trl_obj1 = bid_table.objects.all().order_by('-time_stamp')

	for i in trl_obj1:
		list_deliv_form_id.append(i.deliv_form_id)
	return render(request,'sample_app/post.html',{'trl_obj':trl_obj,'res':x,'list_deliv_form_id':list_deliv_form_id})

def login_user(request):
	return render(request,'sample_app/login.html')

def table(request):
	return render(request,'sample_app/table.html')

def profile(request):
	import datetime
	import pytz
	x =datetime.datetime.now()
	x = pytz.utc.localize(x)
	list_deliv_form_id=[]
	trl_obj = deliv_form.objects.all().order_by('-time_stamp')
	trl_obj1 = bid_table.objects.all().order_by('-time_stamp')

	for i in trl_obj1:
		list_deliv_form_id.append(i.deliv_form_id)
	return render(request,'sample_app/profile.html',{'trl_obj':trl_obj,'res':x,'list_deliv_form_id':list_deliv_form_id})

def add_auction(request):
	return render(request,'sample_app/add_auction.html')

def logout_user(request):
	logout(request)
	return render(request,'sample_app/home.html')

def reg_post(request):
	try:
		if request.method=='POST':
			username=request.POST['username']
			email=request.POST['email']
			password=request.POST['password']
			password2=request.POST['password2']
			if password == password2:
				#request.session['uname1']=username
				user=User.objects.create_user(username=username,email=email,password=password)
				user.save()
				messages.success(request,'registered successfully')
				return render(request,'sample_app/login.html')
			else:
				messages.error(request,'registration failed')
				return render(request,'sample_app/register.html')
	except:
		messages.error(request,'registration failed')
		return render(request,'sample_app/register.html')



def add_login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:

			login(request,user)
			return HttpResponseRedirect('home')
		else:
			messages.error(request,'credantials failed')
			return HttpResponseRedirect('login_user')
	messages.error(request,'fill all credantials ')
	return HttpResponseRedirect('login_user')


def auct_form(request):
	import random
	p=[]
	trl_obj = deliv_form.objects.all()
	for i in trl_obj:
		p.append(i)

	c_id = random.randrange(10000,99999)
	while c_id in p:
		c_id = random.randrange(10000,99999)
		continue

	import datetime
	x = datetime.datetime.now()
		#t1 = x.year
		#t2 = x.strftime("%d")
		#t3 = x.strftime("%B")
		#t4 = x.strftime("%X")
	reg_obj1 = deliv_form.objects.create(
		deliv_form_id=c_id,
		auct_year=x.year,
		auct_time=x.strftime("%X"),
		auct_month=x.strftime("%B"),
		auct_day=x.strftime("%d"),
		username=request.user.username,
		sender_name=request.POST.get('s_name'),
		sender_email_id=request.POST.get('s_email'),
		sender_phone_no=request.POST.get('s_Phone_no'),
		sen_d_no=request.POST.get('s_d_no'),
		sen_city=request.POST.get('s_city'),
		sen_state=request.POST.get('s_state'),
		sen_district=request.POST.get('s_district'),
		sen_pincode=request.POST.get('s_pincode'),
		sen_land_mark=request.POST.get('s_land_mark'),
		rec_name=request.POST.get('r_name'),
		rec_email_id=request.POST.get('r_email'),
		rec_phone_no=request.POST.get('r_phone_no'),
		rec_d_no=request.POST.get('r_d_no'),
		rec_city=request.POST.get('r_city'),
		rec_state=request.POST.get('r_state'),
		rec_district=request.POST.get('r_district'),
		rec_pincode=request.POST.get('r_pincode'),
		rec_land_mark=request.POST.get('r_land_mark'),
		about_product=request.POST.get('about_prod'),
		pro_waight=request.POST.get('p_waight'),
		pickup_time=request.POST.get('pick_time'),
		auction_time=request.POST.get('auct_time'),
		time_stamp=datetime.datetime.now(),
		)
	reg_obj1.save()
	messages.success(request,'Aucton Form Submitted Successfully')
	return HttpResponseRedirect('profile')
	



def bid_form(request):
	import datetime

	list_deliv_form_id = []
	list_bid_amount = []
	trl_obj1 = bid_table.objects.all()

	for i in trl_obj1:
		list_deliv_form_id.append(int(i.deliv_form_id))



	for i in trl_obj1:
		if int(request.POST.get('custId')) == i.deliv_form_id:
			list_bid_amount.append(int(i.bid_amount))

	if int(request.POST.get('custId')) in list_deliv_form_id:
		if int(request.POST.get('bid_amount1')) < min(list_bid_amount):
			reg_obj2 = bid_table.objects.create(
				username=request.user.username,
				deliv_form_id=request.POST.get('custId'),
				time_stamp=datetime.datetime.now(),
				bid_amount=request.POST.get('bid_amount1'),
				)
			reg_obj2.save()
			
			return HttpResponseRedirect('home')

		else:
			messages.error(request,'please bid lower amount')
			
			return HttpResponseRedirect('home')

	else:
		reg_obj2 = bid_table.objects.create(
			username=request.user.username,
			deliv_form_id=request.POST.get('custId'),
			time_stamp=datetime.datetime.now(),
			bid_amount=request.POST.get('bid_amount1'),
			)
		reg_obj2.save()
		
		return HttpResponseRedirect('home')

def add_status_disagreed(request):
	u_id =request.POST.get('U_id')
	v_id =request.POST.get('V_id')

	list_bid_amount=[]

	trl_obj1 = bid_table.objects.all().order_by('-time_stamp')
	for i in trl_obj1:
		if int(i.deliv_form_id) == int(u_id):
			list_bid_amount.append(i.bid_amount)
	for j in trl_obj1:
		if int(j.bid_amount)==min(list_bid_amount):
			achived_by_p=j.username


	deliv_form.objects.filter(deliv_form_id=u_id).update(auction_status=v_id)
	deliv_form.objects.filter(deliv_form_id=u_id).update(achived_by=achived_by_p)
	deliv_form.objects.filter(deliv_form_id=u_id).update(min_bid_amnt=min(list_bid_amount))
	return HttpResponseRedirect('profile')


def add_status_received(request):
	u_id =request.POST.get('U_id')
	v_id =request.POST.get('V_id')


	deliv_form.objects.filter(deliv_form_id=u_id).update(auction_status=v_id)
	return HttpResponseRedirect('achived')

def add_status_closed(request):
	u_id =request.POST.get('U_id')
	v_id =request.POST.get('V_id')


	deliv_form.objects.filter(deliv_form_id=u_id).update(auction_status=v_id)
	return HttpResponseRedirect('profile')


def add_status_agreed(request):
	u_id =request.POST.get('U_id')
	v_id =request.POST.get('V_id')
	list_bid_amount=[]

	trl_obj1 = bid_table.objects.all().order_by('-time_stamp')
	for i in trl_obj1:
		if int(i.deliv_form_id) == int(u_id):
			list_bid_amount.append(i.bid_amount)
	for j in trl_obj1:
		if int(j.bid_amount)==min(list_bid_amount):
			achived_by_p=j.username

	deliv_form.objects.filter(deliv_form_id=u_id).update(auction_status=v_id)
	deliv_form.objects.filter(deliv_form_id=u_id).update(achived_by=achived_by_p)
	deliv_form.objects.filter(deliv_form_id=u_id).update(min_bid_amnt=min(list_bid_amount))
	return HttpResponseRedirect('profile')

def achived(request):
	import datetime
	import pytz
	x =datetime.datetime.now()
	x = pytz.utc.localize(x)



	list_bid_amount=[]
	list_bid_id=[]

	trl_obj = deliv_form.objects.all().order_by('-time_stamp')


	trl_obj1 = bid_table.objects.all().order_by('-time_stamp')
	for i in trl_obj1:
		list_bid_id.append(i.deliv_form_id)
	
	

	return render(request,'sample_app/achived.html',{'trl_obj':trl_obj,'res':x,'list_bid_id':list_bid_id, 'trl_obj1':trl_obj1})



def edit_profile(request):
	return render(request,'sample_app/edit_profile.html')	