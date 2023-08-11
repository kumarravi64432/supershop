from django.db import models

# Create your models here.
class Maincategory(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.id)+"/"+self.name

class Subcategory(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)+"/"+self.name


class Brand(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=30)
    pic =models.ImageField(upload_to="upload/brand")

    def __str__(self):
        return str(self.id)+"/"+self.name

class Product(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=30)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    baseprice=models.IntegerField()
    discount=models.IntegerField()
    finalprice=models.IntegerField()
    stock=models.IntegerField(default=True)
    color=models.CharField(max_length=30)
    size=models.CharField(max_length=10)
    description=models.TextField()
    pic1=models.ImageField(upload_to="upload/product",null=True,blank=True)
    pic2=models.ImageField(upload_to="upload/product",default=None,blank=True,null=True)
    pic3=models.ImageField(upload_to="upload/product",default=None,blank=True,null=True)
    pic4=models.ImageField(upload_to="upload/product",default=None,blank=True,null=True)
    def __str__(self):
        return str(self.id)+"/"+self.name

class Buyer(models.Model):  #We did not use password field in buyer table 
    id = models.AutoField(primary_key=True) 
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30, unique=True)
    email=models.EmailField(max_length=30)
    address=models.TextField(default="",blank=True,null=True)
    pin=models.IntegerField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=15,default="")
    city=models.CharField(max_length=50,default="",null=True,blank=True)
    state=models.CharField(max_length=40,default="",null=True,blank=True)
    pic=models.ImageField(upload_to="uploads/users",default="",null=True,blank=True)
    otp=models.IntegerField(default=None,blank=None,null=True)

    def __str__(self):
        return str(self.id)+"/"+self.name+"/"+self.username

class Wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)+"/"+self.buyer.username
    
orderStatusOption=(
    (0,'Order is Placed'),
    (1,'Order is Packed'),
    (2,'Ready to dispatch'),
    (3,'dispatched'),
    (4,'Out for delivery'),
    (5,'Delivered'),
)
paymentStatusOption=(
    (0,'Pending'),
    (1,'Done'),   
)
paymentModeOption=(
    (0,'COD'),
    (1,'NetBanking'),
    
)
class Checkout(models.Model):
    id=models.AutoField(primary_key=True)
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE) 
    orderstatus=models.IntegerField(choices=orderStatusOption,default=0)   
    paymentstatus=models.IntegerField(choices=paymentStatusOption,default=0)   
    paymentmode=models.IntegerField(choices=paymentModeOption,default=0) 
    subtotal=models.IntegerField()  
    shipping=models.IntegerField()  
    total=models.IntegerField()  
    rppid=models.CharField(max_length=20,default="",null=True,blank=True)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.buyer.username

class CheckoutProduct(models.Model):
    id=models.AutoField(primary_key=True)
    checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return str(self.id)
    
    
class Newslatter(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(unique=True,max_length=50)

    def __str__(self):
        return str(self.id)+" "+self.email

    
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=50)
    phone=models.CharField(max_length=15)
    subject=models.TextField()
    message=models.TextField()
    status=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"/"+self.email

class Testimonial(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    message=models.TextField()
    pic=models.ImageField(upload_to='uploads/testimonials')

    def __str__(self):
        return str(self.id)+"/"+self.name