from django.shortcuts import render,HttpResponse
from  PyDictionary import PyDictionary

# Create your views here.
dictionary = PyDictionary()

def home(request):
    return render(request,'home.html')

def search(request):
    word = request.POST['search']
    meaning = dictionary.meaning(word)
    syn = dictionary.synonym(word)
    opp = dictionary.antonym(word)

    try:
        result = meaning['Noun'][:2]
    except:
        try:
            result = meaning['Verb'][:2]
        except:
            return HttpResponse("<script>alert('NO meanings found!!')</script>")


    print(result)
    if meaning == None:
        return HttpResponse("<script>alert('NO meanings found!!')</script>")
    else:

        params = {
            'word' : word,
            'meaning' : result,
            'syn': syn[:4],
            'ant' : opp[:4]
        }

        return render(request,'search.html',params)