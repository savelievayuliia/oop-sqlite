import tkinter
import sqlite3
import tkinter.messagebox
import csv


def get_vehicles_from_db_to_csv(vehicle):
    vehicles_list = []
    conn = sqlite3.connect("yuliia_final_project/Vehicles_python.db")
    cursor = conn.cursor()
    cursor.execute(f"select * from {vehicle}")
    result_list = cursor.fetchall()
    with open("vehicles.csv", "w") as file:
        writer = csv.writer(file)
        for result in result_list:
            vehicles_list.append(result)
            writer.writerows(vehicles_list)

        conn.close()


def insert_plane_into_database(icao, country, registration, operator, model, passengers):
    conn = sqlite3.connect("yuliia_final_project/Vehicles_python.db")
    cursor = conn.cursor()
    sql_insert_code = f"INSERT INTO plain VALUES ('{icao}','{country}','{registration}','{operator}','{model}','{passengers}')"
    cursor.execute(sql_insert_code)
    conn.commit()
    conn.close()


def insert_car_into_database(id, year, brand, model, msrp, msrp_currency):
    conn = sqlite3.connect("yuliia_final_project/Vehicles_python.db")
    cursor = conn.cursor()
    sql_insert_code = f"INSERT INTO cars VALUES ('{id}','{year}','{brand}','{model}','{msrp}','{msrp_currency}')"
    cursor.execute(sql_insert_code)
    conn.commit()
    conn.close()


def insert_ship_into_database(imo, flag, vessel, destination_port, current_port, vessel_type, latitude, longtitude):
    conn = sqlite3.connect("yuliia_final_project/Vehicles_python.db")
    cursor = conn.cursor()
    sql_insert_code = f"INSERT INTO ships VALUES ('{imo}','{flag}','{vessel}','{destination_port}','{current_port}','{vessel_type}','{latitude}','{longtitude}')"
    cursor.execute(sql_insert_code)
    conn.commit()
    conn.close()


# styles
PROGRAM_FONT = ("Verdana", 10)
WINDOW_BG = '#344955'
BUTTON_BG = '#F9AA33'
BUTTON_FG = '#344955'
TEXT_FG = '#FFFBE6'
RB_SELECTCOLOR = '#356859'
BUTTON_PADX = 30


class VehiclesGUIv2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Welcome to the database editing mode")
        self.main_window.geometry("600x300+10+20")
        self.main_window.configure(bg=WINDOW_BG)
        self.choose_option_frame = tkinter.Frame(self.main_window)
        self.choose_option_frame.configure(bg=WINDOW_BG)
        self.radio_button_frame = tkinter.Frame(self.main_window)
        self.radio_button_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.main_window)
        self.buttons_frames.configure(bg=WINDOW_BG)
        self.what_do_you_want_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                    font=PROGRAM_FONT,
                                                    text="Choose one of the editing option below")

        # radiobuttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.radio_button_frame, text="Add new vehicle", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.radio_button_frame, text="Modify vehicle's data", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.radio_button_frame, text="Export data to csv file", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var,
                                       value=3)

        self.ok_button = tkinter.Button(self.buttons_frames, text="OK", bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                        padx=BUTTON_PADX,
                                        command=self.editing_mode)
        self.exit_button = tkinter.Button(self.buttons_frames, text="Exit", fg=BUTTON_FG, bg=BUTTON_BG,
                                          font=PROGRAM_FONT,
                                          padx=BUTTON_PADX,
                                          command=self.main_window.destroy)

        # packing
        self.choose_option_frame.pack()
        self.radio_button_frame.pack()
        self.buttons_frames.pack()
        self.what_do_you_want_label.pack(side="left")
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")

        tkinter.mainloop()

    def editing_mode(self):
        if self.radio_var.get() == 1:
            self.main_window.destroy()
            self.editing_mode = AddNewVehicle()

        if self.radio_var.get() == 2:
            self.main_window.destroy()
            self.editing_mode = ChangeVehicleData()

        if self.radio_var.get() == 3:
            self.main_window.destroy()
            self.editing_mode = ExportDataToCsv()


