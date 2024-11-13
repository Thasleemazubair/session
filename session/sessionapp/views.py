from django.shortcuts import render

def set_session(request):
    request.session['user_name']='alice'
    return render(request,'set_session.html')

def get_session(request):
    user_name = request.session.get('user_name','Guest')
    return render(request,'get_session.html',{'user_name':user_name})

def delete_session(request):
    if 'user_name' in request.session:
        del request.session['user_name']
    return render(request,'delete_session.html')

def clear_session(request):
    request.session(request)
    return render(request,'clear_session.html')
