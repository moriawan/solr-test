from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
 
sqs = SearchQuerySet().facet('type').facet('location')
 
urlpatterns = patterns('haystack.views',
    url(r'^search$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
    #url()
)

urlpatterns += url(r'^se/$', 'search.views.index', name="custom_search"),