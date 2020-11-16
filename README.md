# 1. domácí úkol - Úvod do programování

Skript, vytvořený v rámci předmětu Úvod do programování na PřF UK, zimní semestr 2020/2021. 
Kód má pomocí knihovny turtle vytvářet čtyři mapová zobrazení, a to Lambertovo válcové, kuželové a azimutální a Sansonovo nepravé.
Link na zadání: https://github.com/xtompok/uvod-do-prg_20/tree/master/du01

<h3> Vstup </h3>

Uživatelským vstupem, zadávaným pomocí <code> input </code> je kód zobrazení, měřítko, poloměr Země a body pro výpočet souřadnic. 
V případě nekorektního vstupu pro zobrazení se skript zeptá znovu, u dalších vstupů vyskočí chybové hlášení a skript skončí. 
Zobrazení bylo povinným vstupem a kontrola jeho validity se uskutečňuje přes totožnost s listem dostupných zobrazení. 
Dalším povinným vstupem bylo měřítko. Zde se pouze ověří, zdali se jedná o celočíselnou hodnotu <code> integer </code>. Pokud vyskočí
<code>ValueError</code>, program skončí. Poloměr Země je volitelné rozšíření, kde při zadání 0 bude nastaven jako defaultní hodnota, 6371.11 km.
Zadávání bodů pro výpočet souřadnice se realizuje, dokud uživatel po zadání zeměpisné šířky a délky nenapíše 0. Pokud je hodnota vstupu různá od nuly, 
skript se ptá na další body. Tuto část vidím jako problematickou, především z hlediska ošetření severní a jižní šířky a západní a východní délky. 

<h3> Funkce </h3>

Následuje definice funkcí, kde pro každé ze čtyř zobrazení je napsána jedna funkce. Pro výpočet souřadnic bodů v každém zobrazení je rovněž unikátní
funkce, takže dohromady je definováno 8 funkcí. Funkce pro výpočet bodů by šla napsat do jedné, kde by příslušný výpočet x,y byl realizován podmínkou,
jejíž vstupem by byl kód zobrazení. Volání funkcí je uskutečněno na posledních řádcích, kde dle vstupního zobrazení jsou volány příslušné funkce. 

<h3> Výstup </h3>

Výstupem je mapové zobrazení, kreslené pomocí modulu turtle. Uvažuje se, že jeden pixel, tedy souřadnice, které se želvě udávají je 0.3 mm. Ideální
pro výstup je tedy měřítko přibližně 120 000 000, v závislosti na zobrazení. Po nakreslení zobrazení želvou se v konzoli vypíšou souřadnice zadaných 
bodů, přepočtené do příslušného zobrazení a měřítka. 
