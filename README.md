# Datu lasīšana no vietnes, apgriešana un saglabāšana.

## Projekta apraksts
Man patīk sports un īpaši futbols, es visu laiku sekoju līdzi spēļu rezultātiem. Mana mīļākā komanda ir "Barcelona", tāpēc es nolēmu uzrakstīt kodu, kas nolasīs La Liga turnīra tabulas, kur spēlē "Barcelona". Kods nolasa katras komandas (20 komandas) pozīciju, nosaukumu un punktus, pēc tam tas saglabā nolasītos datus divās kopijās csv un xlsx failos. Tas ļauj man ātri apskatīt interesējošos datus, neieejot tīmekļa vietnē. Saglabātos failus var arī neatvērt, bet manuāli ievadīt komandas nosaukumu, un tas sniegs jums attiecīgās komandas pozīciju, nosaukumu un punktu skaitu.

## Kādas Python bibliotēkas un kāpēc tiek izmantotas projekta izstrādes laikā?
Es izmantoju 4 Python bibliotēkas, lai šis kods darbotos un veiktu nepieciešamos uzdevumus.
1. requests
2. BeautifulSoup
3. csv
4. pandas

Bibliotēka requests ļauj strādāt ar HTTP pieprasījumiem, ar tās palīdzību es atvēru nepieciešamo url adresi un ieguvu lapas HTML kodu. Pēc tam saņemtie dati tiek nodoti citai bibliotēkai BeautifulSoup. 
Ar BeautifulSoup palīdzību es analizēju lapas HTML kodu. Es atradu vajadzīgos datus. 
Tad es šos datus saglabāju csv failā, izmantojot csv bibliotēku, un saglabāju tos xlsx failā, izmantojot pandas.

## Rrogrammatūras izmantošanas metodes
Jebkurā laikā es varu palaist programmu, kas atjaunina visus datus un sniedz jaunākos rezultātus, man vairs nav jāatver pārlūkprogramma, jāiet uz pareizo vietni un starp visu informāciju jāmeklē kopvērtējuma tabulu. Tas ievērojami samazinās patērēto laiku, arī nākotnē šo kodu var uzlabot, lai rādītu ne tikai tabulu, bet arī, teiksim, rezultātus un gaidāmās spēles.

## Es rakstīju un izstrādāju kodu VSC. Es augšupielādēju pilnībā pabeigtu versiju GitHub, tāpēc jūs nevarat redzēt izmaiņas un darba gaitu.