class AddNewVehicle:
    def __init__(self):
        self.adding_window = tkinter.Tk()
        self.adding_window.geometry("600x300+10+20")
        self.adding_window.configure(bg=WINDOW_BG)
        self.adding_window.title("Add new vehicle to database")
        self.choose_label_frame = tkinter.Frame(self.adding_window)
        self.choose_label_frame.configure(bg=WINDOW_BG)
        self.radio_button_frame = tkinter.Frame(self.adding_window)
        self.radio_button_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.adding_window)
        self.buttons_frames.configure(bg=WINDOW_BG)
        self.vehicles_fields = tkinter.Frame(self.adding_window)
        self.vehicles_fields.configure(bg=WINDOW_BG)

        self.choose_vehicle_type = tkinter.Label(self.choose_label_frame, text="Choose vehicle type", bg=WINDOW_BG,
                                                 fg=TEXT_FG, font=PROGRAM_FONT)

        # radiobuttons
        self.choice_var = tkinter.IntVar()
        self.choice_var.set(1)
        self.choice_1 = tkinter.Radiobutton(self.radio_button_frame, text="Plane", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var,
                                            value=1)
        self.choice_2 = tkinter.Radiobutton(self.radio_button_frame, text="Car", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var, value=2)
        self.choice_3 = tkinter.Radiobutton(self.radio_button_frame, text="Ship", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var,
                                            value=3)

        self.ok_button = tkinter.Button(self.buttons_frames, text="Ok", bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                        padx=BUTTON_PADX,
                                        command=self.new_vehicles_data_fields)
        self.exit_button = tkinter.Button(self.buttons_frames, text="Exit", bg=BUTTON_BG, fg=BUTTON_FG,
                                          font=PROGRAM_FONT,
                                          padx=BUTTON_PADX,
                                          command=self.adding_window.destroy)

        # packing
        self.choose_label_frame.pack()
        self.radio_button_frame.pack()
        self.buttons_frames.pack()
        self.choose_vehicle_type.pack(side="left")
        self.choice_1.pack()
        self.choice_2.pack()
        self.choice_3.pack()
        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")
        self.vehicles_fields.pack()

        tkinter.mainloop()

    def new_vehicles_data_fields(self):
        if self.choice_var.get() == 1:
            self.adding_window.destroy()
            self.editing_mode = AddPlaneToDatabase()
        if self.choice_var.get() == 2:
            self.adding_window.destroy()
            self.editing_mode = AddCarToDatabase()
        if self.choice_var.get() == 3:
            self.adding_window.destroy()
            self.editing_mode = AddShipToDatabase()


