from django.shortcuts import render

# views.py (Python)
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import URL
from .utils import generate_short_url
from django.db import transaction


def home(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        now = timezone.now()
        threshold = now - timedelta(minutes=1)

        existing_url = URL.objects.filter(
            long_url=long_url,
            created_at__gte=threshold
        ).order_by('-created_at').first()

        if existing_url:
            existing_url.attempts += 1
            existing_url.save()
            url = existing_url
        else:
            url = URL(long_url=long_url, short_url=generate_short_url())
            url.save()

        return render(request, "home.html", {
            "short_url": request.build_absolute_uri(url.short_url)
        })

    return render(request, "home.html")



def redirect_to_long_url(request, short_url):
    url = URL.objects.filter(short_url=short_url).first()
    if url is None:
        return HttpResponse("This URL was not found.", status=410)

    expiration_time = url.created_at + timedelta(minutes=1)

    if timezone.now() > expiration_time:
        print(f"Is being deleted URL: {url.short_url}")

        with transaction.atomic():
            url.delete()

        return HttpResponse("Shorten URL has expired.", status=410)

    return redirect(url.long_url)

