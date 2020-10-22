from django.db import models
from django.contrib.auth.models import User
from .models import *
# Create your models here.

# user
class Customer(models.Model):
    GRADE = (
        ('MVG','MVG'),
        ('VIP','VIP'),
        ('GOLD','GOLD'),
        ('ACE','ACE'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # 아이디
    name = models.CharField(max_length=200, null=True) # 이름
    email = models.EmailField(max_length=200, null=True) # 이메일 
    # date_created = models.DateTimeField(auto_now_add=True, null=True) # 아이디 생성시간
    rank = models.IntegerField(max_length=None, null=True) # 순위
    grade = models.CharField(max_length=200, null=True, choices=GRADE) # 등급
    
    def __str__(self):
        return self.name

# 상품
class Item(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #id
    name = models.CharField(max_length=200, null=True) # 상품명
    hastag = models.CharField(max_length=200, null=True) # 해시태그
    price = models.IntegerField(max_length=None, null=True) # 상품가격
    image = models.ImageField(upload_to='images/', blank=True, null=True) # 이미지
    # save = models.IntegerField(max_length=None, null=True) # 상품 찜 / 하트눌러서 찜하면 1, 안하면 0
    
    def __str__(self):
        return self.name


# 선물세트		
class Set(models.Model):

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #id
    name = models.CharField(max_length=200, null=True) # 세트명
    price = models.IntegerField(max_length=None, null=True) # 세트가격
    hastag = models.CharField(max_length=200, null=True) # 세트 해시태그
    like = models.IntegerField(max_length=None, null=True) # 좋아요수 
    sales = models.IntegerField(max_length=None, null=True) # 판매량
    cart = models.IntegerField(max_length=None, null=True) # 장바구니 / 장바구니에 있으면 1, 없으면 0
    # save = models.IntegerField(max_length=None, null=True) # 세트 찜  / 하트 눌러서 찜하면 1, 안하면 0
    order = models.CharField(max_length=200, null=True) # 주문일 / 주문하면 주문날짜, 안하면 빈값
    # packing = models.IntegerField(max_length=None, null=True) # 포장지 / 포장지에 따라 0,1,2 숫자 부여(선물세트 이미지를 이 포장지 이미지로 대체)
    packing_test = models.TextField(null=True) # 포장지 문구
    item1 = models.CharField(max_length=200, null=True) # 세트명
    
    #form = models.CharField(max_length=200, null=True, choices=OPTION) # 구성
    # product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    # item1 = models.CharField(max_length=200, null=True) # 세트명 / 세트에 들어가는 아이템1 
    # item2 = models.CharField(max_length=200, null=True) # 세트명 / 세트에 들어가는 아이템2
    # item3 = models.CharField(max_length=200, null=True) # 세트명 / 세트에 들어가는 아이템3
    # item4 = models.CharField(max_length=200, null=True) # 세트명 / 세트에 들어가는 아이템4

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)