class AddPlaneToDatabase:
    def __init__(self):
        self.plane_table_window = tkinter.Tk()
        self.plane_table_window.geometry("600x600+10+20")
        self.plane_table_window.configure(bg=WINDOW_BG)
        self.plane_table_window.title("Adding new plane to the database")
        self.entry_frame = tkinter.Frame(self.plane_table_window)
        self.entry_frame.configure(bg=WINDOW_BG)
        self.add_more_button_frame = tkinter.Frame(self.plane_table_window)
        self.add_more_button_frame.configure(bg=WINDOW_BG)

        self.icao_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, text="ICAO24 code")
        self.icao_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, width="10")
        self.country_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                           font=PROGRAM_FONT, text="Country")
        self.country_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                           font=PROGRAM_FONT, width="10")
        self.registration_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT, text="Registration")
        self.registration_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT, width="10")
        self.operator_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                            font=PROGRAM_FONT, text="Operator")
        self.operator_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                            font=PROGRAM_FONT, width="10")
        self.model_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, text="Model")
        self.model_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, width="10")
        self.passengers_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                              font=PROGRAM_FONT, text="Passengers")
        self.passengers_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                              font=PROGRAM_FONT, width="10")

        self.clear_button = tkinter.Button(self.add_more_button_frame, text="Add more", bg=BUTTON_BG, fg=BUTTON_FG,
                                           font=PROGRAM_FONT,
                                           padx=BUTTON_PADX, command=self.adding_text)
        self.finished_button = tkinter.Button(self.add_more_button_frame, text="Save and exit", bg=BUTTON_BG,
                                              fg=BUTTON_FG, font=PROGRAM_FONT,
                                              padx=BUTTON_PADX,
                                              command=self.save_and_exit)

        self.icao_label.pack()
        self.icao_entry.pack()
        self.country_label.pack()
        self.country_entry.pack()
        self.registration_label.pack()
        self.registration_entry.pack()
        self.operator_label.pack()
        self.operator_entry.pack()
        self.model_label.pack()
        self.model_entry.pack()
        self.passengers_label.pack()
        self.passengers_entry.pack()

        self.clear_button.pack(side="left")
        self.finished_button.pack(side="left")

        self.entry_frame.pack()
        self.add_more_button_frame.pack()

        tkinter.mainloop()

    def adding_text(self):
        icao = self.icao_entry.get()
        country = self.country_entry.get()
        registration = self.registration_entry.get()
        operator = self.operator_entry.get()
        model = self.model_entry.get()
        passengers = self.passengers_entry.get()

        insert_plane_into_database(icao, country, registration, operator, model, passengers)

        self.icao_entry.delete(0, 'end')
        self.country_entry.delete(0, 'end')
        self.registration_entry.delete(0, 'end')
        self.operator_entry.delete(0, 'end')
        self.model_entry.delete(0, 'end')
        self.passengers_entry.delete(0, 'end')

    def save_and_exit(self):
        icao = self.icao_entry.get()
        country = self.country_entry.get()
        registration = self.registration_entry.get()
        operator = self.operator_entry.get()
        model = self.model_entry.get()
        passengers = self.passengers_entry.get()

        insert_plane_into_database(icao, country, registration, operator, model, passengers)

        are_you_sure = tkinter.messagebox.askyesno(title="Exit", message="Are you sure you want to exit the program?")
        if are_you_sure is True:

            self.icao_entry.delete(0, 'end')
            self.country_entry.delete(0, 'end')
            self.registration_entry.delete(0, 'end')
            self.operator_entry.delete(0, 'end')
            self.model_entry.delete(0, 'end')
            self.passengers_entry.delete(0, 'end')

            tkinter.messagebox.showinfo(title="Exit", message="Your data was saved.")
            self.plane_table_window.destroy()

        else:
            self.icao_entry.delete(0, 'end')
            self.country_entry.delete(0, 'end')
            self.registration_entry.delete(0, 'end')
            self.operator_entry.delete(0, 'end')
            self.model_entry.delete(0, 'end')
            self.passengers_entry.delete(0, 'end')

            icao = self.icao_entry.get()
            country = self.country_entry.get()
            registration = self.registration_entry.get()
            operator = self.operator_entry.get()
            model = self.model_entry.get()
            passengers = self.passengers_entry.get()

            insert_plane_into_database(icao, country, registration, operator, model, passengers)


