from flask import render_template,request, redirect, url_for, flash
from . import main
from app.models import User,Blog,Comment,Subscriber
from ..requests import get_quotes
from flask_login import login_required, current_user
from .forms import CreateBlog
from ..email import mail_message

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    quotes = get_quotes()
    post=Blog.query.all()
    
    return render_template('index.html', quotes=quotes, post=post)


@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object()
        blog = Blog(title=title,content=content,user=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("New Blog Post","email/subscriber",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        flash('You Posted a new Blog', )
    return render_template('newblog.html', form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog.query.get(id)
    return render_template('blogs.html',blog=blog,comments=comments)
    

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Nicky's Blogging site","email/subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
