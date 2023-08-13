from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TaxiDriverForm
# from .models import UserProfile, Station, TaxiCallNotification
from .models import UserProfile, Station
from django.views import View

# Create your views here.
def start_login(request):
    return render(request, 'profiles/mainlogin.html')

def custom_logout(request):
    logout(request)
    return redirect('map:map_main')

@login_required
def my_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    stations = Station.objects.all()

    if request.method == 'POST':
        form = TaxiDriverForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('map:map_main')  # 폼 저장 후 프로필 페이지로 리디렉션
    else:
        form = TaxiDriverForm(instance=user_profile)
        
    phone_number = user_profile.phone_number
        
    context = {
        'user': request.user,
        'user_profile': user_profile,
        'form': form,
        'phone_number': phone_number,
        'stations': stations,
    }
    return render(request, 'profiles/mypage.html', context)

@login_required
def call_list(request):
    return render(request, 'profiles/call_list.html')
# class TaxiCallListView(View):
#     template_name = 'profiles/notifications_list.html'  # 템플릿 파일의 경로
#
#     def get(self, request, *args, **kwargs):
#         notifications = TaxiCallNotification.objects.all()
#         context = {'notifications': notifications}
#         return render(request, self.template_name, context)