class AddCarToDatabase:
    def __init__(self):
        self.car_table_window = tkinter.Tk()
        self.car_table_window.geometry("600x600+10+20")
        self.car_table_window.title("Adding new car to the database")
        self.car_table_window.configure(bg=WINDOW_BG)

        self.entry_frame = tkinter.Frame(self.car_table_window)
        self.entry_frame.configure(bg=WINDOW_BG)
        self.add_more_button_frame = tkinter.Frame(self.car_table_window)
        self.add_more_button_frame.configure(bg=WINDOW_BG)

        self.id_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Car ID")
        self.id_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, width="10")
        self.year_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, text="Year")
        self.year_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, width="10")
        self.brand_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, text="Brand")
        self.brand_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, width="10")
        self.model_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, text="Model")
        self.model_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                         font=PROGRAM_FONT, width="10")
        self.msrp_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, text="Starting MSRP")
        self.msrp_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, width="10")
        self.msrp_currency_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, text="Starting MSRP currency")
        self.msrp_currency_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, width="10")

        self.clear_button = tkinter.Button(self.add_more_button_frame, text="Add more", bg=BUTTON_BG, fg=BUTTON_FG,
                                           font=PROGRAM_FONT,
                                           padx=BUTTON_PADX, command=self.adding_text)
        self.finished_button = tkinter.Button(self.add_more_button_frame, text="Save and exit", bg=BUTTON_BG,
                                              fg=BUTTON_FG, font=PROGRAM_FONT,
                                              padx=BUTTON_PADX,
                                              command=self.save_and_exit)

        self.id_label.pack()
        self.id_entry.pack()
        self.year_label.pack()
        self.year_entry.pack()
        self.brand_label.pack()
        self.brand_entry.pack()
        self.model_label.pack()
        self.model_entry.pack()
        self.msrp_label.pack()
        self.msrp_entry.pack()
        self.msrp_currency_label.pack()
        self.msrp_currency_entry.pack()

        self.clear_button.pack(side="left")
        self.finished_button.pack(side="left")

        self.entry_frame.pack()
        self.add_more_button_frame.pack()

        tkinter.mainloop()

    def adding_text(self):
        id = self.id_entry.get()
        year = self.year_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        msrp = self.msrp_entry.get()
        msrp_currency = self.msrp_currency_entry.get()

        insert_car_into_database(id, year, brand, model, msrp, msrp_currency)

        self.id_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.brand_entry.delete(0, 'end')
        self.model_entry.delete(0, 'end')
        self.msrp_entry.delete(0, 'end')
        self.msrp_currency_entry.delete(0, 'end')

    def save_and_exit(self):
        id = self.id_entry.get()
        year = self.year_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        msrp = self.msrp_entry.get()
        msrp_currency = self.msrp_currency_entry.get()

        insert_car_into_database(id, year, brand, model, msrp, msrp_currency)

        are_you_sure = tkinter.messagebox.askyesno(title="Exit", message="Are you sure you want to exit the program?")

        if are_you_sure is True:

            self.id_entry.delete(0, 'end')
            self.year_entry.delete(0, 'end')
            self.brand_entry.delete(0, 'end')
            self.model_entry.delete(0, 'end')
            self.msrp_entry.delete(0, 'end')
            self.msrp_currency_entry.delete(0, 'end')

            tkinter.messagebox.showinfo(title="Exit", message="Your data was saved.")
            self.car_table_window.destroy()

        else:
            self.id_entry.delete(0, 'end')
            self.year_entry.delete(0, 'end')
            self.brand_entry.delete(0, 'end')
            self.model_entry.delete(0, 'end')
            self.msrp_entry.delete(0, 'end')
            self.msrp_currency_entry.delete(0, 'end')

            id = self.id_entry.get()
            year = self.year_entry.get()
            brand = self.brand_entry.get()
            model = self.model_entry.get()
            msrp = self.msrp_entry.get()
            msrp_currency = self.msrp_currency_entry.get()

            insert_car_into_database(id, year, brand, model, msrp, msrp_currency)


