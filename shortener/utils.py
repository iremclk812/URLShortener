import random
import string
from .models import URL


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits

    while True:
        short_url = ''.join(random.choice(chars) for _ in range(length))

        # Veritabanında bu kısa URL var mı kontrol edelim (benzersiz olması gerekir)
        if not URL.objects.filter(short_url=short_url).exists():
            return short_url