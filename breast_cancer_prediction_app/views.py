
from django.shortcuts import render
from django.template  import loader
from joblib import load
import os

model_path = os.path.join(os.path.dirname(__file__), 'breast-cancer-prediction.joblib')
trained_model = load(model_path);

# Create your views here.
def index(request):
	if request.method == 'POST':
		model = []
		model.append(request.POST.get('radius_mean'))
		model.append(request.POST.get('texture_mean'))
		model.append(request.POST.get('perimeter_mean'))
		model.append(request.POST.get('area_mean'))
		model.append(request.POST.get('smoothness_mean'))
		model.append(request.POST.get('compactness_mean'))
		model.append(request.POST.get('concavity_mean'))
		model.append(request.POST.get('concave_points_mean'))
		model.append(request.POST.get('symmetry_mean'))
		model.append(request.POST.get('fractal_dimension_mean'))
		model.append(request.POST.get('radius_se'))
		model.append(request.POST.get('texture_se'))
		model.append(request.POST.get('perimeter_se'))
		model.append(request.POST.get('area_se'))
		model.append(request.POST.get('smoothness_se'))
		model.append(request.POST.get('compactness_se'))
		model.append(request.POST.get('concavity_se'))
		model.append(request.POST.get('concave_points_se'))
		model.append(request.POST.get('Symmetry_se'))
		model.append(request.POST.get('Fractal_dimesion_se'))
		model.append(request.POST.get('Radius_worst'))
		model.append(request.POST.get('Texture_worst'))
		model.append(request.POST.get('Perimeter_worst'))
		model.append(request.POST.get('Area_worst'))
		model.append(request.POST.get('Smoothness_worst'))
		model.append(request.POST.get('Compactness_worst'))
		model.append(request.POST.get('Concavity_worst'))
		model.append(request.POST.get('Concave_points_worst'))
		model.append(request.POST.get('Symmetry_worst'))
		model.append(request.POST.get('Fractal_dimension_worst'))

		prediction = trained_model.predict([model])

		if prediction == '[0]':
			return render(request, 'breast_cancer_prediction_app/index.html', {'prediction': 'B' })
		else:
			return render(request, 'breast_cancer_prediction_app/index.html', {'prediction': 'M' })
	else:
		return render(request, 'breast_cancer_prediction_app/index.html')


