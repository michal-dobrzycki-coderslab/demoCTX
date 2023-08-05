from django.utils import timezone


def my_cp(request):
    ctx = {
        'result': 10 + 12 * 2,
        'now': timezone.now(),
        'lista': [110, 2, 2, 3, 4, 5],
        'title': 'władca pierścieni 3 tralalla'
    }
    return ctx