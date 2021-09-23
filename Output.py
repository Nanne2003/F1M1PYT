Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 -10
90
>>> 25 / 5
5.0
>>> 10 /3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is <Nanne>')
Mijn naam is <Nanne>
>>> naam = '<Nanne>'
>>> print(naam)
<Nanne>
>>> print(naam.upper())
<NANNE>
>>> print(naam[0:2])
<N
>>> print(naam[::-1])
>ennaN<
>>> leeftijd= 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo <Nanne> ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	 print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')	             elif leeftijd > 18:
		 
SyntaxError: unexpected indent
>>> if leeftijd < 18:
	hoelang-tot18jaar = 18 - leeftijd
	
SyntaxError: cannot assign to operator
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 1 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
309
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
931
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 931
>>> from datetime import datetime
>>> datum = datetime.now
>>> print(datum)
<built-in method now of type object at 0x10bdc3b98>
>>> datum= datetime.now()
>>> print(datum)
2021-09-23 10:54:50.304591
>>> datum.strftime('%A %d %B %Y')
'Thursday 23 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 23 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Giovedì 23 Settembre 2021'
>>> 