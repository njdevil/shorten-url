from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from ****.urlform.models import ShortLinks
from ****.urlform.forms import ShortLinksForm
import base64

# Change to your domain here
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
        form = ShortLinksForm(request.POST)
        if form.is_valid:
            long_url = request.POST["long_url"]
            # force "http://" to be saved into the DB for faster retrieval later
            if "http://" not in long_url:
                long_url = "http://" + long_url
            visitor_ip = request.META["REMOTE_ADDR"]
            # one of various methods to ENCRYPT data, "base64", an included library
            short_url = base64.urlsafe_b64encode(long_url)
            # extend the Save operation to include the extra vars
            temp = form.save()
            temp.visitor_ip = visitor_ip
            temp.short_url = short_url
            temp.save()
            template_dict = {"long_url": long_url, "short_url": SITE_URL + short_url}
            return render_to_response('newurl.html', template_dict)
    else:
        form = ShortLinksForm()
        return render_to_response('newurl.html', {'short_links_form': form})


def use_new_url(request, new_url):
    """
    Module to receive the shortened URL link and redirect to the original URL.
    """

    #structure the QuerySet to return just the URL in a list by itself
    url = ShortLinks.objects.filter(short_url = new_url).values_list('long_url', flat = True)[0]
    return HttpResponseRedirect(url)

