from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

zodiac_dict = {
    'aries': "Aries Cardinal fire; ruled by Mars. Willpower, impulsive, initiative, courage, energy, activity. Often rushes headlong into things.",
    'taurus': "Taurus Fixed earth; ruled by Venus. Sensual, pleasure-seeker, steadfast, strives for security. Sees red when provoked for a long time",
    'gemini': "Gemini Mutable air; ruled by Mercury. Mental type, witty, communicative, mobile, takes pleasure in learning. Rarely touches down.",
    'cancer': "Cancer Cardinal water; ruled by the Moon. Emotional type, stubborn, seeks safety and closeness. Very much a family person.",
    'leo': "Leo Fixed fire; ruled by the Sun. Glamour, generosity, organizer, the center of attention. Likes to take the lion's part.",
    'virgo': "Virgo Mutable earth; ruled by Mercury. Precise, differentiates, does what is necessary, utilitarian. A critical point of view.",
    'libra': "Libra Cardinal air; ruled by Venus. A sense of beauty and proportion, tactful, seeks balance and harmony. Sometimes hovers between the scales.",
    'scorpio': "Scorpio Fixed water; ruled by Pluto. Corrosive, passionate, piercing, extreme situations. Frequently quarrels with the spirits he called.",
    'sagittarius': "Sagittarius Mutable fire; ruled by Jupiter. Free spirit, carefree, love of movement, cheerful. Wanderlust, often seems to be elsewhere.",
    'capricorn': "Capricorn Cardinal earth; ruled by Saturn. Enduring, has a sense of purpose, proud, ambitious. Can get stuck in craggy heights.",
    'aquarius': "Aquarius Fixed air; ruled by Uranus. Communicative, humanitarian, progressive, fraternal. Universal spirit with occasional astonishing obstinacy.",
    'pisces': "Pisces Mutable water; ruled by Neptune. Sensitive, compassionate, helpful, sociable. Very adaptable, hard to get a hold on."}


element_dict = {'fire': ['aries', 'leo', 'sagittarius'],
                'earth': ['taurus', 'virgo', 'capricorn'],
                'air': ['gemini', 'libra', 'aquarius'],
                'water': ['cancer', 'scorpio', 'pisces']
                }


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'You have entered a four-digit number - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'You have entered a float number - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'You have entered a date - {sign_zodiac}')


def index_elements(request):
    zodiac_elements = list(element_dict)
    context = {'zodiac_elements': zodiac_elements}
    return render(request, 'horoscope/index_elements.html', context=context)


def get_info_about_element(request, element: str):
    description = element_dict.get(element)
    data = {'description_element': description,
            'element': element}
    return render(request, 'horoscope/info_elements.html', context=data)


def index(request):
    zodiacs = list(zodiac_dict)
    context = {'zodiacs': zodiacs}
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {'description': description,
            'sign': sign_zodiac,
            'zodiacs': zodiac_dict}
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Unknown zodiac sign's sequence number - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)

