# from django.http import HttpRes ponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Post, Comment

from django.urls import reverse


def index(request):
	list_posts = Post.objects.all()
	return render(
		request, 
		'posts/list_posts.html', 
		{'list_posts': list_posts},
		)


def detail(request, post_id):
	try:
		p = Post.objects.get(id = post_id)

	except:
		raise Http404('Пост не найден!')

	latest_comments = p.comment_set.order_by('-id')[:10]

	return render(request, 'posts/detail.html', {'post': p, 'latest_comments': latest_comments})

def leave_comment(request, post_id):
	try:
		p = Post.objects.get(id = post_id)

	except:
		raise Http404('Пост не найден!')

	p.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect(reverse('posts:detail', args = (p.id,)))