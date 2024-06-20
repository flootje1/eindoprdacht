import tkinter as tk
from tkinter import messagebox

# gemaakt door stijn
# Klasse voor het berekenen van BTW
class BTWCalculator:
    # Methode voor het berekenen van BTW
    def bereken_btw(self, bedrag):
        try:
            bedrag = float(bedrag)
            btw_percentage = 0.21  # BTW percentage
            btw_bedrag = bedrag * btw_percentage
            totaal_bedrag = bedrag + btw_bedrag
            return bedrag, btw_bedrag, totaal_bedrag
        except ValueError:
            # Terugkeerwaarde bij foutieve invoer
            return None, None, None

# gemaakt door stijn
# Klasse voor het berekenen van reistijd
class ReistijdCalculator:
    # Methode voor het berekenen van reistijd
    def bereken_reistijd(self, afstand, snelheid):
        try:
            afstand = float(afstand)
            snelheid = float(snelheid)
            reistijd = afstand / snelheid
            return reistijd
        except ValueError:
            # Terugkeerwaarde bij foutieve invoer
            return None

# gemaakt door stijn
# Klasse voor het berekenen van de omtrek en oppervlakte van een vierkant
class VierkantCalculator:
    # Methode voor het berekenen van omtrek en oppervlakte
    def bereken_vierkant(self, lengte, breedte):
        try:
            lengte = float(lengte)
            breedte = float(breedte)
            omtrek = 2 * (lengte + breedte)
            oppervlakte = lengte * breedte
            return omtrek, oppervlakte
        except ValueError:
            # Terugkeerwaarde bij foutieve invoer
            return None, None

# gemaakt door florian
# Klasse voor het berekenen van de omtrek en oppervlakte van een cirkel
class CirkelCalculator:
    # Methode voor het berekenen van omtrek en oppervlakte
    def bereken_cirkel(self, diameter):
        try:
            diameter = float(diameter)
            straal = diameter / 2
            omtrek = 2 * 3.14 * straal
            oppervlakte = 3.14 * straal ** 2
            return omtrek, oppervlakte
        except ValueError:
            # Terugkeerwaarde bij foutieve invoer
            return None, None

# gemaakt door florian
# Klasse voor het omrekenen van valuta
class ValutaOmrekenen:
    def __init__(self):
        # Wisselkoersen voor valuta omrekening
        self.wisselkoersen = {"EURUSD": 1.2, "USDGBP": 0.8}
    
    # Methode voor het omrekenen van valuta
    def omrekenen(self, bedrag, van_valuta, naar_valuta):
        try:
            bedrag = float(bedrag)
            wisselkoers = self.wisselkoersen.get(van_valuta + naar_valuta)
            if wisselkoers:
                omgerekend_bedrag = bedrag * wisselkoers
                return omgerekend_bedrag
            else:
                return None
        except ValueError:
            # Terugkeerwaarde bij foutieve invoer
            return None

# gemaakt door florian
# GUI applicatie voor het berekenen van BTW
class BTWCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("BTW Calculator")
        
        # Label voor invoerbedrag
        self.label = tk.Label(master, text="Voer het bedrag in:")
        self.label.pack()
        
        # Invoerveld voor bedrag
        self.bedrag_entry = tk.Entry(master)
        self.bedrag_entry.pack()
        
        # Knop voor het berekenen van BTW
        self.bereken_button = tk.Button(master, text="Bereken BTW", command=self.bereken_btw)
        self.bereken_button.pack()
        
        # Label voor het weergeven van het resultaat
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
        
        # BTWCalculator instantie
        self.calculator = BTWCalculator()
    
    # Methode die wordt aangeroepen bij het klikken op de bereken-knop
    def bereken_btw(self):
        bedrag = self.bedrag_entry.get()
        bedrag, btw, totaal = self.calculator.bereken_btw(bedrag)
        if bedrag is not None:
            self.resultaat_label.config(text=f"Bedrag: {bedrag}\nBTW: {btw}\nTotaal: {totaal}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer een geldig bedrag in.")

