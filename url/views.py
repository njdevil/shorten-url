from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from ****.url.models import ShortLinks

#Change to your domain here
SITE_URL=""


@csrf_exempt
def convert_url(request):
    """
    Module to receive a URL POST from the rendered template.
    Module automatically adds http:// if it wasnt included on the submission.
    URL is saved into the DB and the Primary Key (PK) is used as this shortened URL
    as in,  www.*****.com/2, or www.*****.com/1224
    """

    if request.POST:
        long_url = request.POST["long_url"]
        if "http://" not in long_url:
            long_url = "http://" + long_url
        visitor_ip = request.META["REMOTE_ADDR"]
        url = ShortLinks(visitor_ip = visitor_ip, long_url = long_url)
        url.save()
        template_dict = {"long_url": long_url, "short_url": SITE_URL + str(url.pk)}

        return render_to_response('newurl.html', template_dict)
    return render_to_response('newurl.html')


def use_new_url(request, new_url):
    """
    Module to receive the shortened URL link and redirect to the original URL.
    """

    #structure the QuerySet to return just the URL in a list by itself
    url = ShortLinks.objects.filter(pk = new_url).values_list('long_url', flat = True)[0]
    return HttpResponseRedirect(url)
