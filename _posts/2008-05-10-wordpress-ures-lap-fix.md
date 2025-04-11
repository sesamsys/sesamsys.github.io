---
layout: post
title: WordPress üres lap fix
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-05-10 22:13:58 +0200'
date_gmt: '2008-05-10 13:13:58 +0200'
tags:
- blank page
- fix
- wordpress
- Tech &amp; Gizmos
comments: []
---

Technoblabla következik, súlyosbítva a ténnyel, hogy nem vagyok szakértő, tehát lehet hogy hülyeség lesz.

A weboldal hibájára a következőképpen jöttünk rá. Gyanús lett, hogy a print_r( headers_list( ) ); üresen jön vissza. (Már nem nekem, sLD-nek. :D ) Ráadásul egy szimpla átirányítást végző php file gond nélkül lefutott.

Ezután visszaállítottam a weboldal témáját az előző minimal designra, és láss csodát azzal nem jött elő a fehérlap-probléma.

Innentől egyenes út vezetett a témában legutóbb szerkesztett functions.php filehoz, ahol két <?php ... ?> között lévő üres sor bizonyult a ludasnak.

Mi a teendő tehát ha üres lapokat kezd megjeleníteni a WordPress?

  1. Deaktiváld az összes plugint. Hibás plugin könnyen okozhat ilyen hibát.
  2. Cseréld ki a használt témát. Ha az új témával eltűnnek az üres oldalak, nézd át a kódot üres sorok után a php hívások körül.
  3. Ellenőrizd a WordPress config.php fileját üres sorokat keresve a végén.



A StartLogic - úgy fest - nem tehet semmiről. (Hacsak arról nem, hogy elnyomják a hibákat, és bűvészkedni kell.) Egyedül engem terhel a felelősség, én írtam át a nevezett fájlt hibásan. Tanulság: túlságosan forrófejű vagyok. (És nem értek a php-hez.)

Az RSS feed is emiatt volt tele kérdőjelekkel. Nekem már megjavult.
