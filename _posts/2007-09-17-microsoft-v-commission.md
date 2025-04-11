---
layout: post
title: Microsoft v Commission
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-09-17 18:30:35 +0200'
date_gmt: '2007-09-17 09:30:35 +0200'
tags:
- EU
- Law
- Tech &amp; Gizmos
comments: []
---

Az Elsőfokú Bíróság ma reggel hirdette ki döntését a _Microsoft kontra Bizottság_ ügyben. Gondolom sokan emlékeznek az Európai Bizottság 2004-es döntésére, ahol közel félmilliárd Eurós büntetést róttak ki a Microsoftra az EU versenytörvényeinek megsértéséért. Erre kért bírósági felülvizsgálatot a Microsoft.

Az ügy két részre tagolódik. A sokak által ismert és inkább nevetségesnek mint komolynak tartott része a döntésnek a beépített Windows Media Player (WMP) körüli huzavona. A Bizottság szerint azzal, hogy a Windows-zal együtt a WMP-t is megkapja a vásárló (bundled software) a Microsoft gyakorlatilag ellehetetlenítette a konkurenseket a médialejátszó piacon. Ennek erdeményeként kellett egy speciális Windows-verziót bevezetni az EU piacra, amelyben nincs benne a WMP. A WMP persze ingyen letölthető ennek ellenére, valamint mindenki úgyis azt használ, amit akar. Más kérdés, hogy valóban ki fizetne egy lejátszóért, amikor kap "ingyen" Micrisoftéktól.

A lényegesebbik - és sokkal kevesebbet emlegetett - része a döntésnek azonban az interoperabilitás (együttműködés) kérdése. Ez a WGS (WorkGroup Server) piacra vonatkozik elsősorban. A lényege, hogy a versenytársak elégtelennek találták a Microsoft által nekik juttatott információkat, melyekre szükség van ahhoz, hogy az ő szoftvereik is együtt tudjanak működni a Microsoft termékeivel.

Az alapvető dilemma az, hogy a Microsoft szoftverei mind zárt forrású, jogvédett, egyes esetekben szabadalmaztatott szoftverek. Az interoperabilitáshoz szükséges információ viszont egyenlő a forráskód egyes részeivel, pont amit fenti szerzői jogok és szabadalmak védenek. Ezen információ hiánya esetén azonban a versenytársak képtelenek olyan szoftvereket írni, amelyek adott esetben együtt tudnak működni a Microsoft piacvezető termékeivel, de facto kizárva ezzel a verseny lehetőségét.

Ahhoz, hogy megértsük a bizottsági döntés mögötti logikát kissé vissza kell mennünk az időben, egészen pontosan 1980-as évek végéig, a _Magill_ -ügyig.

Akkoriban három televízióadó működött Írországban, és ezek mind kiadták a saját műsorújságjukat. Magill lehetőséget látott a dologban, és kiadott egy saját műsorújságot, mely mindhárom adó programjait tartalmazta. A tévéadók azonban arra hivatkoztak, hogy a műsorra vonatkozó információkat szerzői jogok illetik meg, így Magill jogsértést követett el. Magill erre panaszt tett az Európai Bizottságnál, miszerint a televíziók visszaéltek monopolhelyzetükkel. Érvéként az [Európai Unióról szóló szerződés 82. cikkelyét](http://eur-lex.europa.eu/LexUriServ/site/hu/oj/2006/ce321/ce32120061229hu00010331.pdf) hozta fel:

> A közös piaccal összeegyeztethetetlen és tilos egy vagy több vállalkozásnak a közös piacon vagy annak jelentős részén meglévő erőfölényével való visszaélése, amennyiben ez hatással lehet a tagállamok közötti kereskedelemre.

Az akkori döntés sokkoló, és mint az később bebizonyosodott precedensértékű volt: a Bizottság kötelezte a TV-adókat, hogy megosszák a programjaikkal kapcsolatos információkat Magillal.

> 12 In that decision the Commission found that there had been a breach of Article 86 of the EEC Treaty and ordered the three organizations to put an end to that breach, in particular "by supplying ... third parties on request and on a non-discriminatory basis with their individual advance weekly programme listings and by permitting reproduction of those listings by such parties". It was also provided that, if the three organizations chose to grant reproduction licences, any royalties requested should be reasonable.

A TV-adók előbb sikertelenül kezdeményezett felülvizsgálatot az Elsőfokú Bíróságon (CFI), majd fellebbezett az Európai Bíróságon (ECJ). Az [Európai Bíróság 1995-ös ítéletében](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:61991J0241:EN:HTML) egyetértett, hogy a jogvédett információk licenszelésének megtagadása nem jelenti a 82. cikkely megsértését. Azonban a bíróság bevezette az ún. kivételes eseteket (exceptional circumstances), melyek a következők:

1) A programinformáció megtagadása gyakorlatilag a **verseny teljes ellehetetlenítésével egyenlő** a műsorújságok piacán (downstream market).

