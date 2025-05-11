from django.shortcuts import render
posts = [
    {
        'title': 'التدوينة الأولي',
        'content': 'هذه هي محتوي التدوينة الأولي',
        'date_posted': '2023-10-01',
        'author': 'أحمد',
    },
        {
        'title': 'التدوينة الثانية',
        'content': 'هذه هي محتوي التدوينة الثانية',
        'date_posted': '2018-09-06',
        'author': 'كريم',
    },
        {
        'title': 'التدوينة الثالثة',
        'content': 'هذه هي محتوي التدوينة الثاثلة',
        'date_posted': '2024-03-28',
        'author': 'علي',
    },
        {
        'title': 'التدوينة الرابعة',
        'content': 'هذه هي محتوي التدوينة الرابعة',
        'date_posted': '2021-12-15',
        'author': 'تامر',
    },
        {
        'title': 'التدوينة الخامسة',
        'content': 'هذه هي محتوي التدوينة الخامسة',
        'date_posted': '2022-09-01',
        'author': 'سيد'}
]
def home(request):
    context = {
        'posts': posts,
        'title': 'الصفحة الرئيسية',
    }
    return render(request, 'blog/index.html', context)


def about_us(request):

    return render(request, 'blog/about.html', {'title': 'من نحن'})
