# Import flask objects to use
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import json
# Import function imageSearch
from bingImageSearch import imageSearch

simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/', defaults={'page':'index'})
@simple_page.route('/<page>')
def show(page):
    imageHtml = json.loads(imageSearch())
    imageThumbnailUrlList = []
    for key,value in imageHtml.iteritems():
        if key == 'value':
            for imageDetails in imageHtml[key]:
                for key2, value2 in imageDetails.iteritems():
                    if key2 == 'thumbnailUrl':
                        imageThumbnailUrlList.append(value2)

    try:
        return render_template('%s.html' % page, imageHtml=json.dumps(imageThumbnailUrlList))
    except:
        abort(404)

