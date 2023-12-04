
(myvenv) C:\Users\black\djangogirls>python manage.py shell
Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
Post.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Post' is not defined
from blog.models import Post
Post.objects.all()
<QuerySet [<Post: My name.>, <Post: Wife>, <Post: dogs>, <Post: people>, <Post: nothing>]>
Post.objects.create(author=me, title='Sample title', text='Test')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'me' is not defined
from django.contrib.auth.models import User
User.objects.all()
<QuerySet [<User: joe>]>
me = User.objects.get(username='joe')
Post.objects.create(author=me, title='Sample title', text='Test')
<Post: Sample title>
Post.objects.all()
<QuerySet [<Post: My name.>, <Post: Wife>, <Post: dogs>, <Post: people>, <Post: nothing>, <Post: Sample title>]>
Post.objects.filter(author=me)
<QuerySet [<Post: My name.>, <Post: Wife>, <Post: dogs>, <Post: people>, <Post: nothing>, <Post: Sample title>]>
Post.objects.filter(title__contains='title')
<QuerySet [<Post: Sample title>]>
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: nothing>]>
post = Post.objects.get(title="Sample title")
post.publish()
Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: nothing>, <Post: Sample title>]>
Post.objects.order_by('created_date')
<QuerySet [<Post: My name.>, <Post: Wife>, <Post: dogs>, <Post: people>, <Post: nothing>, <Post: Sample title>]>
Post.objects.order_by('-created_date')
<QuerySet [<Post: Sample title>, <Post: nothing>, <Post: people>, <Post: dogs>, <Post: Wife>, <Post: My name.>]>
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: nothing>, <Post: Sample title>]>
exit()

(myvenv) C:\Users\black\djangogirls>
