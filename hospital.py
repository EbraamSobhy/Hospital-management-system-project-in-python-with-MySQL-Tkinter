from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBrith = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="+ HOSPITAL MANAGEMENT SYSTEM", fg="red",
                bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                        font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                        font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=480, height=350)

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)

        lblNameTable = Label(DataFrameLeft, text="Name OF Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTable.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets, state="readonly", font=("times new roman", 12, "bold"),
                        width=37)
        comNametablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=0, column=1)
        comNametablet.current(0)

        lblref = Label(DataFrameLeft, text="Reference No:", font=("arial", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ref)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, text="Dose:", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataFrameLeft, text="No of Tablets:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.NumberofTablets)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, text="Lot:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataFrameLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Issuedate)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, text="Exp Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ExpDate)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.DailyDose)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, text="Side Effect:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.SideEffect)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataFrameLeft, text="Further Information:", font=("arial", 12, "bold"), padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.FurtherInformation)
        txtFurtherinfo.grid(row=0, column=3)

        lblStorage = Label(DataFrameLeft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.StorageAdvice)
        txtStorage.grid(row=2, column=3)

        lblPatientId = Label(DataFrameLeft, text="Patient ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientId)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, text="NHS Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.nhsNumber)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataFrameLeft, text="Patient Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientName)
        txtPatientname.grid(row=6, column=3)

        lblDateOfBrith = Label(DataFrameLeft, text="Date of Birth:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOfBrith.grid(row=7, column=2, sticky=W)
        txtDateOfBrith = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DateOfBrith)
        txtDateOfBrith.grid(row=7, column=3)

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=8, column=3)

        lblDrivingAdvice = Label(DataFrameRight, text="Driving/Using Machines:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDrivingAdvice.grid(row=0, column=0, sticky=W)
        txtDrivingAdvice = Entry(DataFrameRight, font=("arial", 12, "bold"), width=25, textvariable=self.DrivingUsingMachine)
        txtDrivingAdvice.grid(row=0, column=1)

        lblHowToUseMedication = Label(DataFrameRight, text="How to Use Medication:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblHowToUseMedication.grid(row=1, column=0, sticky=W)
        txtHowToUseMedication = Entry(DataFrameRight, font=("arial", 12, "bold"), width=25, textvariable=self.HowToUseMedication)
        txtHowToUseMedication.grid(row=1, column=1)

        # Add Buttons
        btnAdd = Button(ButtonFrame, text="Add Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=35, command=self.add_prescription)
        btnAdd.grid(row=0, column=0, padx=10)

        btnDisplay = Button(ButtonFrame, text="Display", bg="green", fg="white", font=("arial", 12, "bold"), width=35, command=self.display_data)
        btnDisplay.grid(row=0, column=1, padx=10)

        btnClear = Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=35, command=self.clear_fields)
        btnClear.grid(row=0, column=2, padx=10)

        btnExit = Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=32, command=self.exit_app)
        btnExit.grid(row=0, column=3, padx=10)

        # Treeview for displaying data
        SCROLL_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        SCROLL_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("Name", "Ref", "Dose", "NoOfTablets", "Lot", "IssueDate", "ExpDate", "DailyDose", "SideEffect", "FurtherInfo", "StorageAdvice", "PatientID", "NHSNumber", "PatientName", "DOB", "PatientAddress", "DrivingAdvice", "HowToUseMedication"), show="headings")
        SCROLL_x.pack(side=BOTTOM, fill=X)
        SCROLL_y.pack(side=RIGHT, fill=Y)
        
        SCROLL_x = ttk.Scrollbar(command=self.hospital_table.xview)
        SCROLL_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Name", text="Name")
        self.hospital_table.heading("Ref", text="Ref")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOfTablets", text="No Of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Exp Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("FurtherInfo", text="Further Information")
        self.hospital_table.heading("StorageAdvice", text="Storage Advice")
        self.hospital_table.heading("PatientID", text="Patient ID")
        self.hospital_table.heading("NHSNumber", text="NHS Number")
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("DOB", text="Date of Birth")
        self.hospital_table.heading("PatientAddress", text="Patient Address")
        self.hospital_table.heading("DrivingAdvice", text="Driving/Using Machines")
        self.hospital_table.heading("HowToUseMedication", text="How to Use Medication")

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.connect_db()

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sy5gGg3UJomPeF",
                database="my_data"
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

    def add_prescription(self):
        try:
            sql = """INSERT INTO prescriptions (Nameoftablets, ref, Dose, NumberofTablets, Lot, Issuedate, ExpDate, DailyDose, SideEffect, FurtherInformation, StorageAdvice, DrivingUsingMachine, HowToUseMedication, PatientId, nhsNumber, PatientName, DateOfBrith, PatientAddress)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(), self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(), self.SideEffect.get(), self.FurtherInformation.get(), self.StorageAdvice.get(), self.DrivingUsingMachine.get(), self.HowToUseMedication.get(), self.PatientId.get(), self.nhsNumber.get(), self.PatientName.get(), self.DateOfBrith.get(), self.PatientAddress.get())

            self.cursor.execute(sql, values)
            self.conn.commit()
            self.display_data()
            messagebox.showinfo("Success", "Prescription added successfully!")
        except Error as e:
            messagebox.showerror("Database Error", f"Error adding prescription: {e}")

    def display_data(self):
        self.hospital_table.delete(*self.hospital_table.get_children())
        try:
            self.cursor.execute("SELECT * FROM prescriptions")
            rows = self.cursor.fetchall()
            for row in rows:
                self.hospital_table.insert("", END, values=row)
        except Error as e:
            messagebox.showerror("Database Error", f"Error retrieving data: {e}")

    def clear_fields(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBrith.set("")
        self.PatientAddress.set("")

    def exit_app(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
