from django.db import models

# Create your models here.
class Axf(models.Model):
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract='true'

class axf_wheel(Axf):
    class Meta:
        db_table='axf_wheel'


class axf_nav(Axf):
    class Meta:
        db_table='axf_nav'

class axf_mustbuy(Axf):
    class Meta:
        db_table='axf_mustbuy'

class axf_shop(Axf):
    class Meta:
        db_table='axf_shop'

class axf_mainshow(Axf):
    '''
    trackid,name,img,categoryid,brandname,
    img1,childcid1,productid1,longname1,price1,marketprice1,
    img2,childcid2,productid2,longname2,price2,marketprice2,
    img3,childcid3,productid3,longname3,price3,marketprice3
    '''
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=10)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)



    class Meta:
        db_table='axf_mainshow'

class axf_foodtypes(models.Model):
    #typeid, typename, childtypenames, typesort

    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'

class axf_goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=0)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=0)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table='axf_goods'


class user(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    sex =  models.CharField(max_length=2)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

class role(models.Model):
    r_name = models.CharField(max_length=20)
    r_desc = models.CharField(max_length=32)

    class Meta:
        db_table = 'role'


class auth(models.Model):
    a_name = models.CharField(max_length=20)
    a_path = models.CharField(max_length=20)

    class Meta:
        db_table = 'auth'

class user_role(models.Model):
    uid = models.ForeignKey(user, on_delete=models.PROTECT)
    rid = models.ForeignKey(role, on_delete=models.PROTECT)
    class Meta:
        db_table = 'user_role'


class role_auth(models.Model):
    rid = models.ForeignKey(role, on_delete=models.PROTECT)
    aid = models.ForeignKey(auth, on_delete=models.PROTECT)

    class Meta:
        db_table = 'role_auth'


class axf_shopcar(models.Model):
    user = models.ForeignKey(user,on_delete=models.PROTECT)
    goods = models.ForeignKey(axf_goods, on_delete=models.PROTECT)
    number = models.IntegerField(default=1)
    isselect = models.BooleanField(default=False)

    class Meta:
        db_table = 'shopcar'

#创建订单
class axf_order(models.Model):
    user  = models.ForeignKey(user)
    #定单状态 0 未付款 1 已付款代发货  2已发货 3已退款 4已评价
    status = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    createdate = models.DateTimeField(auto_now=True)
    upddate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'

class axf_order_goods(models.Model):

    order = models.ForeignKey(axf_order)
    goods = models.ForeignKey(axf_goods)
    number = models.IntegerField(default=1)
    money = models.FloatField()

    class Meta:
        db_table = 'order_goods'