# gemaakt door stijn
# GUI applicatie voor het berekenen van reistijd
class ReistijdCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Reistijd Calculator")
        
        # Label voor invoerafstand
        self.afstand_label = tk.Label(master, text="Voer de afstand in (km):")
        self.afstand_label.pack()
        
        # Invoerveld voor afstand
        self.afstand_entry = tk.Entry(master)
        self.afstand_entry.pack()
        
        # Label voor invoersnelheid
        self.snelheid_label = tk.Label(master, text="Voer de snelheid in (km/u):")
        self.snelheid_label.pack()
        
        # Invoerveld voor snelheid
        self.snelheid_entry = tk.Entry(master)
        self.snelheid_entry.pack()
        
        # Knop voor het berekenen van reistijd
        self.bereken_button = tk.Button(master, text="Bereken Reistijd", command=self.bereken_reistijd)
        self.bereken_button.pack()
        
        # Label voor het weergeven van het resultaat
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
        
        # ReistijdCalculator instantie
        self.calculator = ReistijdCalculator()
    
    # Methode die wordt aangeroepen bij het klikken op de bereken-knop
    def bereken_reistijd(self):
        afstand = self.afstand_entry.get()
        snelheid = self.snelheid_entry.get()
        reistijd = self.calculator.bereken_reistijd(afstand, snelheid)
        if reistijd is not None:
            self.resultaat_label.config(text=f"Geschatte reistijd: {reistijd:.2f} uur")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer geldige afstand en snelheid in.")

# gemaakt door stijn
# GUI applicatie voor het berekenen van omtrek en oppervlakte van een vierkant
class VierkantCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Vierkant Calculator")
        
        # Label voor invoerlengte
        self.lengte_label = tk.Label(master, text="Voer de lengte van het vierkant in:")
        self.lengte_label.pack()
        
        # Invoerveld voor lengte
        self.lengte_entry = tk.Entry(master)
        self.lengte_entry.pack()
        
        # Label voor invoerbreedte
        self.breedte_label = tk.Label(master, text="Voer de breedte van het vierkant in:")
        self.breedte_label.pack()
        
        # Invoerveld voor breedte
        self.breedte_entry = tk.Entry(master)
        self.breedte_entry.pack()
        
        # Knop voor het berekenen van omtrek en oppervlakte
        self.bereken_button = tk.Button(master, text="Bereken Vierkant", command=self.bereken_vierkant)
        self.bereken_button.pack()
        
        # Label voor het weergeven van het resultaat
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
        
        # VierkantCalculator instantie
        self.calculator = VierkantCalculator()
    
    # Methode die wordt aangeroepen bij het klikken op de bereken-knop
    def bereken_vierkant(self):
        lengte = self.lengte_entry.get()
        breedte = self.breedte_entry.get()
        omtrek, oppervlakte = self.calculator.bereken_vierkant(lengte, breedte)
        if omtrek is not None:
            self.resultaat_label.config(text=f"Omtrek: {omtrek}\nOppervlakte: {oppervlakte}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer geldige lengte en breedte in.")

# gemaakt door stijn
# GUI applicatie voor het berekenen van omtrek en oppervlakte van een cirkel
class CirkelCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cirkel Calculator")
        
        # Label voor invoerdiameter
        self.diameter_label = tk.Label(master, text="Voer de diameter van de cirkel in:")
        self.diameter_label.pack()
        
        # Invoerveld voor diameter
        self.diameter_entry = tk.Entry(master)
        self.diameter_entry.pack()
        
        # Knop voor het berekenen van omtrek en oppervlakte
        self.bereken_button = tk.Button(master, text="Bereken Cirkel", command=self.bereken_cirkel)
        self.bereken_button.pack()
        
        # Label voor het weergeven van het resultaat
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
        
        # CirkelCalculator instantie
        self.calculator = CirkelCalculator()
    
    # Methode die wordt aangeroepen bij het klikken op de bereken-knop
    def bereken_cirkel(self):
        diameter = self.diameter_entry.get()
        omtrek, oppervlakte = self.calculator.bereken_cirkel(diameter)
        if omtrek is not None:
            self.resultaat_label.config(text=f"Omtrek: {omtrek:.2f}\nOppervlakte: {oppervlakte:.2f}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer een geldige diameter in.")

