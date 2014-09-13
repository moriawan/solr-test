# Create your views here.
from django.http import HttpResponse
from haystack.query import SearchQuerySet

# all_results = SearchQuerySet().all()
# hello_results = SearchQuerySet().filter(content='hello')
# hello_world_results = SearchQuerySet().filter(content='hello world')
# unfriendly_results = SearchQuerySet().exclude(content='hello').filter(content='world')
# recent_results = SearchQuerySet().order_by('-pub_date')[:5]

# Using the new input types...
#from haystack.inputs import AutoQuery, Exact, Clean
#sqs = SearchQuerySet().filter(content=AutoQuery(request.GET['q']), product_type=Exact('ancient book'))


def index(request):


	# if request.GET['product_url']:
	#     sqs = sqs.filter(product_url=Clean(request.GET['product_url']))

	if request.GET['search_text']:
		search_text = request.GET['search_text']

	sqs = SearchQuerySet().filter(text=search_text, textNgrams=search_text)


    return HttpResponse("Hello, world. You're at the polls index.")