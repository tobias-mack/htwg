#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from threading import Event
from threading import Lock
import time
from math import floor


F = 20 #x-Fache Geschwindigkeit
printLock = Lock()


class KundIn(Thread):
    def __init__(self, Einkaufsliste, Kundentyp, Kundennummer):
        Thread.__init__(self)
        self.Einkaufsliste = Einkaufsliste
        self.Kundentyp = Kundentyp
        self.Kundennummer = Kundennummer
        self.servEv = Event()
        self.Vollständig = True
        self.beginEinkauf = 0       #Zeitpunkt Anfang
        self.endeEinkauf = 0        #          Ende

    def run(self):
        self.beginEinkauf = time.perf_counter() #Einkauf Start für Kunde
        printLock.acquire()
        AnzahlKunden.hochzählen()               #Kundenanzahl++
        printLock.release()
        
        while True:
            time.sleep(self.Einkaufsliste[0][0]/F)  #Hinweg Kunde

            if len(self.Einkaufsliste[0][3].Warteschlange) > self.Einkaufsliste[0][1]: #Überpsringen wenn Warteschlange zu groß
                printLock.acquire()
                self.Einkaufsliste[0][3].überspringen = self.Einkaufsliste[0][3].überspringen + 1
                end = time.perf_counter()
                print(floor((end-begin)*F), self.Kundentyp, self.Kundennummer, "überspringt", self.Einkaufsliste[0][3].Stationsname)
                del self.Einkaufsliste[0]
                self.Vollständig = False
                printLock.release()
            else:
                printLock.acquire()
                end = time.perf_counter()
                print(floor((end-begin)*F), self.Kundentyp, self.Kundennummer, "stellt sich an", self.Einkaufsliste[0][3].Stationsname, "an")
                self.Einkaufsliste[0][3].Warteschlange.append((self.servEv, self.Einkaufsliste[0][2]))
                
                
                self.Einkaufsliste[0][3].arrEv.set()
                printLock.release()

                self.servEv.wait()      #Wartet solange bis Station ihn aufweckt

                printLock.acquire()
                end = time.perf_counter()
                print(floor((end-begin)*F), self.Kundentyp, self.Kundennummer, "verlässt", self.Einkaufsliste[0][3].Stationsname)
                del self.Einkaufsliste[0]
                self.servEv.clear()
                printLock.release()

            #Sollte Einkaufsliste leer
            if self.Einkaufsliste == []:
                self.endeEinkauf = time.perf_counter()      #Zeitpunkt Ende
                printLock.acquire()
                AnzahlKunden.Gesamteinkauf(floor((self.endeEinkauf-self.beginEinkauf)*F))   #Zeitdifferenz für ein Kunde
                printLock.release()
                if self.Vollständig == True:
                    printLock.acquire()
                    AnzahlKunden.hochzählen_vollständig()
                    AnzahlKunden.Gesamteinkauf_vollständig(floor((self.endeEinkauf-self.beginEinkauf)*F))
                    printLock.release()
                if self.Kundentyp == 'A' and self.Kundennummer == 10 and AnzahlKunden.Kundenzahl == 40:     #Wenn alle Fertig und Anzahl erreicht
                    Auswertung()
                break





class Station(Thread):
    def __init__(self, Abarbeitungsdauer, Stationsname):
        Thread.__init__(self)
        self.Stationsname = Stationsname
        self.Abarbeitungsdauer = Abarbeitungsdauer
        self.Warteschlange = []
        self.arrEv = Event()
        self.überspringen = 0
        self.bedient = 0


    def run(self):
        while True:
            self.arrEv.wait()

            time.sleep((self.Warteschlange[0][1] * self.Abarbeitungsdauer)/F)
            self.Warteschlange[0][0].set()  #Wieder Kunde aufwecken


            printLock.acquire()
            self.bedient = self.bedient + 1
            del self.Warteschlange[0]
            if self.Warteschlange == []:    #Wenn niemand ansteht dann schlafen
                self.arrEv.clear()
            printLock.release()


class start(Thread):
    def __init__(self, Startpunkt, Startzeit):
        Thread.__init__(self)
        self.Startpunkt = Startpunkt
        self.Startzeit = Startzeit

#Erstellt Kunden
    def run(self):
        time.sleep(self.Startpunkt/F)
        n = self.Startpunkt
        a = 0
        b = 0
        while n < 1801:
            if(n % self.Startzeit == 0):
                a = a+1
                TypA = [(10, 10, 10, Bäcker), (30, 10, 5, Metzger), (45, 5, 3, Käse), (60, 20, 30, Kasse)]
                Kunde = KundIn(TypA, 'A', a)
                Kunde.start()
            if(n % self.Startzeit == 1):
                b = b + 1
                TypB = [(30, 5, 2, Metzger), (30, 20, 3, Kasse), (20, 20, 3, Bäcker)]
                Kunde = KundIn(TypB, 'B', b)
                Kunde.start()
            n = n + self.Startzeit
            time.sleep(self.Startzeit/F)


class Kundenzähler:
    def __init__(self):
        self.Kundenzahl = 0
        self.vollständig = 0
        self.Dauer = 0
        self.Dauer_vollständig = 0


    def hochzählen(self):
        self.Kundenzahl = self.Kundenzahl + 1

    def hochzählen_vollständig(self):
        self.vollständig = self.vollständig + 1

    def Gesamteinkauf(self,Einkaufs_Dauer):
        self.Dauer = self.Dauer + Einkaufs_Dauer

    def Gesamteinkauf_vollständig(self,Einkaufs_Dauer):
        self.Dauer_vollständig = self.Dauer_vollständig + Einkaufs_Dauer


def Auswertung():
    ende = time.perf_counter()
    print("Simulationsende:", floor((ende-begin)*F))
    print("Anzahl Kunden:", AnzahlKunden.Kundenzahl)
    print("Anzahl vollständige Einkäufe:", AnzahlKunden.vollständig)
    print("Durchschnittliche Einkaufsdauer:", AnzahlKunden.Dauer/AnzahlKunden.Kundenzahl)
    print("Durchscnittliche Einkaufsdauer (vollständig):", AnzahlKunden.Dauer_vollständig/AnzahlKunden.vollständig)
    print("Bäcker übersprungen (in %)", (Bäcker.überspringen/(Bäcker.bedient+Bäcker.überspringen))*100)
    print("Metzger übersprungen (in %)", (Metzger.überspringen/(Metzger.bedient+Metzger.überspringen))*100)
    print("Käse übersprungen (in %)", (Käse.überspringen/(Käse.bedient+Käse.überspringen))*100)
    print("Kasse übersprungen (in %)", (Kasse.überspringen/(Kasse.bedient+Kasse.überspringen))*100)



#main
AnzahlKunden = Kundenzähler()

begin = time.perf_counter()
Bäcker = Station(10, "Bäcker")
Metzger = Station(30, "Metzger")
Käse = Station(60, "Käse")
Kasse = Station(5, "Kasse")

KundeA = start(0, 200)
KundeB = start(1, 60)

Bäcker.start()
Metzger.start()
Käse.start()
Kasse.start()
KundeA.start()
KundeB.start()