# gemaakt door stijn
# GUI applicatie voor het omrekenen van valuta
class ValutaOmrekenenApp:
    def __init__(self, master):
        self.master = master
        master.title("Valuta Omrekenen")
        
        # Label voor invoerbedrag
        self.bedrag_label = tk.Label(master, text="Voer het bedrag in:")
        self.bedrag_label.pack()
        
        # Invoerveld voor bedrag
        self.bedrag_entry = tk.Entry(master)
        self.bedrag_entry.pack()
        
        # Label voor invoer van valuta
        self.van_valuta_label = tk.Label(master, text="Van valuta (bijv. EUR):")
        self.van_valuta_label.pack()
        
        # Invoerveld voor van valuta
        self.van_valuta_entry = tk.Entry(master)
        self.van_valuta_entry.pack()
        
        # Label voor invoer naar valuta
        self.naar_valuta_label = tk.Label(master, text="Naar valuta (bijv. USD):")
        self.naar_valuta_label.pack()
        
        # Invoerveld voor naar valuta
        self.naar_valuta_entry = tk.Entry(master)
        self.naar_valuta_entry.pack()
        
        # Knop voor het omrekenen van valuta
        self.bereken_button = tk.Button(master, text="Omrekenen", command=self.omrekenen)
        self.bereken_button.pack()
        
        # Label voor het weergeven van het resultaat
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
        
        # ValutaOmrekenen instantie
        self.calculator = ValutaOmrekenen()
    
    # Methode die wordt aangeroepen bij het klikken op de bereken-knop
    def omrekenen(self):
        bedrag = self.bedrag_entry.get()
        van_valuta = self.van_valuta_entry.get().upper()
        naar_valuta = self.naar_valuta_entry.get().upper()
        omgerekend_bedrag = self.calculator.omrekenen(bedrag, van_valuta, naar_valuta)
        if omgerekend_bedrag is not None:
            self.resultaat_label.config(text=f"Omgerekend bedrag: {omgerekend_bedrag:.2f} {naar_valuta}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Controleer de valutacodes.")

# Klasse voor het hoofdmenu van de applicatie
class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Functionaliteit Schermen")
        
        # Menubalk voor de verschillende functionaliteiten
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        
        self.create_menu()
    
    # Methode voor het aanmaken van het menu
    def create_menu(self):
        functionaliteit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Functionaliteit", menu=functionaliteit_menu)
        functionaliteit_menu.add_command(label="BTW Calculator", command=self.open_btw_calculator)
        functionaliteit_menu.add_command(label="Reistijd Calculator", command=self.open_reistijd_calculator)
        functionaliteit_menu.add_command(label="Vierkant Calculator", command=self.open_vierkant_calculator)
        functionaliteit_menu.add_command(label="Cirkel Calculator", command=self.open_cirkel_calculator)
        functionaliteit_menu.add_command(label="Valuta Omrekenen", command=self.open_valuta_omrekenen)
    
    # Methode voor het openen van de BTW calculator
    def open_btw_calculator(self):
        window = tk.Toplevel(self.master)
        app = BTWCalculatorApp(window)
    
    # Methode voor het openen van de reistijd calculator
    def open_reistijd_calculator(self):
        window = tk.Toplevel(self.master)
        app = ReistijdCalculatorApp(window)
    
    # Methode voor het openen van de vierkant calculator
    def open_vierkant_calculator(self):
        window = tk.Toplevel(self.master)
        app = VierkantCalculatorApp(window)
    
    # Methode voor het openen van de cirkel calculator
    def open_cirkel_calculator(self):
        window = tk.Toplevel(self.master)
        app = CirkelCalculatorApp(window)
    
    # Methode voor het openen van de valuta omreken applicatie
    def open_valuta_omrekenen(self):
        window = tk.Toplevel(self.master)
        app = ValutaOmrekenenApp(window)

# Hoofdprogramma voor het starten van de applicatie
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
