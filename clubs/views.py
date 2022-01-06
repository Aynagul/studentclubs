from django.shortcuts import render

from .models import StudentClubsTitle, Announcement, About, Club


def home(request):
    all_description = StudentClubsTitle.objects.all()
    all_announcements = Announcement.objects.all()
    return render(request, 'clubs/index.html',
                  {'all_announcements': all_announcements, 'all_description': all_description})


def home_tr(request):
    return render(request, 'clubs/index_tr.html')


def about(request):
    all_about = About.objects.all()
    return render(request, 'clubs/about.html', {'all_about': all_about})


def about_tr(request):
    return render(request, 'clubs/about_tr.html')


def student_clubs(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/student_clubs.html', {'clubs': clubs})


def student_clubs_tr(request):
    return render(request, 'clubs/student_clubs_tr.html')


def news(request):
    all_description = StudentClubsTitle.objects.all()
    all_announcements = Announcement.objects.all()
    return render(request, 'clubs/news.html',{'all_announcements': all_announcements, 'all_description': all_description})


def news_tr(request):
    return render(request, 'clubs/news_tr.html')


def club_view(request, pk):
    club = Club.objects.get(pk=pk)
    return render(request, 'clubs/clubs_item.html', {'club': club})

