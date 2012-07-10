from django.shortcuts import *
from blog.models import Posts

def index(request):
    '''
     Index of champagne blog
    '''
    parms = {}
    args = {}
    args['status'] = 'publish'
    args['p_type'] = 'post'
    posts = Posts.objects.filter(**args)
    parms['posts'] = posts
    return render_to_response('index.html', parms, context_instance=RequestContext(request))

def page(request, page='1'):
    '''
     Page of the champagne blog
    '''
    print page
    parms = {}
    args = {}
    args['id'] = int(page)
    args['status'] = 'publish'
    post = get_object_or_404(Posts, **args)
    parms['post'] = post
    return render_to_response('page.html', parms, context_instance=RequestContext(request))
