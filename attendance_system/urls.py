"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='register'),
    path('save/',views.save),
    path('',views.login),
    path('login/',views.login,name='login'),
    path('mainpage/',views.mainpage),
    path('IT/',views.IT,name='it'),
    path('Comp/',views.Comp,name='comp'),
    path('Mech/',views.Mech,name='mech'),
    path('Elect/',views.Elect,name='elect'),
    path('Eandtc/',views.Eandtc,name='eandtc'),
    path('Civil/',views.Civil,name='civil'),

# first year
    path('ITfirstyear/',views.ITfirstyear,name='itfirstyear'),
    path('Compfirstyear/',views.Compfirstyear,name='compfirstyear'),
    path('Mechfirstyear/',views.Mechfirstyear,name='mechfirstyear'),
    path('Electfirstyear/',views.Electfirstyear,name='electfirstyear'),
    path('Eandtcfirstyear/',views.Eandtcfirstyear,name='eandtcfirstyear'),
    path('Civilfirstyear/',views.Civilfirstyear,name='civilfirstyear'),

    # path('login/',views.login)
# second year
    path('ITsecondyear/',views.ITsecondyear,name='itsecondyear'),
    path('Compsecondyear/',views.Compsecondyear,name='compsecondyear'),
    path('Mechsecondyear/',views.Mechsecondyear,name='mechsecondyear'),
    path('Electsecondyear/',views.Electsecondyear,name='electsecondyear'),
    path('Eandtcsecondyear/',views.Eandtcsecondyear,name='eandtcsecondyear'),
    path('Civilsecondear/',views.Civilsecondyear,name='civilsecondyear'),

# third year
    path('ITthirdyear/',views.ITthirdyear,name='itthirdyear'),
    path('Compthirdyear/',views.Compthirdyear,name='compthirdyear'),
    path('Mechthirdyear/',views.Mechthirdyear,name='mechthirdyear'),
    path('Electthirdyear/',views.Electthirdyear,name='electthirdyear'),
    path('Eandtcthirdyear/',views.Eandtcthirdyear,name='eandtcthirdyear'),
    path('Civilthirdear/',views.Civilthirdyear,name='civilthirdyear'),


# fourth year
    path('ITfourthyear/',views.ITfourthyear,name='itfourthyear'),
    path('Compfourthyear/',views.Compfourthyear,name='compfourthyear'),
    path('Mechfourthyear/',views.Mechfourthyear,name='mechfourthyear'),
    path('Electfourthyear/',views.Electfourthyear,name='electfourthyear'),
    path('Eandtcfourthyear/',views.Eandtcfourthyear,name='eandtcfourthyear'),
    path('Civilfourthear/',views.Civilfourthyear,name='civilfourthyear'),

    path('ITfiveyear/',views.ITfiveyear,name='itfiveyear'),