class AddShipToDatabase:
    def __init__(self):
        self.ship_table_window = tkinter.Tk()
        self.ship_table_window.geometry("600x600+10+20")
        self.ship_table_window.title("Adding new ship to the database")
        self.ship_table_window.configure(bg=WINDOW_BG)

        self.entry_frame = tkinter.Frame(self.ship_table_window)
        self.entry_frame.configure(bg=WINDOW_BG)
        self.add_more_button_frame = tkinter.Frame(self.ship_table_window)
        self.add_more_button_frame.configure(bg=WINDOW_BG)

        self.imo_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, text="Vessel IMO")
        self.imo_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width="10")
        self.flag_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, text="Flag")
        self.flag_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                        font=PROGRAM_FONT, width="10")
        self.vessel_name_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                               font=PROGRAM_FONT, text="Vessel Name")
        self.vessel_name_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                               font=PROGRAM_FONT, width="10")
        self.destination_port_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                    font=PROGRAM_FONT, text="Destination Port")
        self.destination_port_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                    font=PROGRAM_FONT, width="10")
        self.current_port_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT, text="Current Port")
        self.current_port_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT, width="10")
        self.vessel_type_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                               font=PROGRAM_FONT, text="Vessel Type")
        self.vessel_type_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                               font=PROGRAM_FONT, width="10")
        self.latitude_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                            font=PROGRAM_FONT, text="Latitude")
        self.latitude_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                            font=PROGRAM_FONT, width="10")
        self.longtitude_label = tkinter.Label(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                              font=PROGRAM_FONT, text="Longitude")
        self.longtitude_entry = tkinter.Entry(self.entry_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                              font=PROGRAM_FONT, width="10")

        self.clear_button = tkinter.Button(self.add_more_button_frame, text="Add more", bg=BUTTON_BG, fg=BUTTON_FG,
                                           font=PROGRAM_FONT,
                                           padx=BUTTON_PADX, command=self.adding_text)
        self.finished_button = tkinter.Button(self.add_more_button_frame, text="Save and exit", bg=BUTTON_BG,
                                              fg=BUTTON_FG, font=PROGRAM_FONT,
                                              padx=BUTTON_PADX,
                                              command=self.save_and_exit)

        self.imo_label.pack()
        self.imo_entry.pack()
        self.flag_label.pack()
        self.flag_entry.pack()
        self.vessel_name_label.pack()
        self.vessel_name_entry.pack()
        self.destination_port_label.pack()
        self.destination_port_entry.pack()
        self.current_port_label.pack()
        self.current_port_entry.pack()
        self.vessel_type_label.pack()
        self.vessel_type_entry.pack()
        self.latitude_label.pack()
        self.latitude_entry.pack()
        self.longtitude_label.pack()
        self.longtitude_entry.pack()

        self.clear_button.pack(side="left")
        self.finished_button.pack(side="left")

        self.entry_frame.pack()
        self.add_more_button_frame.pack()

        tkinter.mainloop()

    def adding_text(self):

        imo = self.imo_entry.get()
        flag = self.flag_entry.get()
        vessel = self.vessel_name_entry.get()
        destination_port = self.destination_port_entry.get()
        current_port = self.current_port_entry.get()
        vessel_type = self.vessel_type_entry.get()
        latitude = self.latitude_entry.get()
        longtitude = self.longtitude_entry.get()

        insert_ship_into_database(imo, flag, vessel, destination_port, current_port, vessel_type, latitude, longtitude)

        self.imo_entry.delete(0, 'end')
        self.flag_entry.delete(0, 'end')
        self.vessel_name_entry.delete(0, 'end')
        self.destination_port_entry.delete(0, 'end')
        self.current_port_entry.delete(0, 'end')
        self.vessel_type_entry.delete(0, 'end')
        self.latitude_entry.delete(0, 'end')
        self.longtitude_entry.delete(0, 'end')

    def save_and_exit(self):

        imo = self.imo_entry.get()
        flag = self.flag_entry.get()
        vessel = self.vessel_name_entry.get()
        destination_port = self.destination_port_entry.get()
        current_port = self.current_port_entry.get()
        vessel_type = self.vessel_type_entry.get()
        latitude = self.latitude_entry.get()
        longtitude = self.longtitude_entry.get()

        insert_ship_into_database(imo, flag, vessel, destination_port, current_port, vessel_type, latitude, longtitude)

        are_you_sure = tkinter.messagebox.askyesno(title="Exit", message="Are you sure you want to exit the program?")

        if are_you_sure is True:

            tkinter.messagebox.showinfo(title="Exit", message="Your data was saved.")
            self.ship_table_window.destroy()

        else:
            self.imo_entry.delete(0, 'end')
            self.flag_entry.delete(0, 'end')
            self.vessel_name_entry.delete(0, 'end')
            self.destination_port_entry.delete(0, 'end')
            self.current_port_entry.delete(0, 'end')
            self.vessel_type_entry.delete(0, 'end')
            self.latitude_entry.delete(0, 'end')
            self.longtitude_entry.delete(0, 'end')

            imo = self.imo_entry.get()
            flag = self.flag_entry.get()
            vessel = self.vessel_name_entry.get()
            destination_port = self.destination_port_entry.get()
            current_port = self.current_port_entry.get()
            vessel_type = self.vessel_type_entry.get()
            latitude = self.latitude_entry.get()
            longtitude = self.longtitude_entry.get()

            insert_ship_into_database(imo, flag, vessel, destination_port, current_port, vessel_type, latitude,
                                      longtitude)