> 53 Thus the appellants - who were, by force of circumstance, the only sources of the basic information on programme scheduling which is the indispensable raw material for compiling a weekly television guide - gave viewers wishing to obtain information on the choice of programmes for the week ahead no choice but to buy the weekly guides for each station and draw from each of them the information they needed to make comparisons.

2) Valamint hogy a TV-adók ténykedése **meghiúsította egy lehetséges új termék megjelenését a piacon, melyre ráadásul fogyasztói igény is mutatkozott**.

> 54 The appellants' refusal to provide basic information by relying on national copyright provisions thus prevented the appearance of a new product, a comprehensive weekly guide to television programmes, which the appellants did not offer and for which there was a potential consumer demand. Such refusal constitutes an abuse under heading (b) of the second paragraph of Article 86 of the Treaty.

3) A bíróság nem látta **objektív okát** az információ megtagadásának.

> 55 Second, there was no justification for such refusal either in the activity of television broadcasting or in that of publishing television magazines (RTE judgment, paragraph 73, and ITP judgment, paragraph 58).

Egészen sokáig ez a Magill-ítélet volt az alapja a legtöbb szellemi tulajdon (IP) kontra verseny témájú ügynek. Két dolgot azonban érdemes megjegyezni ezzel kapcsolatban. Egyik, hogy sok kritikus szerint a kivételes esetek definíciói túlságosan is kötődnek a Magill-ügy tényeihez, így roppant nehéz őket alkalmazni más esetekben. Valamint hogy a kérdéses szellemi tulajdon Magill esetében úgynevezett _weak IP_ , azaz gyenge szellemi tulajdonnak minősül.

(Érdeklődőknek a következő ügyek ajánlhatóak: Magill-előzmény a _Volvo v Veng_ , folyomány az _IMS Health_ ügy.)

Tehát a Microsoft-ügy három kérdéses pontja a következő:

1) A szóban forgó IP nem mondható banálisnak vagy "gyengének", ellentétben a műsorújságokéval. A Microsoft próbálkozott is - hiábavalóan - hivatkozni a szabadalmaira és szellemi tulajdonjogaira. Kérdés tehát, hogy az IP megléte befolyásolja-e az interoperabilitásról szóló vitát.

2) A Microsoft-ügyben a Bizottság igencsak szabadon bánt a kivételes kondíciókkal. Teljesen kimaradt például az új termék megjelenésének igénye. (A versenytársak nem új termékeket, hanem a Microsoftéval megegyező feladatot végző szoftvereket kívántak elsősorban fejleszteni.)

3) Eléggé megkérdőjelenzhető pontosan mit értett a Bizottság interoperabilitási információk alatt. A döntésben a Bizottság arra hivatkozott, hogy az ő verziójuk konzisztens a szoftverekről szóló [91/250-es EC direktívával](http://en.wikipedia.org/wiki/Directive_on_the_legal_protection_of_computer_programs). Kritikusok szerint azonban meglehetősen kitágították a kört.

A Microsoft felülvizsgálati keresetében az alábbiakra hivatkozott:

1) Tagadta, hogy az interoperabilitáshoz szükséges információk elengedhetetlenek lennének a versenytársak számára konkurens szoftverek fejlesztéséhez. A valóság szerintük az, hogy már most is akárki versenybe szállhat velük ezeken a piacokon, ahogyan azt aktívan teszik is konkurenseik.

2) A bíróság szerinte hibásan mérte fel a szembenálló érdekeket: a Microsoft érdekét az innovációra (melyhez szüksége van betartatható szellemi tulajdonjogokra) és az egész ágazat innovációjára vonatkozó hatást. Szerintük az előbbinek kellene előnyt élveznie.

Ez nagyjából konzisztens [Szamosi Katalinnak, a Magyar Versenyjogi Egyesület elnökének az ítéletet megelőző írásával](http://hvg.hu/Tudomany/20070916_microsoft_europai_bizottsag_per_itelet_hi.aspx). Hogy én is lehessek [rosszmájú](http://velemenyemvan.freeblog.hu/archives/2007/09/17/Ma_lesz_itelet_a_Microsoft_kontra_mindenki_ugyben), csak nem a Microsoft Magyarország keze van a dologban? :)

> Az Európai Bíróság döntése a szellemi tulajdont védők eddig jól körülbástyázott és jól működő rendjének fellazítását eredményezheti. Egy precedens értékű ítélet ugyanis feljogosíthatja bármilyen ipari ágazat szereplőit, hogy a versenytársak szellemi alkotásával kapcsolatos információkat megszerezzék pusztán azon az alapon, hogy kapcsolódó termékeket kívánnak gyártani. A fejlesztési információk olyan, a találmányhoz kötődő, vagyoni értéket képviselő tudásanyagok, amelyek átengedésére csak egyedi esetben és ellenérték fejében kerülhet sor.

A reggeli döntése az Elsőfokú Bíróságnak pedig, hogy elutasítja a Microsoft fellebbezését, és egy apró változtatás kivételével fenntartja a Bizottság döntését. ([Microsoft loses anti-trust appeal](http://news.bbc.co.uk/2/hi/business/6998272.stm))

Újrajátszás az Európai Bíróságon gondolom.
