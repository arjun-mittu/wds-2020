from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm,tradeform,requestsellform,tradereqform,reportform
from django.urls import reverse
from .models import Stock,trade,stock_list,tradereq,Report,StockList
import json
from django.db.models import Q
def home(request):
    return render(request,"home.html", {'messages': messages.get_messages(request)})

def news(request):
    return render(request,"news.html")


def register(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(data=request.POST)

        if (form.is_valid()):
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            print(form.errors)
    else:
        form=RegisterForm()
        
    return render(request, 'register.html', {'form': form})





def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)


        user=authenticate(username=username,password=password)

        if user is not None:
                login(request,user)
        else:
            print("false login")
            messages.error(request, f'Invalid Teamname or Password')
            return redirect('core:userlogin')
        return redirect('/')
    else:
        print("render part ran successfully")
        return render(request,'userlogin.html')

@login_required
def userlogout(request):
    print("logout")
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    user_dashdata = Stock.objects.filter(user=request.user)
    dash_dic = {'dashdata':user_dashdata}
    return render(request,'dashboard.html', {'dashdata':user_dashdata})

def stock_display(request):
    context = {
      'posts': StockList.objects.all()
    }
    return render(request,'stocks.html', context)


class Trade(ListView):
    def get(self, *args, **kwargs):
        form = tradeform()
        context = {
            'form':form,
        }
        return render(self.request, 'buy-sell-form.html', context)

    def post(self, *args, **kwargs):
        form = tradeform(self.request.POST or None)
        try:
            if form.is_valid():
                seller=form.cleaned_data.get('seller')
                stock=form.cleaned_data.get('stock')
                numberofstocks=form.cleaned_data.get('numberofstocks')
                priceperstock=form.cleaned_data.get('priceperstock')
               # userbalance=form.cleaned_data.get('userbalance')
                buyer=form.cleaned_data.get('buyer')
                trading=trade.objects.create(
                    seller=seller,
                    stock=stock,
                    numberofstocks=numberofstocks,
                    priceperstock=priceperstock,
                    buyer=buyer,
                    #userbalance=userbalance,
                )
                print(priceperstock)
                print(numberofstocks)
                stock_seller=Stock.objects.get(user=seller)
                print(stock_seller)
                          
                stock_buyer=Stock.objects.get(user=buyer)
                print(stock_buyer)
                '''for st in stock_list:
                    if stock==st[0]:
                        stock_seller.st[0]-=numberofstocks
                        stock_seller.userbalance+=priceperstock*numberofstocks
                        stock_buyer.st[0]+=numberofstocks
                        stock_buyer.userbalance-=priceperstock*numberofstocks
                        stock_seller.save()
                        stock_buyer.save()'''

                if stock=="ASHOKLEY":
                    stock_seller.ASHOKLEY-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.ASHOKLEY+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()                 
                    stock_buyer.save()
                elif stock=="WIPRO":
                    stock_seller.WIPRO-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.WIPRO+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()         
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="RAJESHEXPO":
                    stock_seller.RAJESHEXPO-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.RAJESHEXPO+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="AMBUJACEM":
                    stock_seller.AMBUJACEM-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.AMBUJACEM+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="MM":
                    stock_seller.MM-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.MM+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="ONGC":
                    stock_seller.ONGC-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.ONGC+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="DMART":
                    stock_seller.DMART-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.DMART+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="SUNPHARMA":
                    stock_seller.SUNPHARMA-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.SUNPHARMA+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="HINDUUNILVR":
                    stock_seller.HINDUUNILVR-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.HINDUUNILVR+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="ADANIPOWER":
                    stock_seller.ADANIPOWER-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.ADANIPOWER+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                return redirect('/')
        except ObjectDoesNotExist:
                messages.error(self.request, "fill the form correctly")
                return redirect("/")