class ChangeVehicleData:
    def __init__(self):
        self.change_vehicle_window = tkinter.Tk()
        self.change_vehicle_window.title("Update vehicles data")
        self.change_vehicle_window.geometry("600x300+10+20")
        self.change_vehicle_window.configure(bg=WINDOW_BG)
        self.choose_option_frame = tkinter.Frame(self.change_vehicle_window)
        self.choose_option_frame.configure(bg=WINDOW_BG)
        self.radio_button_frame = tkinter.Frame(self.change_vehicle_window)
        self.radio_button_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.change_vehicle_window)
        self.buttons_frames.configure(bg=WINDOW_BG)

        self.what_do_you_want_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                    font=PROGRAM_FONT,
                                                    text="Choose vehicles you want to edit")

        # radiobuttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.radio_button_frame, text="Plane", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.radio_button_frame, text="Car", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.radio_button_frame, text="Ship", bg=WINDOW_BG,
                                       font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                       variable=self.radio_var,
                                       value=3)

        self.ok_button = tkinter.Button(self.buttons_frames, text="Ok", bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                        padx=BUTTON_PADX, command=self.editing_mode)
        self.exit_button = tkinter.Button(self.buttons_frames, text="Exit", bg=BUTTON_BG, fg=BUTTON_FG,
                                          font=PROGRAM_FONT,
                                          padx=BUTTON_PADX, command=self.change_vehicle_window.destroy)

        # packing
        self.choose_option_frame.pack()
        self.radio_button_frame.pack()
        self.buttons_frames.pack()
        self.what_do_you_want_label.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")

        tkinter.mainloop()

    def editing_mode(self):
        if self.radio_var.get() == 1:
            self.change_vehicle_window.destroy()
            self.editing_mode = EditPlaneData()

        if self.radio_var.get() == 2:
            self.change_vehicle_window.destroy()
            self.editing_mode = EditCarData()

        if self.radio_var.get() == 3:
            self.change_vehicle_window.destroy()
            self.editing_mode = EditShipData()


class EditPlaneData:
    def __init__(self):
        self.edit_plane_window = tkinter.Tk()
        self.edit_plane_window.title("Edit planes data")
        self.edit_plane_window.geometry("600x300+10+20")
        self.edit_plane_window.configure(bg=WINDOW_BG)
        self.choose_option_frame = tkinter.Frame(self.edit_plane_window)
        self.choose_option_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.edit_plane_window)
        self.buttons_frames.configure(bg=WINDOW_BG)

        self.choose_option_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, text="What parameter to update?")
        self.choose_option_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, width=20)
        self.old_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Value")
        self.old_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.new_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Replace with")
        self.new_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.list_options_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT,
                                                text=f"Available parameters:\nICAO24\nCountry\nRegistration\nOperator"
                                                     "\nModel\nPassengers")

        self.ok_button = tkinter.Button(self.buttons_frames, bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                        padx=BUTTON_PADX, text="Commit changes", command=self.editing_mode)
        self.exit_button = tkinter.Button(self.buttons_frames, bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                          padx=BUTTON_PADX, text="Exit", command=self.edit_plane_window.destroy)

        # packing

        self.choose_option_frame.pack()
        self.buttons_frames.pack()
        self.choose_option_label.pack()
        self.choose_option_entry.pack()
        self.old_data.pack()
        self.old_entry.pack()
        self.new_data.pack()
        self.new_entry.pack()

        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")
        self.list_options_label.pack()

        tkinter.mainloop()

    def editing_mode(self):
        parameter = self.choose_option_entry.get()
        old_data = self.old_entry.get()
        new_data = self.new_entry.get()
        with sqlite3.connect("yuliia_final_project/Vehicles_python.db") as conn:
            cursor = conn.cursor()
            if parameter == "ICAO24":
                sql_update = "update plain set ICAO24 = :s_name_change where ICAO24 = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Country":
                sql_update = "update plain set Country = :s_name_change where Country = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Registration":
                sql_update = "update plain set Registration = :s_name_change where Registration = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Operator":
                sql_update = "update plain set Operator = :s_name_change where Operator = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Model":
                sql_update = "update plain set Model = :s_name_change where Model = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Passengers":
                sql_update = "update plain set Passengers = :s_name_change where Passengers = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            else:
                tkinter.messagebox.showinfo(title="Warning", message="The parameter you have entered doesn't exist")
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
                self.edit_plane_window.destroy()
                self.__init__()


