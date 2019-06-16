from django.shortcuts import render,render_to_response
from cmdb.models import invitation, log
from django.core.paginator import Paginator # 分页
from django.http import HttpResponseRedirect
# Create your views here.

# 展示、分页
def index(request):
    # 限制每一页显示的条目数量
    limit = 10
    article = invitation.objects
    paginator = Paginator(article,limit)
    # 从url中获取页码参数
    page_num = request.GET.get('page',1)
    loaded = paginator.page(page_num)
    grade = {
        'invitation':loaded
    }
    return render(request,"index.html",grade)

# 回显
def toUpdate(request):
    if request.method == 'GET':
        number = request.GET.get("number",None)
    invi = invitation.objects.filter(number=number)
    grade1 = {
        'invitation':invi
    }
    return render(request,"update.html",grade1)


# 进入添加页面
def toAdd(request):
    return render(request,"add.html")

# 添加
def addInvitation(request):
    if request.method == 'POST':
        number = request.POST.get("number", None)
        name = request.POST.get("name", None)
        # 添加到数据库
        invi = invitation(number = number,name = name)
        invi.save()
    return HttpResponseRedirect('/index/')



# 修改
def updateInvitation(request):
    if request.method == 'POST':
        number = request.POST.get("number", None)
        name = request.POST.get("name", None)
        invi = invitation.objects.filter(number=number).update(name=name)
    return HttpResponseRedirect('/index/')

# 删除
def delete(requeset):
    if requeset.method == 'GET':
        number = requeset.GET.get("number",None)
    invi = invitation.objects.filter(number=number).delete()
    print(invi)
    return HttpResponseRedirect('/index/')

# 查询

def query(request):
    return render_to_response("query.html")

def toquery(request):
    if request.method == 'POST':
        number = request.POST.get("number", None)
        name  = request.POST.get("name",None)

    invi2 = invitation.objects.filter(number=number)

    iniv4 = invitation.objects.filter(name = name)

    invi5 = invi2 or iniv4

    grade1 = {
        'invitation':invi5
        }
    return render(request,"queryshow.html",grade1)


# log 分页回显
def logs(request):
    # 限制每一页显示的条目数量
    limit = 10
    article = log.objects
    paginator = Paginator(article,limit)
    # 从url中获取页码参数
    page_num = request.GET.get('page',1)
    loaded = paginator.page(page_num)
    grade = {
        'log':loaded
    }
    return render(request,"logs.html",grade)

# log 查询

def logquery(request):
    return render_to_response("logquery.html")

def logtoquery(request):
    if request.method == 'POST':
        number = request.POST.get("number", None)
        name  = request.POST.get("name",None)

    invi2 = log.objects.filter(number=number)

    iniv4 = log.objects.filter(name = name)

    invi5 = invi2 or iniv4

    grade1 = {
        'log':invi5
        }
    return render(request,"logqueryshow.html",grade1)



# def queryshow(request):
#     limit = 10
#     article = invitation.objects
#     paginator = Paginator(article, limit)
#     # 从url中获取页码参数
#     page_num = request.GET.get('page', 1)
#     loaded = paginator.page(page_num)
#     grade = {
#         'invitation': loaded
#     }
#     return render(request, "queryshow.html", grade)


# def query(requeset):
#     if request.method == 'POST':
#         number = request.POST.get("number", None)
#         name = request.POST.get("name", None)
#         grade = request.POST.get("grade", None)
#         sex = request.POST.get("sex", None)
#         myquery1 = {"name": "name"}
#         myquery2 = {"name": "name"}
#         myquery3 = {"grade": "grade"}
#         myquery4 = {"sex": "sex"}
#     invi = invitation.objects.find($or())
#     print(invi)
#     return render(request, "query2.html", grade)

# def toquery(request):
#     if request.method == 'GET':
#         number = request.GET.get("number",None)
#         name = request.GET.get("name", None)
#         grade = request.GET.get("grade", None)
#         sex = request.GET.get("sex", None)
#         myquery1 = {name==name}
#         myquery2 = {number==number}
#         myquery3 = {grade==grade}
#         myquery4 = {sex==sex}
#     invi = invitation.objects.filter(myquery1|myquery2|myquery3|myquery4)
#     grade = {
#         'invitation':invi
#     }
#     return render(request,"queryshow.html",grade)