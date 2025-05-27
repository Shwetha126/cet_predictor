from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    if request.user.is_authenticated:
        return redirect('predict')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('predict')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def predict(request):
    if request.method == 'POST':
        cet_marks = int(request.POST.get('cet_marks'))
        puc_marks = int(request.POST.get('puc_marks'))

        # Dummy prediction logic (replace with ML model later)
        predicted_rank = max(1, 10000 - (cet_marks * 10) - (puc_marks * 5))
        probability = min(1, (cet_marks + puc_marks) / 200)  # Example probability 0 to 1

        # Example college list (replace with database later)
        colleges = [
            {"name": "RV College of Engineering", "rank_cutoff": 1000},
            {"name": "BMS College of Engineering", "rank_cutoff": 2000},
            {"name": "MS Ramaiah Institute of Technology", "rank_cutoff": 4000},
            {"name": "Dayananda Sagar College", "rank_cutoff": 6000},
            {"name": "Nitte Meenakshi Institute", "rank_cutoff": 8000},
            {"name": "New Horizon College", "rank_cutoff": 10000},
        ]

        # Filter colleges where predicted rank is <= cutoff rank
        matching_colleges = [c for c in colleges if predicted_rank <= c["rank_cutoff"]]

        context = {
            'predicted_rank': predicted_rank,
            'probability': round(probability * 100, 2),  # Show % format
            'matching_colleges': matching_colleges,
        }
        return render(request, 'predictor/result.html', context)

    return render(request, 'predictor/predict.html')
