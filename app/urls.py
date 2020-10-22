from django.urls import path
from . import views


urlpatterns = [
    path('exer/', views.exer, name="exer"),
    path('', views.opening, name="opening"),
    path('home/', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('make/', views.make, name="make"),
    path('rank/', views.rank, name="rank"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('mypage/<str:pk_test>/', views.myPage,name="mypage"),
    # path('cart/', views.cart, name="cart"),
    # path('history/', views.history, name="history"),
    # path('modify/', views.modify, name="modify"),
    # path('myrank/', views.myrank, name="myrank"),
    # path('save/', views.save, name="save"),
    path('pay/', views.pay, name="pay"),
    # path('create/', views.createOrder, name="create"),
    # path('delete/<int:pk>', views.deleteOrder, name="delete"),
    # path('update/<int:pk>', views.updateOrder, name="update"),

    # ##
    # path('get', views.get, name = "get"),
    # # path('rb', views.recipeBase, name = "recipeBase"),
    # # path('ri', views.recipeIngredient, name = "recipeIngredient"),
    # # path('rp', views.recipeProcess, name = "recipeProcess")
    # path('detail', views.detail, name = "detail")

     #path('nav/', views.nav, name="nav"),

    # # 산하추가
    # path('index_login/<str:pk_test>/', views.index_login, name="index_login"),

    path('make_search/', views.make_search,name="make_search"),

    
]



    

