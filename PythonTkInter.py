import tkinter as tk

class Window:
    def __init__(self, title, geometry, icon_path):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.iconbitmap(icon_path)

    def run(self):
        self.root.mainloop()


class OhmGUI:
    def __init__(self, window):
        self.window = window

        self.lbltext = tk.Label(window.root, text="Introdu valori pentru a putea calcula!")
        self.lbltext.grid(row=0, column=0, columnspan=3, padx=0, pady=20)

        self.lblVolti = tk.Label(window.root, text="Volti", fg="blue")
        self.lblVolti.grid(row=1, column=0, padx=0, pady=10)

        self.lblAmperi = tk.Label(window.root, text="Amperi", fg="blue")
        self.lblAmperi.grid(row=1, column=1, padx=0, pady=10)

        self.lblOhm = tk.Label(window.root, text="Unitati Ohm", fg="blue")
        self.lblOhm.grid(row=1, column=2, padx=0, pady=10)

        self.VoltiEntry = tk.Entry(window.root)
        self.VoltiEntry.grid(row=2, column=0, padx=10, pady=10)

        self.AmperiEntry = tk.Entry(window.root)
        self.AmperiEntry.grid(row=2, column=1, padx=10, pady=10)

        self.RezultatOhm = tk.Label(window.root, text="")
        self.RezultatOhm.grid(row=2, column=2, padx=10, pady=10)

        self.btnCalculeaza = tk.Button(window.root, text="Calculeaza", command=self.calculate_ohm, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeaza.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

        window.root.grid_columnconfigure(0, weight=1)
        window.root.grid_columnconfigure(1, weight=1)
        window.root.grid_columnconfigure(2, weight=1)

    def calculate_ohm(self):
        try:
            volti = float(self.VoltiEntry.get())
            amperi = float(self.AmperiEntry.get())

            ohm_units = volti / amperi
            truncated_ohm_units = round(ohm_units, 2)

            self.RezultatOhm.config(text=str(truncated_ohm_units))
        except ValueError:
            self.RezultatOhm.config(text="Invalid input, enter only digits!")

class PowerGUI:
    def __init__(self, window):
        self.window = window

        self.lbltext = tk.Label(window.root, text="Introdu valori pentru a putea calcula!")
        self.lbltext.grid(row=0, column=0, columnspan=3, padx=0, pady=20)

        self.lblVolti = tk.Label(window.root, text="Volti", fg="blue")
        self.lblVolti.grid(row=1, column=0, padx=0, pady=10, sticky="e")

        self.lblAmperi = tk.Label(window.root, text="Amperi", fg="blue")
        self.lblAmperi.grid(row=2, column=0, padx=0, pady=10, sticky="e")

        self.VoltiEntry = tk.Entry(window.root)
        self.VoltiEntry.grid(row=1, column=1, padx=10, pady=10)

        self.AmperiEntry = tk.Entry(window.root)
        self.AmperiEntry.grid(row=2, column=1, padx=10, pady=10)

        self.RezultatOhm = tk.Label(window.root, text="")
        self.RezultatOhm.grid(row=4, column=1, padx=10, pady=10)

        self.btnCalculeazaP = tk.Button(window.root, text="Calculeaza putere", command=self.calculate_power, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeazaP.grid(row=3, column=1, padx=10, pady=20)

        self.lblPower = tk.Label(window.root, text="Puterea", fg="blue")
        self.lblPower.grid(row=5, column=0, padx=0, pady=10, sticky="e")

        self.lblTimp = tk.Label(window.root, text="Timp", fg="blue")
        self.lblTimp.grid(row=6, column=0, padx=0, pady=10, sticky="e")

        self.PowerEntry = tk.Entry(window.root)
        self.PowerEntry.grid(row=5, column=1, padx=10, pady=10)

        self.TimeEntry = tk.Entry(window.root)
        self.TimeEntry.grid(row=6, column=1, padx=10, pady=10)

        self.lblE = tk.Label(window.root, text="")
        self.lblE.grid(row=8, column=1, padx=10, pady=10)

        self.btnCalculeazaE = tk.Button(window.root, text="Calculeaza energie", command=self.calculate_energy, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeazaE.grid(row=7, column=1, padx=10, pady=20)

        self.lblEnergy = tk.Label(window.root, text="Energie", fg="blue")
        self.lblEnergy.grid(row=9, column=0, padx=0, pady=10, sticky="e")

        self.lblPower2 = tk.Label(window.root, text="Putere", fg="blue")
        self.lblPower2.grid(row=10, column=0, padx=0, pady=10, sticky="e")

        self.EnergyEntry = tk.Entry(window.root)
        self.EnergyEntry.grid(row=9, column=1, padx=10, pady=10)

        self.PowerEntry2 = tk.Entry(window.root)
        self.PowerEntry2.grid(row=10, column=1, padx=10, pady=10)

        self.lblT = tk.Label(window.root, text="")
        self.lblT.grid(row=12, column=1, padx=0, pady=10)

        self.btnCalculeazaT = tk.Button(window.root, text="Calculeaza timp", command=self.calculate_time, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeazaT.grid(row=11, column=1, padx=10, pady=20)

        self.lblResult = tk.Label(window.root, text="")
        self.lblResult.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        window.root.grid_columnconfigure(0, weight=1)
        window.root.grid_columnconfigure(1, weight=1)

        window.root.grid_rowconfigure(0, weight=1)
        window.root.grid_rowconfigure(12, weight=1)

    def calculate_power(self):
        try:
            volti = float(self.VoltiEntry.get())
            amperi = float(self.AmperiEntry.get())
            putere = volti * amperi
            self.RezultatOhm.config(text=f"Puterea calculata: {putere} W", fg="green")
            self.lblResult.config(text="")
        except:
            self.RezultatOhm.config(text="Invalid input, enter only digits!", fg="Red")

    def calculate_energy(self):
        try:
            putere = float(self.PowerEntry.get())
            timp = float(self.TimeEntry.get())
            energie = putere * timp
            self.lblE.config(text=f"Energie calculata: {energie} J", fg="green")
            self.lblResult.config(text="")
        except:
            self.lblE.config(text="Invalid input, enter only digits!", fg="Red")

    def calculate_time(self):
        try:
            energie = float(self.EnergyEntry.get())
            putere = float(self.PowerEntry2.get())
            timp = energie / putere
            self.lblT.config(text=f"Timpul calculat: {timp} secunde", fg="green")
            self.lblResult.config(text="")
        except:
            self.lblT.config(text="Invalid input, enter only digits!", fg="Red")


class MainGUI:
    def __init__(self, window):
        self.window = window

        self.lbltext = tk.Label(window.root, text="Interfata principala")
        self.lbltext.grid(row=0, column=0, columnspan=3, padx=0, pady=20)

        self.btnCalculeaza = tk.Button(window.root, text="Intra pentru a calcula Ohm", command=self.open_ohm_gui, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeaza.grid(row=1, column=0, columnspan=3, padx=10, pady=20, sticky="n")

        self.btnCalculeaza = tk.Button(window.root, text="Intra pentru a calcula general", command=self.open_power_gui, relief="raised", bg="white", fg="black", activebackground="red", activeforeground="white")
        self.btnCalculeaza.grid(row=2, column=0, columnspan=3, padx=10, pady=20, sticky="n")


        window.root.grid_columnconfigure(0, weight=1)
        window.root.grid_columnconfigure(1, weight=1)
        window.root.grid_columnconfigure(2, weight=1)

    def open_ohm_gui(self):
        ohm_window = Window("Calculator ohm", "500x220", "ohm.ico")
        ohm_gui = OhmGUI(ohm_window)
        ohm_window.run()
    
    def open_power_gui(self):
        power_window = Window("Calculator general", "500x720","energie.ico" )
        power_gui = PowerGUI(power_window)
        power_window.run()


if __name__ == '__main__':
    main_window = Window("Interfata principala", "500x220", "calculator.ico")
    main_gui = MainGUI(main_window)
    main_window.run()