@login_required
def reqcreate(request):
    user=request.user
    if request.method=='POST':
        form = tradereqform(request.POST or None)
        if form.is_valid():
                sender=user
                receiver=form.cleaned_data.get('receiver')
                action=form.cleaned_data.get('action')
                stock=form.cleaned_data.get('stock')
                numberofstock=form.cleaned_data.get('numberofstocks')
                priceperstock=form.cleaned_data.get('priceperstock')
                amount = numberofstock*priceperstock
                stock_request_sender=Stock.objects.get(user=sender)
                status='pending'
                if action=='buy':
                    if (amount<=stock_request_sender.userbalance):
                        request_trade=tradereq.objects.create(
                            sender=sender,
                            receiver=receiver,action=action,
                            stock=stock,
                            numberofstocks=numberofstock,
                            priceperstock=priceperstock,
                            is_active=True,
                        )
                        return redirect('core:sentreq')
                    else:
                        messages.error(request, f'Insufficient Balance for transaction!!')
                elif action=='sell':
                    if stock=='MM':
                        if (numberofstock<=stock_request_sender.MM):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='SUNPHARMA':
                        if (numberofstock<=stock_request_sender.SUNPHARMA):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='ADANIPOWER':
                        if (numberofstock<=stock_request_sender.ADANIPOWER):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='TATASTEEL':
                        if (numberofstock<=stock_request_sender.TATASTEEL):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='INDIAMART':
                        if (numberofstock<=stock_request_sender.INDIAMART):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='RELIANCE':
                        if (numberofstock<=stock_request_sender.RELIANCE):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='INFOSYS':
                        if (numberofstock<=stock_request_sender.INFOSYS):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='BHARTIARTL':
                        if (numberofstock<=stock_request_sender.BHARTIARTL):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='ITC':
                        if (numberofstock<=stock_request_sender.ITC):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='HDFCBANK':
                        if (numberofstock<=stock_request_sender.HDFCBANK):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='CIPLA':
                        if (numberofstock<=stock_request_sender.CIPLA):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='TCS':
                        if (numberofstock<=stock_request_sender.TCS):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='LT':
                        if (numberofstock<=stock_request_sender.LT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='ASIANPAINT':
                        if (numberofstock<=stock_request_sender.ASIANPAINT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='ICICIPRULI':
                        if (numberofstock<=stock_request_sender.ICICIPRULI):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('core:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    
 
    return render(request,'create_request.html',{'form':tradereqform})
@login_required
def report(request):
    form = reportform()
    if request.method=='POST':
        form = reportform(request.POST or None)
        if form.is_valid():
            obj = Report()
            obj.reporter=request.user
            obj.reporting=form.cleaned_data.get('reporting')
            print(obj.reporter)
            print(obj.reporting)
            obj.save()
        else:
            form=reportform()
        return redirect('core:dashboard')
    return render(request, 'report.html', {'form':form})
@login_required
def received_request(request):
    user=request.user
    requests_pending=tradereq.objects.order_by('-id').filter(receiver=user,is_active=True)
    return render(request,'received_request.html',{'requests':requests_pending})

@login_required
def sent_request(request):
    user=request.user
    sent_pending=tradereq.objects.order_by('-id').filter(sender=user,is_active=True)
    return render(request,'sent_requests.html',{'requests':sent_pending})

@login_required
def history(request):
    user=request.user
    transactions=tradereq.objects.order_by('-id').filter(sender=user)
    return render(request,'transaction-history.html',{'requests':transactions})

@login_required
def all_history(request):
    user=request.user
    #transactions=tradereq.objects.order_by('-id').filter(Q(receiver=user) | Q(sender=user))
    comb_query = tradereq.objects.filter(sender=user) | tradereq.objects.filter(receiver=user)
    final_query = comb_query.filter(status='accepted')
    transactions=final_query.order_by('-id')
    return render(request,'transaction-log.html',{'requests':transactions})


"""
@login_required
def accept_request(request,*args, **kwargs):
    user=request.user
    payload={}
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.id(pk=tradereq_id)
            if trade_request.receiver==user:
                if trade_request:
                    trade_request.accept()
                    payload['response']="request accepted"
                else:
                    payload['response']="something went wrong"
            else:
                payload['response']="not yours request"
        else:
            payload['response']="unable not accepted"
    else:
        payload['response']="you must be authenticated to accpet a friend request"
    return HttpResponse(json.dumps(payload),content_type="application/json")
"""

@login_required 
def accept_request(request,*args, **kwargs):
    user =request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                msg = trade_request.accept()
                print(msg)
                messages.error(request, msg)
                return redirect("core:receivedreq")

@login_required
def decline_request(request,*args, **kwargs):
    user=request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                trade_request.decline()
                return redirect("core:receivedreq")


@login_required
def cancel_request(request,*args, **kwargs):
    user=request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                trade_request.cancel()
                return redirect("core:sentreq")


