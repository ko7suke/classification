from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from .forms import PredictForm
from .models import Predict


def form(request):
    context = {'form': PredictForm()}
    template = loader.get_template("classify/form.html")
    return HttpResponse(template.render(context, request))


def predict(request):
    if not request.method == 'POST':
        return redirect('classify:form')

    prediction_form = PredictForm(request.POST, request.FILES)
    if not prediction_form.is_valid():
        raise ValueError('Formが不正です')

    image = Predict(
        image=prediction_form.cleaned_data['image'],
    )

    label, percentage = image.predict()
    template = loader.get_template('classify/result.html')

    context = {
        'image_name': image.image.name,
        'image_src': image.image_src(),
        'label': label,
        'percentage': percentage,
    }

    return HttpResponse(template.render(context, request))
