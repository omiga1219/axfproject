import hashlib
import random

from PIL import Image, ImageDraw, ImageFont

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from myapp.models import axf_wheel, axf_nav, axf_mainshow, axf_mustbuy, axf_shop, axf_foodtypes, axf_goods, user, role, \
    user_role, auth, role_auth, axf_shopcar, axf_order, axf_order_goods


#主页面
def main(request):
    return render(request,'main.html')

#首页
def index(request):

    wheels = axf_wheel.objects.all()
    navs = axf_nav.objects.all()
    buys = axf_mustbuy.objects.all()
    shops = axf_shop.objects.all()
    shops_0 = shops[0]
    shops_1 = shops[1:3]
    shops_2 = shops[3:7]
    shops_3 = shops[7:11]
    shows = axf_mainshow.objects.all()


    data={
        'title':'首页',

        'wheels': wheels,
        'navs': navs,
        'buys': buys,
        'shops_0': shops_0,
        'shops_1': shops_1,
        'shops_2': shops_2,
        'shops_3': shops_3,
        'shows': shows,
    }
    return render(request, 'index.html',data)

#商品
@cache_page(300)
def market(request):
    #获得大类typeid
    typeid=request.GET.get('typeid') if request.GET.get('typeid') else '104749'
    #获得小类childcid
    childcid = request.GET.get('childcid') if request.GET.get('childcid') else '0'
    #获得sort排序序号
    sort = request.GET.get('sort') if request.GET.get('sort') else '0'

    foodtypes = axf_foodtypes.objects.all()
    goodlist = axf_goods.objects.filter(categoryid=typeid)

    f = axf_foodtypes.objects.filter(typeid=typeid).first().childtypenames.split("#")
    flist=[]
    for i in f:
        flist.append(i.split(":"))
    print(flist)


    if childcid !='0':
        goodlist = goodlist.filter(childcid=childcid)


    #排序
    if sort=='1':
        goodlist = goodlist.order_by('productid')
    if sort=='2':
        goodlist = goodlist.order_by('-price')
    if sort=='3':
        goodlist = goodlist.order_by('price')



    data = {
        'title': '商品',
        'foodtypes':foodtypes,
        'typeid':typeid,
        'goodlist':goodlist,
        'sort':sort,
        'childcid':childcid,
        'flist':flist,

    }
    return render(request,'market.html',data)

#购物车
def shopcar(request):

    uid = request.session.get('uid')
    shops = axf_shopcar.objects.filter(user_id=uid)

    data = {
        'title': '购物车',
        'shops': shops,
    }
    return render(request, 'shopcar.html',data)

#我的
def mine(request):

    data = {
        'title': '我的'
    }
    return render(request, 'mine.html',data)


#md5加密
def md5jm(src):
    md5 = hashlib.md5()
    md5.update(src.encode('utf-8'))
    return md5.hexdigest()

#注册：
def regist(request):
    if request.method=='GET':
        return render(request,'regist.html')

    name = request.POST.get('name')
    psw1 = request.POST.get('psw1')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    email = request.POST.get('email')

    u = user()
    u.name = name
    u.password = md5jm(psw1)
    u.age  = age
    u.sex = sex
    u.email = email
    u.save()
    data={
        'title':'登录',
        'msg':'登录成功'
    }

    return render(request,'main.html',data)


#登录
def login(request):
    if request.method=='GET':

        return render(request,'login.html')
    name = request.POST.get('name')
    psw = request.POST.get('psw')

    m = user.objects.filter(name=name).first()
    if m :
        if m.password ==md5jm(psw):
            auths=set()
            #用用户获取角色 id
            urs = user_role.objects.filter(uid_id=m.id)

            for ur in urs: #查询其角色role.rid_id代表的就是一条角色
                # print(ur.rid_id)
                ras = role_auth.objects.filter(rid_id=ur.rid_id)
                for ra in ras:
                    # print(ra.aid_id)
                    auth1 = auth.objects.filter(pk=ra.aid_id).first().a_path
                    auths.add(auth1)
            print(auths)
            auths = str(auths)
            print(auths)
            request.session['auths'] = auths
            request.session['name'] = name
            request.session['uid'] = m.id

            data = {
                'title': '登录',
                'msg': '登录成功'
            }
            return HttpResponse("<a href='/index/'>点击跳转首页</a>")
    else:
        data={
            'title':'登录',
            'msg':'用户名和密码错误'
        }
        return HttpResponse("<a href='/login/'>点击重新登录</a>")

#验证码

def getcolor():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    return (r,g,b)