class EditCarData:
    def __init__(self):
        self.edit_car_window = tkinter.Tk()
        self.edit_car_window.title("Edit cars data")
        self.edit_car_window.geometry("600x300+10+20")
        self.edit_car_window.configure(bg=WINDOW_BG)
        self.choose_option_frame = tkinter.Frame(self.edit_car_window)
        self.choose_option_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.edit_car_window)
        self.buttons_frames.configure(bg=WINDOW_BG)

        self.choose_option_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, text="What parameter to update?")
        self.choose_option_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, width=20)
        self.old_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Value")
        self.old_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.new_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Replace with")
        self.new_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.list_options_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT,
                                                text=f"Available parameters:\nID\nYear\nBrand\nModel"
                                                     "\nStartingMSRP\nCurrencyforMSRP")

        self.ok_button = tkinter.Button(self.buttons_frames, bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                        padx=BUTTON_PADX, text="Commit changes", command=self.editing_mode)
        self.exit_button = tkinter.Button(self.buttons_frames, bg=BUTTON_BG, fg=BUTTON_FG, font=PROGRAM_FONT,
                                          padx=BUTTON_PADX, text="Exit", command=self.edit_car_window.destroy)

        # packing

        self.choose_option_frame.pack()
        self.buttons_frames.pack()
        self.choose_option_label.pack()
        self.choose_option_entry.pack()
        self.old_data.pack()
        self.old_entry.pack()
        self.new_data.pack()
        self.new_entry.pack()

        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")
        self.list_options_label.pack()

        tkinter.mainloop()

    def editing_mode(self):
        parameter = self.choose_option_entry.get()
        old_data = self.old_entry.get()
        new_data = self.new_entry.get()
        with sqlite3.connect("yuliia_final_project/Vehicles_python.db") as conn:
            cursor = conn.cursor()
            if parameter == "ID":
                sql_update = "update cars set ID = :s_name_change where ID = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Year":
                sql_update = "update cars set Year = :s_name_change where Year = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Brand":
                sql_update = "update cars set Brand = :s_name_change where Brand = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Model":
                sql_update = "update cars set Model = :s_name_change where Model = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "StartingMSRP":
                sql_update = "update cars set Model = :s_name_change where Model = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "CurrencyforMSRP":
                sql_update = "update cars set Passengers = :s_name_change where Passengers = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            else:
                tkinter.messagebox.showinfo(title="Warning", message="The parameter you have entered doesn't exist")
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
                self.edit_car_window.destroy()
                self.__init__()


class EditShipData:
    def __init__(self):
        self.edit_ship_window = tkinter.Tk()
        self.edit_ship_window.title("Edit ships data")
        self.edit_ship_window.geometry("600x300+10+20")
        self.edit_ship_window.configure(bg=WINDOW_BG)
        self.choose_option_frame = tkinter.Frame(self.edit_ship_window)
        self.choose_option_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.edit_ship_window)
        self.buttons_frames.configure(bg=WINDOW_BG)

        self.choose_option_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, text="What parameter to update?")
        self.choose_option_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, width=20)
        self.old_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Value")
        self.old_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.new_data = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                      font=PROGRAM_FONT, text="Replace with")
        self.new_entry = tkinter.Entry(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                       font=PROGRAM_FONT, width=20)
        self.list_options_label = tkinter.Label(self.choose_option_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                font=PROGRAM_FONT,
                                                text=f"Available parameters:\nIMO\nFlag\nVesselName\nDestinationPort"
                                                     "\nCurrentPort\nVesselType-Generic\nLatitude\nLongitude")

        self.ok_button = tkinter.Button(self.buttons_frames, text="Commit", bg=BUTTON_BG, fg=BUTTON_FG,
                                        font=PROGRAM_FONT,
                                        padx=BUTTON_PADX, command=self.editing_mode)
        self.exit_button = tkinter.Button(self.buttons_frames, text="Exit", bg=BUTTON_BG, fg=BUTTON_FG,
                                          font=PROGRAM_FONT,
                                          padx=BUTTON_PADX, command=self.edit_ship_window.destroy)

        # packing

        self.choose_option_frame.pack()
        self.buttons_frames.pack()
        self.choose_option_label.pack()
        self.choose_option_entry.pack()
        self.old_data.pack()
        self.old_entry.pack()
        self.new_data.pack()
        self.new_entry.pack()

        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")
        self.list_options_label.pack()

        tkinter.mainloop()


    def editing_mode(self):
        parameter = self.choose_option_entry.get()
        old_data = self.old_entry.get()
        new_data = self.new_entry.get()
        with sqlite3.connect("yuliia_final_project/Vehicles_python.db") as conn:
            cursor = conn.cursor()
            if parameter == "IMO":
                sql_update = "update ships set IMO = :s_name_change where IMO = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Flag":
                sql_update = "update ships set Flag = :s_name_change where Flag = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "VesselName":
                sql_update = "update ships set VesselName = :s_name_change where VesselName = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "DestinationPort":
                sql_update = "update ships set DestinationPort = :s_name_change where DestinationPort = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "CurrentPort":
                sql_update = "update ships set CurrentPort = :s_name_change where CurrentPort = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "VesselType-Generic":
                sql_update = "update ships set VesselType-Generic = :s_name_change where VesselType-Generic = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')

            elif parameter == "Latitude":
                sql_update = "update ships set Latitude = :s_name_change where Latitude = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            elif parameter == "Longitude":
                sql_update = "update ships set Longitude = :s_name_change where Longitude = :s_name"
                cursor.execute(sql_update, {
                    "s_name": f'{old_data}',
                    "s_name_change": f'{new_data}'
                })
                conn.commit()
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
            else:
                tkinter.messagebox.showinfo(title="Warning", message="The parameter you have entered doesn't exist")
                self.choose_option_entry.delete(0, 'end')
                self.old_entry.delete(0, 'end')
                self.new_entry.delete(0, 'end')
                self.edit_ship_window.destroy()
                self.__init__()


