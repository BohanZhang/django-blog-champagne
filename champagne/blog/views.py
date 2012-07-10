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
    # TODO: Change here to the filter and order by desc
    posts = Posts.objects.all()
    parms['posts'] = posts
    print posts
    return render_to_response('index.html', parms, context_instance=RequestContext(request))

def page(request, page='1'):
    '''
     Page of the champagne blog
    '''
    parms = {}
    args = {}
    args['pk'] = int(page)
    args['status'] = 'publish'
    post = get_object_or_404(Posts, args)
    parms['post'] = post
    return render_to_response('page.html', parms, context_instance=RequestContext(request))
