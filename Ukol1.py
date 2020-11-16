from turtle import forward, left, right, exitonclick, speed, circle, goto, penup, pendown, setpos
from math import *

print("Zadejte, jaké zobrazení si přejete vykreslit dle klíče:\n")
proj_list = [
"Lv - Lambertovo zobrazení válcové",
"La - Lambertovo zobrazení azimutální",
"Lk - Lambertovo zobrazení kuželové",
"Sa - Sansonovo zobrazení"]
for i in proj_list:
    print(i)

proj_short_list = ["Lv", "La", "Lk", "Sa"]

#Kontrola, zdali je zadaná zkratka zobrazení validní. Pokud není, program požaduje nový vstup. 
while True:
    value = input(str("Zobrazení: "))
    if value not in proj_short_list:
        print("Zadali jste špatný vstup, zadejte prosím zkratku jednoho z nabízených zobrazení.")
    else:
        break

print("Zadejte, v jakém měřítku si přejete zobrazení vykreslit. Zadejte celočíselné měřítko:")
scale = input("1 : ")

#Kontrola, zdali je měřítko celočíselné. V případě, že není, program skončí chybou. 
try:
    scale = int(scale)
except ValueError:
    print("Nezadali jste celočíselné měřítko. Program skončí chybou.")
    exit()


print("Zadejte poloměr Země v km, nebo napište 0 pro použití defaultního (6371,11 km)")
radius = input("Poloměr: ")

#Volitelná úprava poloměru Země. Kontrola, zdali je vstup číslo. 
if radius == "0":
    radius = 6371.11
else:
    try:
        radius = float(radius)
    except ValueError:
        print("Nezadali jste poměr jako číslo. Program skončí chybou.")
        exit()

X_body = []
Y_body = []
souhlas = 1

print("Zadejte zeměpisnou šířku a zeměpisnou délko délku bodu/ů.")
while souhlas != '0':
    print("Zadejte zeměpisnou šířku. Zapište jako celé či desetinné číslo.")
    sirka_stupne = input("Zeměpisná šířka: ")
    try:
        sirka_stupne = float(sirka_stupne)
    except ValueError:
        print("Nezadali jste číslo. Program skončí chybou.")
        exit()
    X_body.append(sirka_stupne)
    print("Zadejte zeměpisnou délku. Zapište jako celé či desetinné číslo.")
    delka_stupne = input("Zeměpisná délka: ")
    try:
        delka_stupne = float(delka_stupne)
    except ValueError:
        print("Nezadali jste číslo. Program skončí chybou.")
        exit()
    Y_body.append(delka_stupne)
    print("Přejete si zadat další bod? Pokud ne, napiště 0.")
    souhlas = input()

radius = radius * 100000
speed(0)
R = radius/scale/0.03

def lambert_valcove (R):
    """Funkce pro kreslení Lambertova válcového zobrazení.
    Vstupem je poloměr Země."""
    for i in range(2):
        for x in range(36):
            for y in range(18):
                for i in range(2):
                    forward(R/36)
                    left(90)
                    forward((R/36 * sin(radians(10)))*y)
                    left(90)
                left(90)
                forward((R/36 * sin(radians(10)))*y)
                right(90)
            right(90)
            forward((R/36 * sin(radians(10)))*18*y/2)
            left(90)
            forward(R/36)
        left(90)
        forward((R/36 * sin(radians(10)))*18*17)
        left(90)

