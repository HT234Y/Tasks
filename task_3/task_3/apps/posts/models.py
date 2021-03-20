from django.db import models


class Post(models.Model):
	post_title = models.CharField('Заголовок поста', max_length = 200)
	post_text = models.TextField('Описание')
	post_img = models.ImageField(upload_to = 'prod_img')

	def __str__(self):
		return self.post_title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	author_name = models.CharField('Имя', max_length = 50)
	comment_text = models.TextField('Текст', max_length = 200)


	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
