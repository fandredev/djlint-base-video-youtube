from django.shortcuts import render


from .models import Car


def render_template_car(request):
    cars = Car.objects.all()

    return render(
        request,
        "car-detail.html",
        {
            "cars": cars,
        },
    )
