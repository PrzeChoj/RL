# Agenci nauczeni grać w Skiing

1. Na oryginalnej funkcji celu. Agent nauczył się, że minimum lokalnym jest, żeby się nie ruszać. Dojedzie tak do końca zbierając nawet sporo punktów.
2. Na oryginalnej funkcji celu. Daliśmy agentowi łatwiejszy input - dostaje jedynie czarno-biały zamiast kolorowego. Nauczył się trochę ruszać.
3. Agent dostał nagrodę w czasie gry, a nie tylko na koniec. Agent dostawał punkty za znajdowanie się między bramkami. Niestety nauczył się, że jeśli przewróci się, to dostanie tą nagrodę 2 razy, więc nauczył się przewracać.
4. Agent dostawał nagrodę jedynie jeden raz po przejechaniu przez bramkę. Oduczył się przewracać, ale nie umiał wszystkich bramek zdobyć oraz bał się zakończyć epizod - zatrzymuje się na widok mety.
5. Agent dostał karę za zatrzymanie. Nauczył się przewracać o bramki. Kara za zatrzymanie była naliczana zbyt wolno.
6. Kara za zatrzymanie była naliczana szybciej, więc agent nauczył się nie przewracać. Umie zebrać wszystkie bramki.

Extra:
Agent `dont_stop_spryciarz.pt` uczył się tak samo jak 5, ale w karze za zatrzymanie się był błąd. Agent znalazł miejsce na mapie, gdzie mimo "zatrzymania się" pixele się zmieniały troszkę, więc nie dostawał kary za zatrzymanie.