def lambert_valcove_body (R):
    """Funkce pro výpočet souřadnic bodů v Lambertově válcovém zobrazení.
    Vstupem je poloměr Země."""
    for i in range (len(X_body)):
        a = round(R * radians(X_body[i]), 2)
        b = round(R * sin(radians(X_body[i])), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
    exitonclick()

def lamebert_azimutalni (R):
    """Funkce pro kreslení Lambertova azimutálního zobrazení.
    Vstupem je poloměr Země."""
    for u in range (1, 37):
        left(10)
        forward(2*R * sin(radians(90)))
        goto(0,0)
    penup()
    left(90)
    forward(2*R * sin(radians((5))))
    left(90)
    pendown()
    for v in range (1,19):
        circle(2*R * sin(radians((v*5))))
        left(90)
        penup()
        forward((2*R * sin(radians((v*5))))-(2*R * sin(radians(((v+1)*5)))))
        pendown()
        right(90)

def lambert_azimutalni_body (R):
    """Funkce pro výpočet souřadnic bodů v Lambertově azimutálním zobrazení.
    Vstupem je poloměr Země."""
    for i in range (len(X_body)):
        a = round(Y_body[i]*(cos(15)**2),2)
        b = round(2*R * (sin(radians((X_body[i]/2)))/cos(radians(15))),2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
    exitonclick()

def lambert_kuzelove (R):
    """Funkce pro kreslení Lambertova kuželového zobrazení.
    Vstupem je poloměr Země."""
    u = (36*(10*(cos(15)**2))-180)/2
    for v in range (1,19):
        left(180-u)
        forward(2*R * (sin(radians((v*5)))/cos(radians(15))))
        left(2*u)
        forward(2*R * (sin(radians((v*5)))/cos(radians(15))))
        right(90)
        circle(-2*R * (sin(radians((v*5)))/cos(radians(15))), 180+u+u)
        left(90)
        forward((2*R * (sin(radians(((v+1)*5)))/cos(radians(15))))-(2*R * (sin(radians((v*5)))/cos(radians(15)))))
        left(u)
    left(180-u)
    forward(2*R * (sin(radians((v*5)))/cos(radians(15))))
    left(2*u)
    for i in range (1, 37):
        right(10*(cos(15)**2))
        forward(2*R * (sin(radians((19*5)))/cos(radians(15))))
        left(180)
        forward(2*R * (sin(radians((19*5)))/cos(radians(15))))
        left(180)

def lambert_kuzelove_body (R):
    """Funkce pro výpočet souřadnic bodů v Lambertově kuželovém zobrazení.
    Vstupem je poloměr Země."""
    for i in range (len(X_body)):
        a = round(Y_body[i]*(cos(15)**2), 2)
        b = round(2*R * (sin(radians((X_body[i]/2)))/cos(radians(15))), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
    exitonclick()

def sanson (R):
    """Funkce pro kreslení Sansonova zobrazení.
    Vstupem je poloměr Země."""
    for u in range (0, 90, 10):
        for v in range (0, 180, 10):
            if v == 0:
                penup()
            else:
                pendown()
            y = (R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(x,y)
            setpos(-x,y)
    for u in range (0, 90, 10):
        for v in range (0, 180, 10):
            if v == 0:
                penup()
            else:
                pendown()
            y = -(R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(x,y)
            setpos(-x,y)
    for v in range (0, 180, 10):
        for u in range (0, 100, 10):
            if u == 0:
                penup()
            else:
                pendown()
            y = (R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(x,y)
        for u in range (0, 100, 10):
            if u == 0:
                penup()
            else:
                pendown()
            y = (R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(-x,y)
        for u in range (0, 100, 10):
            if u == 0:
                penup()
            else:
                pendown()
            y = (R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(x,-y)
        for u in range (0, 100, 10):
            if u == 0:
                penup()
            else:
                pendown()
            y = (R*radians(u))
            x = (R*radians(v)*cos(radians(u)))
            setpos(-x,-y)

def sanson_body (R):
    """Funkce pro kreslení bodů v Sansonově zobrazení.
    Vstupem je poloměr Země."""
    for i in range (len(X_body)):
        a = round(R * radians(Y_body[i]) * cos(radians(X_body[i])), 2)
        b = round(R * radians(Y_body[i]), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
    exitonclick()

if value == "Lv":
    lambert_valcove(R)
    lambert_valcove_body(R)
elif value == "La":
    lamebert_azimutalni(R)
    lambert_azimutalni_body(R)
elif value == "Lk":
    lambert_kuzelove(R)
    lambert_kuzelove_body(R)
elif value == "Sa":
    sanson(R)
    sanson_body(R)
