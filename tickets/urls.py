from django.urls import path
from blog.views import Blog_Home, ArticleDetail, AddPost, EditPost, DeletePost, AddCategory, BlogCategory, like_post
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    path('blog_home/', login_required(Blog_Home.as_view()), name='blog_home'),
    path('article/<int:pk>', login_required(ArticleDetail.as_view()), name='article_detail'),
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('article/edit/<int:pk>', login_required(EditPost.as_view()), name='edit_post'),
    path('article/<int:pk>/delete', login_required(DeletePost.as_view()), name='delete_post'),
    path('add_blog_category/', login_required(AddCategory.as_view()), name='add_blog_category'),
    path('category/<str:cat>/', BlogCategory, name='category'),
    path('like/<int:pk>/', like_post, name='like_post'),
    # -----------------------------------------------------------------------
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('bookticket/', views.bookticket, name='bookticket'),
    path('feedback/', views.feedback, name='feedback'),
    path('search/', views.search, name='search'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('search_result/', views.search_result, name='search_result'),
]
