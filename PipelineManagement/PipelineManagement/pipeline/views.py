from django.shortcuts import render, redirect
from .models import MyPipelines


# Create your views here.
def submit_pipeline(request):
    if request.method == 'POST':
        prospect_name = request.POST['prospectName']
        intermediary_name = request.POST['intermediaryName']
        premium_amount = request.POST['premiumAmount']
        business_class = request.POST['businessClass']
        transaction_date = request.POST['transactionDate']
        current_insurer = request.POST['currentInsurer']
        likely_hood = request.POST['likelyHood']
        status = request.POST['status']
        remarks = request.POST['remarks']
        MyPipelines.objects.create(prospectName=prospect_name, intermediaryName=intermediary_name,
                                   premiumAmount=premium_amount, businessClass=business_class,
                                   transactionDate=transaction_date, currentInsurer=current_insurer,
                                   likelyHood=likely_hood, status=status, remarks=remarks

                                   )
        return redirect('success')
    return render(request, 'pipeline.html')
