from django.shortcuts import render
from .classifier import predict_insurance

def classify_view(request):
    result = None
    if request.method == "POST":
        age = int(request.POST["age"])
        salary = int(request.POST["salary"])
        result = predict_insurance(age, salary)
    
    return render(request, "classify.html", {"result": result})
