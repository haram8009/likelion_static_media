from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects.all()
    blog_count = len(blogs)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'blog_count': blog_count,'page_obj':page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('imgfile')
    new_blog.save()
    return redirect('detail', new_blog.id)
    # return render(request, 'detail.html', {'blog':new_blog})

# def create(request):
#     form = BlogForm(request.POST)
#
#     if form.is_valid():
#         new_blog = form.save(commit=False)
#         new_blog.save()
#         return redirect('detail', new_blog.id)
#
#     return render(request, 'new.html')

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id) # print() 해보기
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get("title")
    old_blog.content = request.POST.get("content")
    if request.FILES.get('imgfile'):
        old_blog.image = request.FILES.get('imgfile')
    old_blog.save()
    return redirect('detail', old_blog.id)

# def update(request, blog_id):
#     old_blog = get_object_or_404(Blog, pk=blog_id)
#     form = BlogForm(request.POST, instance=old_blog)

    # 클라이언트가 유효한 값을 입력한 경우
    # if form.is_valid():
    #     new_blog = form.save(commit=False)
    #     new_blog.save()
    #     return redirect('detail', old_blog.id)

    # return render(request, 'new.html', {'old_blog':old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')

def search(request):
    search_text = request.GET['search']
    keywords = request.GET['search'].split()
    result_list = []
    for keyword in keywords:
        title_searched_blogs = Blog.objects.filter(title__contains=keyword)
        content_searched_blogs =(Blog.objects.filter(content__contains=keyword))
        searched_blogs = title_searched_blogs.union(content_searched_blogs, all=False)
        if len(searched_blogs):
            for searched_blog in searched_blogs:
                result_list.append(searched_blog)
        else:
            continue

    paginator = Paginator(result_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html', {
        'search_text':search_text, 
        'search_count':len(result_list), 
        'result_list':result_list,
        'page_obj':page_obj})


