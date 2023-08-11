from django import template

register = template.Library()

@register.filter(name="paymentMode")
def paymentMode(Request, num):
    if(num==0):
        return "COD"
    else:
        return "NetBanking"
    

@register.filter(name="paymentStatus")
def paymentStatus(Request, num):
    if(num==0):
        return "Pending"
    else:
        return "Done"
    
@register.filter(name="orderStatus")
def orderStatus(Request, num):
    if(num==0):
        return "Order is Placed"
    elif(num==1):
        return "Order is Dispatch"
    elif(num==2):
        return "Ready is Dispatch"
    elif(num==3):
        return "Dispatched"
    elif(num==4):
        return "Delivered"
    else:
        return "Done"

@register.filter(name="paymentCondition")
def paymentCondition (mode,status):
    if(mode==1 and status==0):
        return True
    else:
        return False