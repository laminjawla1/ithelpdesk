from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class Blog_Home(ListView):
    login_required = True

    model = Post
    template_name = 'blog_home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Blog_Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetail(DetailView):
    login_required = True

    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)

        liked = False
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["liked"] = liked
        return context


class AddPost(CreateView):
    login_required = True

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCategory(CreateView):
    login_required = True

    model = Category
    # form_class = CategoryForm
    template_name = 'add_blog_category.html'
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class EditPost(UpdateView):
    login_required = True
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePost(DeleteView):
    login_required = True
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


@login_required
def BlogCategory(request, cat):
    blog_category = Post.objects.filter(category=cat.replace('-', ' '))

    return render(
        request, 'blog_categories.html', {'cat': cat.replace('-', ' '), 
        'blog_category': blog_category, 'cat_menu': Category.objects.all()})



