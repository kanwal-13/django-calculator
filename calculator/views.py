from django.http import HttpResponseRedirect
from django.shortcuts import render
from calculator.forms import FormName

# Create your views here.
def index(request):
    if request.method =='POST':
        form = FormName(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n1 = form.cleaned_data['num1']
            n2 = form.cleaned_data['num2']
            if 'add' in request.POST:
                res = n1+n2
            if 'sub' in request.POST:
                res = n1 - n2
            if 'mul' in request.POST:
                res = n1 * n2
            if 'div' in request.POST:
                if n2==0:
                    res = "zero divide error"  
                else:
                    res = n1 / n2
            args = {'form': form , 'result': res}
            return render(request, 'input.html', args)
            

    else:
        form = FormName()
        return render(request, 'input.html', {'form': form})


     

