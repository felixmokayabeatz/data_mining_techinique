from django.shortcuts import render
from .classifier import predict_insurance

def classify_view(request):
    
    context = {
        "result": None,
        "prediction": None,
        "age": "",
        "salary": "",
        "error": None
    }
    
    if request.method == "POST":
        try:
            
            age_str = request.POST.get("age", "")
            salary_str = request.POST.get("salary", "")
            
            
            if not age_str or not salary_str:
                context["error"] = "Please provide both age and salary."
            else:
                try:
                    age = int(age_str)
                    salary = int(salary_str)
                    
                    
                    context["age"] = age_str
                    context["salary"] = salary_str
                    
                    
                    if age < 18 or age > 100:
                        context["error"] = "Age must be between 18 and 100."
                    elif salary < 10000:
                        context["error"] = "Salary must be at least 10,000."
                    else:
                        
                        prediction = predict_insurance(age, salary)
                        context["prediction"] = prediction
                        context["result"] = "You will buy insurance!" if prediction == 1 else "You won't buy insurance."
                        
                except ValueError:
                    context["error"] = "Age and salary must be valid numbers."
        
        except Exception as e:
            context["error"] = f"An error occurred: {str(e)}"
    
    return render(request, "classify.html", context)