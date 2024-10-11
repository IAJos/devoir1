from django.shortcuts import render
from hello.form import SchoolForm
from hello.models import School
from django.shortcuts import redirect


def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            school = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('school-list')
    else:
        form = SchoolForm()

    return render(request, 'school_create.html', {'form': form})


def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})
# Create your views here.
