from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

from blogs.models import Blog, Category



# Create your views here.
def posts_by_category(request,category_id):
    # fetch the post that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published',category=category_id)
    #use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #      #redirect the user to the homepage
    #      return redirect('home')
    #use get_object_or_404 when you want to show 404 error page if the category does'nt exist

    category=get_object_or_404(Category,pk=category_id)


    context={'posts':posts,'category':category}
    return render(request,'posts_by_category.html',context)