#Enrollment
    path('itfirstyearenroll/',views.ITfirstyearEnroll,name='itfirstyearenroll'),
    path('compfirstyearenroll/',views.CompfirstyearEnroll,name='compfirstyearenroll'),
    path('mechfirstyearenroll/',views.MechfirstyearEnroll,name='mechfirstyearenroll'),
    path('electfirstyearenroll/',views.ElectfirstyearEnroll,name='electfirstyearenroll'),
    path('eandtcfirstyearenroll/',views.EandtcfirstyearEnroll,name='eandtcfirstyearenroll'),
    path('civilfirstyearenroll/',views.CivilfirstyearEnroll,name='civilfirstyearenroll'),

    path('itsecondyearenroll/',views.ITsecondyearEnroll,name='itsecondyearenroll'),
    path('compsecondyearenroll/',views.CompsecondyearEnroll,name='compsecondyearenroll'),
    path('mechsecondyearenroll/',views.MechsecondyearEnroll,name='mechsecondyearenroll'),
    path('electsecondyearenroll/',views.ElectsecondyearEnroll,name='electsecondyearenroll'),
    path('eandtcsecondyearenroll/',views.EandtcsecondyearEnroll,name='eandtcsecondyearenroll'),
    path('civilsecondyearenroll/',views.CivilsecondyearEnroll,name='civilsecondyearenroll'),

    path('itthirdyearenroll/',views.ITthirdyearEnroll,name='itthirdyearenroll'),
    path('compthirdyearenroll/',views.CompthirdyearEnroll,name='compthirdyearenroll'),
    path('mechthirdyearenroll/',views.MechthirdyearEnroll,name='mechthirdyearenroll'),
    path('electthirdyearenroll/',views.ElectthirdyearEnroll,name='electthirdyearenroll'),
    path('eandtcthirdyearenroll/',views.EandtcthirdyearEnroll,name='eandtcthirdyearenroll'),
    path('civilthirdyearenroll/',views.CivilthirdyearEnroll,name='civilthirdyearenroll'),

    path('itfourthyearenroll/',views.ITfourthyearEnroll,name='itfourthyearenroll'),
    path('compfourthyearenroll/',views.CompfourthyearEnroll,name='compfourthyearenroll'),
    path('mechfourthyearenroll/',views.MechfourthyearEnroll,name='mechfourthyearenroll'),
    path('electfourthyearenroll/',views.ElectfourthyearEnroll,name='electfourthyearenroll'),
    path('eandtcfourthyearenroll/',views.EandtcfourthyearEnroll,name='eandtcfourthyearenroll'),
    path('civilfourthyearenroll/',views.CivilfourthyearEnroll,name='civilfourthyearenroll'),

    path('itfiveyearenroll/',views.ITfiveyearEnroll,name='itfiveyearenroll'),

    path('itfyenroll/',views.itfyenroll,name='itfyenroll'),
    path('compfyenroll/',views.compfyenroll,name='compfyenroll'),
    path('mechfyenroll/',views.mechfyenroll,name='mechfyenroll'),
    path('electfyenroll/',views.electfyenroll,name='electfyenroll'),
    path('eandtcfyenroll/',views.eandtcfyenroll,name='eandtcfyenroll'),
    path('civilfyenroll/',views.civilfyenroll,name='civilfyenroll'),

    path('itsyenroll/',views.itsyenroll,name='itsyenroll'),
    path('compsyenroll/',views.compsyenroll,name='compsyenroll'),
    path('mechsyenroll/',views.mechsyenroll,name='mechsyenroll'),
    path('electsyenroll/',views.electsyenroll,name='electsyenroll'),
    path('eandtcsyenroll/',views.eandtcsyenroll,name='eandtcsyenroll'),
    path('civilsyenroll/',views.civilsyenroll,name='civilsyenroll'),

    path('ittyenroll/',views.ittyenroll,name='ittyenroll'),
    path('comptyenroll/',views.comptyenroll,name='comptyenroll'),
    path('mechtyenroll/',views.mechtyenroll,name='mechtyenroll'),
    path('electtyenroll/',views.electtyenroll,name='electtyenroll'),
    path('eandtctyenroll/',views.eandtctyenroll,name='eandtctyenroll'),
    path('civiltyenroll/',views.civiltyenroll,name='civiltyenroll'),

    path('itlyenroll/',views.itlyenroll,name='itlyenroll'),
    path('complyenroll/',views.complyenroll,name='complyenroll'),
    path('mechlyenroll/',views.mechlyenroll,name='mechlyenroll'),
    path('electlyenroll/',views.electlyenroll,name='electlyenroll'),
    path('eandtclyenroll/',views.eandtclyenroll,name='eandtclyenroll'),
    path('civillyenroll/',views.civillyenroll,name='civillyenroll'),

    path('itfiveyenroll/',views.itfiveyenroll,name='itfiveyenroll'),
    # tracking***********

    path('itfytrack/',views.itfytrack,name='itfytrack'),
    path('compfytrack/',views.compfytrack,name='compfytrack'),
    path('mechfytrack/',views.mechfytrack,name='mechfytrack'),
    path('electfytrack/',views.electfytrack,name='electfytrack'),
    path('eandtcfytrack/',views.eandtcfytrack,name='eandtcfytrack'),
    path('civilfytrack/',views.civilfytrack,name='civilfytrack'),

    path('itsytrack/',views.itsytrack,name='itsytrack'),
    path('compsytrack/',views.compsytrack,name='compsytrack'),
    path('mechsytrack/',views.mechsytrack,name='mechsytrack'),
    path('electsytrack/',views.electsytrack,name='electsytrack'),
    path('eandtcsytrack/',views.eandtcsytrack,name='eandtcsytrack'),
    path('civilsytrack/',views.civilsytrack,name='civilsytrack'),

    path('ittytrack/',views.ittytrack,name='ittytrack'),
    path('comptytrack/',views.comptytrack,name='comptytrack'),
    path('mechtytrack/',views.mechtytrack,name='mechtytrack'),
    path('electtytrack/',views.electtytrack,name='electtytrack'),
    path('eandtctytrack/',views.eandtctytrack,name='eandtctytrack'),
    path('civiltytrack/',views.civiltytrack,name='civiltytrack'),

    path('itlytrack/',views.itlytrack,name='itlytrack'),
    path('complytrack/',views.complytrack,name='complytrack'),
    path('mechlytrack/',views.mechlytrack,name='mechlytrack'),
    path('electlytrack/',views.electlytrack,name='electlytrack'),
    path('eandtclytrack/',views.eandtclytrack,name='eandtclytrack'),
    path('civillytrack/',views.civillytrack,name='civillytrack'),

    path('itfiveyeartrack/',views.itfiveyeartrack,name='itfiveyeartrack'),









]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
