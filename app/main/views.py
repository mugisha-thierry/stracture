from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_news_source,get_news_article
# from .forms import ReviewForm
# from ..models import Article,News

# Views
@main.route('/')
def index():
    return render_template('index.html')