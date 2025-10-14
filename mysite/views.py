"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string


# HTML_STRING = """
# <h1>Hello World</h1>
# """


def home_view(request):
    """
    Take in a request (Django sends a request)
    Return HTML as a response
    """

    article_obj = Article.objects.get(id=1)
    # article_title = article_obj.title
    # article_content = article_obj.content

    context = {
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content

    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = f"""
    # <h1>{article_obj.title} ({article_obj.id})</h1>
    # <p>{article_obj.content}</p>
    # """



    return HttpResponse(HTML_STRING)