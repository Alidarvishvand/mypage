from django.shortcuts import render
from  django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january":"January hello",
    "February":"February hello",
    "march":"March hello",
    "April":"April hello",
    "May":"May hello",
    "June":"June hello",
    "July":"July hello",
    "August":"August hello",
    "September":"September hello",
    "October":"October hello",
    "November":"November hello",
    "December":"December hello"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)




def monthly_challenge_by_number(request, month): 
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] 
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("this month is not supported")
    