def getcolor1():
    r = random.randint(1,150)
    g = random.randint(1,150)
    b = random.randint(1,150)
    return (r,g,b)
def getyzm(request):

    image  = Image.new('RGBA',(100,50),getcolor())
    b = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='static/fonts/ADOBEARABIC-ITALIC.OTF',size=35)

    strs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    code=''
    for i in range(4):
        index = random.randint(1, 63)
        b.text((10+20*i,(random.randrange(0,20))),strs[index],fill= getcolor1(),font=font )
        code +=strs[index]

    request.session['code']=code.lower()


    for i in range(300):
        b.point((random.randrange(100),random.randrange(50)),fill=getcolor())

    import io
    bi= io.BytesIO()
    image.save(bi,'png')

    return HttpResponse(bi.getvalue(),'img/png')


#用户名预校验
def nameyjy(request):
    name= request.GET.get('uname')
    print(name)
    u = user.objects.filter(name=name)
    print(u)
    data={}

    if u: #已存在
        data['res']='0001'
    else:
        data['res'] = '0000'
    print(data)
    return JsonResponse(data)

#验证码预校验
def codejy(request):

    code = request.GET.get('code')

    if  code.lower() ==  request.session.get('code'):
        return JsonResponse({'msg': '0000'})
    else:
        return JsonResponse({'msg': '0001'})


#market+号添加商品
def addshopcar(request):

    goodid = request.GET.get('goodid')

    uid = request.session.get('uid')

    num = request.GET.get('num') if request.GET.get('num') else 1
    data = {}
    m = user.objects.filter(pk=uid).first()

    #获取购物车是否有商品列表
    spc = axf_shopcar.objects.filter(Q(goods_id=goodid) & Q(user_id=uid)).first()

    if m:
        if spc: #如果有，数量加1
            spc.number+=num
            spc.save()
        else: #如果没有，创建spc
            spc = axf_shopcar()
            spc.user_id = uid
            spc.goods_id = goodid
            #数量本应该为1，这里不写是因为modles中进行了dafult=1的设置
            spc.save()
        data['result']='0000'
        data['num'] = spc.number

    else:
        data['result']='0001'

    return JsonResponse(data)

#market-号删减商品
def subshopcar(request):

    goodid = request.GET.get('goodid')
    print(goodid)

    uid = request.session.get('uid')
    print(uid)

    num = request.GET.get('num') if request.GET.get('num') else 1
    data = {}
    m = user.objects.filter(pk=uid).first()

    # 获取购物车是否有商品列表
    spc = axf_shopcar.objects.filter(Q(goods_id = goodid) & Q(user_id=uid)).first()
    print(spc.goods_id)
    if m:
        if spc:
            if spc.number>1:  # 如果有，数量加1
                spc.number -= num
                spc.save()
                data['result'] = '0000'
                data['num'] = spc.number
            else:
                spc.delete()
                data['num'] = '0'
    else:
        data['result']='0001'

    return JsonResponse(data)




def selshopcar(request):


    return None



#shopcar中全选框变化，修改后台数据
def changeall(request):

    li = request.POST.get('li')
    #print(li)
    flag = request.POST.get('flag')
    #print(flag)
    l=li.strip(',').split(',')
    for i in l:
        shop = axf_shopcar.objects.filter(id = i).first()
        shop.isselect = flag=='true' #字符串变布尔值
        shop.save()


    return HttpResponse('0000')

#shopcar中单框变化，修改后台数据
def changeone(request):

    id = request.POST.get('id')
    shop = axf_shopcar.objects.filter(id=id).first()
    shop.isselect = not shop.isselect
    shop.save()

    return HttpResponse('0000')


#购物车结算
@cache_page(200)
def jiesuan(request):

    list0 = request.POST.getlist('fcheck')
    # print(list0)

    #先创建订单，生成订单编号年月日 + 4位流水号
    order = axf_order()
    order.user_id = request.session.get('uid')
    # print(order.user_id)
    order.save()
    money = 0
    for i in list0:
        shopcar = axf_shopcar.objects.filter(id = int(i)).first()
        og = axf_order_goods()
        og.goods_id = shopcar.goods_id
        og.number = shopcar.number
        og.money = shopcar.goods.price*shopcar.number
        money += og.money
        og.order_id = order.id
        og.save()
        shopcar.delete()
    order.money = money
    order.save()
    print(order.money)

    ogs = axf_order_goods.objects.filter(order_id=order.id)

    data={
        'title':'订单',
        'order':order,
        'ogs':ogs,
        'money':money
    }

    return render(request,'order.html',data)