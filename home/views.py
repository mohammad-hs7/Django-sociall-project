from django.shortcuts import render , redirect
from django.views import View
from . models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PostUpdateForm, PostCreatedForm
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
# Create your views here.


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})

    def post(self, request):
        pass



class PostDetailView(View):

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comments = post.post_comments.filter(is_reply=False)
        return render(request, 'home/detail.html', {'posts': post, 'comments': comments})

class PostDeleteView(LoginRequiredMixin, View):

    def get(self,request, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user_id == request.user.id:
            post.delete()
            messages.success(request,'your post is deleted succesfully', 'danger')
        else:
            messages.error(request, 'you can,t')
        return redirect('home:home_page')

class PostUpdateView(LoginRequiredMixin,View):
    form_class = PostUpdateForm

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form': form})

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][20])
            new_post.save()
            messages.success(request, 'post as update successfully... ', 'success')
            return redirect('home:post_detail', post_id)


class PostCreatedView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostCreatedForm()
        return render(request, 'home/create.html', {'form': form})

    def post(self, request):
        form = PostCreatedForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print('fffff')
            Post.objects.create(user=request.user, title=cd['title'],slug=cd['title'].replace(' ', '-'), body=cd['body'])
            messages.success(request, 'your post sending is successfully...')
            return redirect('home:home_page')
        return render(request, 'home/create.html', {'form': form})