class ExportDataToCsv:
    def __init__(self):
        self.export_data_window = tkinter.Tk()
        self.export_data_window.geometry("600x300+10+20")
        self.export_data_window.title("Add new vehicle to database")
        self.export_data_window.configure(bg=WINDOW_BG)
        self.choose_label_frame = tkinter.Frame(self.export_data_window)
        self.choose_label_frame.configure(bg=WINDOW_BG)
        self.radio_button_frame = tkinter.Frame(self.export_data_window)
        self.radio_button_frame.configure(bg=WINDOW_BG)
        self.buttons_frames = tkinter.Frame(self.export_data_window)
        self.buttons_frames.configure(bg=WINDOW_BG)

        self.choose_vehicle_type = tkinter.Label(self.choose_label_frame, bg=WINDOW_BG, fg=TEXT_FG,
                                                 font=PROGRAM_FONT, text="Choose table to export")

        # radiobuttons
        self.choice_var = tkinter.IntVar()
        self.choice_var.set(1)
        self.choice_1 = tkinter.Radiobutton(self.radio_button_frame, text="Plane", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var,
                                            value=1)
        self.choice_2 = tkinter.Radiobutton(self.radio_button_frame, text="Car", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var, value=2)
        self.choice_3 = tkinter.Radiobutton(self.radio_button_frame, text="Ship", bg=WINDOW_BG,
                                            font=PROGRAM_FONT, fg=TEXT_FG, selectcolor=RB_SELECTCOLOR,
                                            variable=self.choice_var,
                                            value=3)

        self.ok_button = tkinter.Button(self.buttons_frames, text="Export data", bg=BUTTON_BG, fg=BUTTON_FG,
                                        font=PROGRAM_FONT,
                                        padx=BUTTON_PADX, command=self.export_command)
        self.exit_button = tkinter.Button(self.buttons_frames, text="Exit", bg=BUTTON_BG, fg=BUTTON_FG,
                                          font=PROGRAM_FONT,
                                          padx=BUTTON_PADX, command=self.export_data_window.destroy)

        # packing
        self.choose_label_frame.pack()
        self.radio_button_frame.pack()
        self.buttons_frames.pack()
        self.choose_vehicle_type.pack()
        self.choice_1.pack()
        self.choice_2.pack()
        self.choice_3.pack()
        self.ok_button.pack(side="left")
        self.exit_button.pack(side="left")

        tkinter.mainloop()

    def export_command(self):
        if self.choice_var.get() == 1:
            get_vehicles_from_db_to_csv("plain")
            tkinter.messagebox.showinfo(title="Success", message="Success! File was saved to the current location.")
            self.export_data_window.destroy()
        if self.choice_var.get() == 2:
            get_vehicles_from_db_to_csv("cars")
            tkinter.messagebox.showinfo(title="Success", message="Success! File was saved to the current location.")
            self.export_data_window.destroy()
        if self.choice_var.get() == 3:
            get_vehicles_from_db_to_csv("ships")
            tkinter.messagebox.showinfo(title="Success", message="Success! File was saved to the current location.")
            self.export_data_window.destroy()


program = VehiclesGUIv2()
