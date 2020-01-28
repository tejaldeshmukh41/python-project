from tkinter import*
import sqlite3
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime
from tkinter import messagebox
from tkinter.messagebox import showinfo


def main():
    root =Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()
        

        self.LabelTitle =Label(self.frame,text ='Pharmacy Management System',font=('arial',50,'bold'),bd=20,)                     
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=20)

        self.Loginframe1 = Frame(self.frame , width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        
        self.Loginframe2 = Frame(self.frame , width=1000, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        
        self.Loginframe3 = Frame(self.frame , width=1000, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0,pady=40)

        self.lblUsername =Label(self.Loginframe1,text='Username',font=('arial', 30, 'bold'), bd=22,)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername =Entry(self.Loginframe1, text ='Username',font=('arial', 30, 'bold'), bd=22,
                                textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword =Label(self.Loginframe1,text='Password',font=('arial', 30, 'bold'), bd=22,)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword =Entry(self.Loginframe1, text ='Password',font=('arial', 30, 'bold'), bd=22, show="*",
                                textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, padx=25)


        self.btnLogin = Button(self.Loginframe2, text="Login", width=20,font=('arial',20,'bold'),command =self.Login_System)
        self.btnLogin.grid(row = 0 ,column = 0)

        self.btnReset = Button(self.Loginframe2,text="Reset", width=20, font=('arial',20,'bold'),command =self.Reset)
        self.btnReset.grid(row = 0 ,column = 1)


        self.btnExit = Button(self.Loginframe2,text="Exit", width=20, font=('arial',20,'bold',), command =self.iExit)
        self.btnExit.grid(row = 0 ,column = 2)

        self.btnRegistration = Button(self.Loginframe3, text="Patient Registration ",                                      
                                  state = DISABLED, command =self.Registration_window, font=('arial',20,'bold'))
        self.btnRegistration.grid(row = 0 ,column = 0)

        self.btnHospital = Button(self.Loginframe3,text="Pharmacy Management ",
                              state = DISABLED, command =self.Hospital_window, font=('arial',20,'bold'))
        self.btnHospital.grid(row = 0 ,column =1)

        self.btnDoctor = Button(self.Loginframe3,text="Doctor Registration ",
                              state = DISABLED, command =self.Doctor_window, font=('arial',20,'bold'))
        self.btnDoctor.grid(row = 0 ,column =2)


    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user ==str(1234)) and (pas ==str(2345)):
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)
            self.btnDoctor.config(state = NORMAL)

        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid login details")
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return
            
                                              
    def Registration_window(self):
           self.newWindow = Toplevel(self.master)
           self.app = Window2(self.newWindow)

    def Hospital_window(self):
           self.newWindow = Toplevel(self.master)
           self.app = Window3(self.newWindow)

    def Doctor_window(self):
           self.newWindow = Toplevel(self.master)
           self.app = Window4(self.newWindow)



class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()                
        Postcode=StringVar()
        Telephone=StringVar()
        ReferenceNo=StringVar()
        Date=StringVar()

                                        
        Membership = StringVar()
        Membership.set("0")

        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Registration System", "Confirm if you want to exit")
            if iExit>0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")                
            Postcode.set("")
            Telephone.set("")
            ReferenceNo.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboMethod_of_Payment.current(0)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askyesno("Patient Registration System", "Confirm if you want to add a new\ record")
            if iResetRecord>0:
                Reset()
            elif iResetRecord <=0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return

        #def Ref_No():
            #x = random.randint(10903, 600873)
            #randomRef = str(x)
            #Ref.set(randomRef)
        def  database(*args):
            
            firstname=Firstname.get()
            surname=Surname.get()
            address=Address.get()
            postcode=Postcode.get()
            telephone=Telephone.get()
            date=DateofOrder.get()
            membership=Membership.get()
            reference=ReferenceNo.get()
            conn=sqlite3.connect("patient.db")
            with conn:
                cursor=conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS Patient(Firstname TEXT primary key,Surname TEXT,Address TEXT,Postcode INTEGER,Telephone NUMERIC,Membership text,ReferenceNo NUMERIC UNIQUE,DateofOrder DATE)")
                cursor.execute("INSERT INTO Patient(Firstname,Surname,Address, Postcode,Telephone,Membership,ReferenceNo,DateofOrder)VALUES(?,?,?,?,?,?,?,?)",(firstname,surname,address,postcode,telephone,membership,reference,date))
                
                conn.commit()
                showinfo( title = "Pateint registration", message = "Data inserted To table")
        def displaydata():
            conn=sqlite3.connect("patient.db")
            cursor=conn.cursor()
            cursor.execute("select * from Patient")
            row=cursor.fetchall()
            conn.close()
            return row
        def view_data():
            #Ref_no()
            for row in displaydata():
                
                self.patientlist.insert(END,"ReferenceNO=",row[6],
                                        "Firstname=",row[0],
                                        "Surname=",row[1] ,
                                        "Address=",row[2],
                                        "Postcode=",row[3],
                                        "Telephone=",row[4],
                                        "Date=",row[7],"",
                                        "Total Payment=",row[5],"\n")    
        
        def deletedata():
            reference=ReferenceNo.get()
            conn=sqlite3.connect("patient.db")
            cursor=conn.cursor()
            cursor.execute("DELETE FROM patient WHERE ReferenceNo=?",(reference,))
            conn.commit()
            showinfo( title = "Pateint registration", message = "Data deleted sucessfully")
            conn.close()
        
               
        
        def update():
            reference=ReferenceNo.get()
            firstname=Firstname.get()
            surname=Surname.get()
            address=Address.get()
            postcode=Postcode.get()
            telephone=Telephone.get()
            date=DateofOrder.get()
            membership=Membership.get()
            
            conn=sqlite3.connect("patient.db")
            cursor=conn.cursor()
            cursor.execute("UPDATE patient SET Firstname=?,Surname=?,Address=?,Postcode=?,Telephone=?,DateofOrder=?,Membership=? WHERE ReferenceNo=?",(firstname,surname,address,postcode,telephone,date,membership,reference))
            conn.commit()
            showinfo( title = "Pateint registration", message = "Data update sucessfully")
            conn.close
            
            
            
        
        def Receipt():
            #self.patientlist.insert(END,"\t" + ReferenceNo.get()+ "\t\t" +Firstname.get() + "\t\t" +Surname.get()+"\t\t"+Address.get() +"\t\t" +DateofOrder.get()+"\t\t" +Telephone.get() +"\t\t" +Membership.get() +"\n")
            self.patientlist.insert(END,"\t" "reference number="+ ReferenceNo.get()+ "\t""\n")
            self.patientlist.insert(END,"\t" "Firstname of patient="+ Firstname.get()+ "\t""\n")
            self.patientlist.insert(END,"\t" "Surname of patient="+ Surname.get()+ "\t""\n")  
            self.patientlist.insert(END,"\t" "Address="+ Address.get()+ "\t""\n")
            self.patientlist.insert(END,"\t" "Date of order="+ DateofOrder.get()+ "\t""\n")
            self.patientlist.insert(END,"\t" "total payement="+ ReferenceNo.get()+ "\t""\n")
            self.patientlist.insert(END,"\t" ".........................................Helth is welth.................................""\t\t""\n")
            
        def Membership_Fees():
            if(var4.get() ==1):
                self.txtMembership.configure(state = NORMAL)
                Item1 = float(50)
                Membership.set("Rs." +str(Item1))
            elif(var4.get() ==0):
                self.txtMembership.configure(state = DISABLED)
                Membership.set("0")

        Mainframe=Frame(self.frame)
        Mainframe.grid()
        TitleFrame=Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame,font=('arial',59,'bold'),text=" Patient Registration System ",padx=2)
        self.lblTitle.grid()

        MemberDetailsFrame = LabelFrame(Mainframe, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,font=('arial',12,'bold'),text ='Patient Name',relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame, bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        self.lblReferenceNo=Label(MembersName_F,font=('arial',14,'bold'),text=" Reference No ",bd=7)
        self.lblReferenceNo.grid(row=0 ,column=0, sticky=W)
        self.txtReferenceNo=Entry(MembersName_F,font=('arial',14,'bold'), bd=7,textvariable=ReferenceNo, insertwidth=2)
        self.txtReferenceNo.grid(row=0 ,column=1)

        self.lblFirstname=Label(MembersName_F,font=('arial',14,'bold'),text=" First Name ",bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname=Label(MembersName_F,font=('arial',14,'bold'),text=" Surname ",bd=7)
        self.lblSurname.grid(row=2 ,column=0, sticky=W)
        self.txtSurname=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=2 ,column=1)

        self.lblAddress=Label(MembersName_F,font=('arial',14,'bold'),text=" Address ",bd=7)
        self.lblAddress.grid(row=3 ,column=0, sticky=W)
        self.txtAddress=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3 ,column=1)

        self.lblPostcode=Label(MembersName_F,font=('arial',14,'bold'),text=" Postcode ",bd=7)
        self.lblPostcode.grid(row=4 ,column=0, sticky=W)
        self.txtPostcode=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Postcode,insertwidth=2)
        self.txtPostcode.grid(row=4 ,column=1)

        self.lblTelephone=Label(MembersName_F,font=('arial',14,'bold'),text=" Telephone ",bd=7)
        self.lblTelephone.grid(row=5 ,column=0, sticky=W)
        self.txtTelephone=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Telephone,insertwidth=2)
        self.txtTelephone.grid(row=5 ,column=1)

        self.lblDate=Label(MembersName_F,font=('arial',14,'bold'),text=" Date ",bd=7)
        self.lblDate.grid(row=6 ,column=0, sticky=W)
        self.txtDate=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable= DateofOrder,insertwidth=2)
        self.txtDate.grid(row=6 ,column=1)

        self.lblProve_of_ID=Label(MembersName_F,font=('arial',14,'bold'),text=" Prove of ID ",bd=7)
        self.lblProve_of_ID.grid(row=7 ,column=0, sticky=W)

        self.cboProve_of_ID=ttk.Combobox(MembersName_F,textvariable = var1, state='readonly', font=('arial',14,'bold'), width=19)
        self.cboProve_of_ID['value']=('','Pilot License', 'Driving License','Passport','Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7 ,column=1, sticky=W)

        self.lblMethod_of_Payment=Label(MembersName_F,font=('arial',14,'bold'),text=" Method of Payment ",bd=7)
        self.lblMethod_of_Payment.grid(row=8 ,column=0, sticky=W)

        self.cboMethod_of_Payment=ttk.Combobox(MembersName_F,textvariable = var3, state='readonly', font=('arial',14,'bold'), width=19)
        self.cboMethod_of_Payment['value']=('','Visa card', 'Debit card','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=8 ,column=1, sticky=W)

        self.chkMembership = Checkbutton(MembersName_F, text=" Total Amount ", variable=var4, onvalue = 1,offvalue = 0,font=('arial',16,'bold'), command=Membership_Fees).grid(row=9, column=0, sticky=W)

        self.txtMembership = Entry(MembersName_F,font=('arial',14,'bold'), textvariable=Membership, bd=7, insertwidth=2, state= DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=9,column=1)
        self.btnsubmit=Button(MembersName_F,padx=18,bd=7,font=("arial",14,"bold"),width=11,
                    text="submit",command=database).grid(row=10,column=1)

        #self.lblLabel=Label(Receipt_ButtonFrame,font=('arial',10,'bold'),pady=10,text="  ReferenceNo\t Firstname\t Surname\t Address\t\t Telephone\t Payment ",bd=7)
        #self.lblLabel.grid(row=0 ,column=0, columnspan=4)

        
        self.patientlist = Listbox(Receipt_ButtonFrame,width=100, height=22, font=('arial',10,'bold'))
        self.patientlist.grid(row=1,column=0, columnspan=6)

        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Receipt ", command= Receipt).grid(row =2, column=0)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" patientdetails", command=view_data ).grid(row =2, column=1)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" update ", command= update).grid(row =2, column=2)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" delete ", command= deletedata).grid(row =2, column=3)
        
        self.btnReset=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Reset ", command=Reset ).grid(row =2, column=4)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Exit ", command=iExit).grid(row =2, column=5)


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management ")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        cmbNameTablets=StringVar()
        Ref = StringVar()
        Dose =StringVar()
        NumberTablets =StringVar()
        Lot =StringVar()
        IssuedDate =StringVar()
        ExpDate =StringVar()
        DailyDose =StringVar()
        PossibleSideEffects =StringVar()
        FurtherInformation =StringVar()
        StorageAdvice =StringVar()
        DrivingUsingMachines =StringVar()
        HowtoUseMedications =StringVar()
        PatientID =StringVar()
        PatientNHSNo =StringVar()
        PatientName =StringVar()
        DateofBirth =StringVar()
        PatientAddress =StringVar()
        Prescription =StringVar()
        NHSNumber = StringVar()
        #================================================================Function Declaration=======================================================================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Pharmacy Management ","Confirm if you want to Exit")
            if iExit >0:
                self.master.destroy()            
                return

        def iPrescription():
            self.txtPrescription.insert(END,'Name of Tablets:\t\t\t' + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,'Reference No. :\t\t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(END,'Dose:\t\t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(END,'Number of tablets:\t\t\t' +  NumberTablets.get()+ "\n")
            self.txtPrescription.insert(END,'Lot:\t\t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(END,'Issued Date:\t\t\t' + IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,'Exp. Date:\t\t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,'Daily Dose:\t\t\t' + DailyDose.get() + "\n")
            self.txtPrescription.insert(END,'Possible Side Effects:\t\t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END,'Further Information:\t\t\t' + FurtherInformation.get()+ "\n")
            self.txtPrescription.insert(END,'Storage Advice:\t\t\t' + StorageAdvice.get()+ "\n")
            self.txtPrescription.insert(END,'Driving or using Machine:\t\t\t' + DrivingUsingMachines.get()+ "\n")
            self.txtPrescription.insert(END,'How to use Medication:\t\t\t' + HowtoUseMedications.get() + "\n")
            self.txtPrescription.insert(END,'Patient ID:\t\t\t' + PatientID.get()+ "\n")
            self.txtPrescription.insert(END,'NHS Number:\t\t\t' + NHSNumber.get() + "\n")
            self.txtPrescription.insert(END,'Patient Name:\t\t\t' + PatientName.get() + "\n")
            self.txtPrescription.insert(END,'Date of Birth:\t\t\t' + DateofBirth.get() + "\n")
            self.txtPrescription.insert(END,'Patient Address:\t\t\t' + PatientAddress.get()+ "\n")
            return
        def  database1(*args):
            nametablets=cmbNameTablets.get()
            ref=Ref.get()
            dose=Dose.get()
            numbertablets=NumberTablets.get()
            lot=Lot.get()
            issueddate=IssuedDate.get()
            expdate=ExpDate.get()
            dailydose=DailyDose.get()
            possiblesideeffects=PossibleSideEffects.get()
            furtherinformation=FurtherInformation.get()
            storageadvice=StorageAdvice.get()
            drivingusingmachine=DrivingUsingMachine.get()
            howtousemedications=HowtoUseMedications.get()
            patientid=PatientID.get()
            patientnhsno=PatientNHSNo.get()
            patientname=PatientName.get()
            dateofbirth=DateofBirth.get()
            patientaddress=PatientAddress.get()
            nhsnumber=NHSNumber.get()
            conn=sqlite3.connect("pharmacy.db")
            with conn:
                cursor=conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS Pharmacy(cmbNameTablets TEXT, Ref INTEGER, Dose INTEGER, NumberTablets INTEGER, Lot INTEGER,  IssuedDate DATE, ExpDate DATE, DailyDose TEXT, PossibleSideEffects TEXT, FurtherInformation TEXT, StorageAdvice TEXT, DrivingUsingMachine TEXT, HowtoUseMedications TEXT, PatientID NUMERIC PRIMARY KEY, PatientNHSNo NUMERIC, PatientName TEXT, DateofBirth DATE, PatientAddress TEXT, NHSNumber NUMERIC)")
                cursor.execute("INSERT INTO Pharmacy(cmbNameTablets,Ref,Dose,NumberTablets,Lot,IssuedDate,ExpDate,DailyDose,PossibleSideEffects,FurtherInformation,StorageAdvice,DrivingUsingMachine,HowtoUseMedications,PatientID,PatientNHSNo,PatientName,DateofBirth,PatientAddress,NHSNumber)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(nametablets,ref,dose,numbertablets,lot,issueddate,expdate,dailydose,possiblesideeffects,furtherinformation,storageadvice,drivingusingmachine,howtousemedications,patientid,patientnhsno,patientname,dateofbirth,patientaddress,nhsnumber))
                conn.commit()
                showinfo( title = "pharmacy data", message = "Data inserted To table")

        def displaydata1():
            conn=sqlite3.connect("pharmacy.db")
            cursor=conn.cursor()
            cursor.execute("select * from Pharmacy")
            conn.commit()
            row=cursor.fetchall()
            conn.close()
            return row
        
        def view_data1():
            for row in displaydata1():
                self.txtFrameDetail.insert(END,"cmbNameTablets="+row[0],
                                           "\t\tRef=",row[1],
                                           "\t\tDose=",row[2],
                                           "\t\tNumberTablets=",row[3],
                                           "\t\tLot=",row[4],
                                           "\t\tIssuedDate=",row[5],
                                           "\t\tExpDate=",row[6],
                                           "\t\tDailyDose="+row[7],
                                           "\t\tPossibleSideEffects="+row[8],
                                           "\t\tFurtherInformation="+row[9],
                                           "\t\tStorageAdvice="+row[10],
                                           "\t\tDrivingUsingMachine="+row[11],
                                           "\t\tHowtoUseMedications="+row[12],
                                           "\t\tPatientID=",row[13],
                                           "\t\tPatientNHSNo=",row[14],
                                           "\t\tPatientName="+row[15],
                                           "\t\tDateofBirth=",row[16],
                                           "\t\tPatientAddress="+row[17],
                                           "\t\tNHSNumber=",row[18],"\n")

        def pharmacy_delete():
            patientid=PatientID.get()
            conn=sqlite3.connect("pharmacy.db")
            cursor=conn.cursor()
            cursor.execute("DELETE FROM Pharmacy WHERE PatientID = ?",(patientid,))
            conn.commit()
            showinfo( title = "pharmacy data", message = "Data deleted from table")
            conn.close()

        def update1():
            patientid=PatientID.get()
            nametablets=cmbNameTablets.get()
            ref=Ref.get()
            dose=Dose.get()
            numbertablets=NumberTablets.get()
            lot=Lot.get()
            issueddate=IssuedDate.get()
            expdate=ExpDate.get()
            dailydose=DailyDose.get()
            possiblesideeffects=PossibleSideEffects.get()
            furtherinformation=FurtherInformation.get()
            storageadvice=StorageAdvice.get()
           # drivingusingmachine=DrivingUsingMachine.get()
            howtousemedications=HowtoUseMedications.get()
            patientnhsno=PatientNHSNo.get()
            patientname=PatientName.get()
            dateofbirth=DateofBirth.get()
            patientaddress=PatientAddress.get()
            nhsnumber=NHSNumber.get()
            conn=sqlite3.connect("pharmacy.db")
            cursor=conn.cursor()
            cursor.execute("UPDATE Pharmacy set cmbNameTablets = ? WHERE PatientID = ?",(nametablets,patientid,))
            cursor.execute("UPDATE Pharmacy set Ref = ? WHERE PatientId = ?",(ref,patientid,))
            cursor.execute("UPDATE Pharmacy set Dose = ? WHERE PatientId = ?",(dose,patientid,))
            cursor.execute("UPDATE Pharmacy set NumberTablets = ? WHERE PatientId = ?",(numbertablets,patientid,))
            cursor.execute("UPDATE Pharmacy set Lot = ? WHERE PatientId = ?",(lot,patientid,))
            cursor.execute("UPDATE Pharmacy set IssuedDate = ? WHERE PatientId = ?",(issueddate,patientid,))
            cursor.execute("UPDATE Pharmacy set Expdate = ? WHERE PatientId = ?",(expdate,patientid,))
            cursor.execute("UPDATE Pharmacy set DailyDose = ? WHERE PatientId = ?",(dailydose,patientid,))
            cursor.execute("UPDATE Pharmacy set PossibleSideEffects = ? WHERE PatientId = ?",(possiblesideeffects,patientid,))
            cursor.execute("UPDATE Pharmacy set FurtherInformation = ? WHERE PatientId = ?",(furtherinformation,patientid,))
            cursor.execute("UPDATE Pharmacy set StorageAdvice = ? WHERE PatientId = ?",(storageadvice,patientid,))
           # cursor.execute("UPDATE Pharmacy set DrivingUsingMachine = ? WHERE PatientId = ?",(drivingusingmachine,patientid,))
            cursor.execute("UPDATE Pharmacy set HowtoUseMedications = ? WHERE PatientId = ?",(howtousemedications,patientid,))
            cursor.execute("UPDATE Pharmacy set PatientNHSNo = ? WHERE PatientId = ?",(patientnhsno,patientid,))
            cursor.execute("UPDATE Pharmacy set PatientName = ? WHERE PatientId = ?",(patientname,patientid,))
            cursor.execute("UPDATE Pharmacy set DateofBirth = ? WHERE PatientId = ?",(dateofbirth,patientid,))
            cursor.execute("UPDATE Pharmacy set PatientAddress = ? WHERE PatientId = ?",(patientaddress,patientid,))
            cursor.execute("UPDATE Pharmacy set NHSNumber = ? WHERE PatientId = ?",(nhsnumber,patientid,))
            conn.commit()
            showinfo( title = "patient data", message = "Data updated  table")
            conn.close()

        def iReceipt():
            self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t"+ Ref.get()+"\t"+ Dose.get()+"\t\t"+NumberTablets.get()+ "\t"+ Lot.get() +"\t\t"+ ExpDate.get() +"\t" +DailyDose.get() +"\t\t"+ StorageAdvice.get() +"\t"+NHSNumber.get() +"\t\t"+ PatientName.get() + "\t"+ DateofBirth.get() +"\t"+ PatientAddress.get() +"\n")
            return

        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedications.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSNumber.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            
            return

        def iReset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedications.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSNumber.set("")
            self.txtPrescription.delete("1.0",END)
            
            return

        
        #================================================================Frame=======================================================================================

        MainFrame =Frame(self.frame)
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame, font=('arial', 40, 'bold'), text="Pharmacy Management ", padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE
                             , font=('arial', 12, 'bold'), text="Patient Information:",)
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE
                                   , font=('arial', 12, 'bold'), text="Prescription:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #===============================================================DataFrameLeft==================================================================================================

        self.lblNameTablets =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablets:", padx=2,pady=2)
        self.lblNameTablets.grid(row=0, column=0, sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets, state='readonly',font=('arial', 12, 'bold'), width=20)
        self.cboNameTablet['value']=('','Ibuprofen','Co-codamol','Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:", padx=2,pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=FurtherInformation, width=25)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.lblRef =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblStorage =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice:", padx=2, pady=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=StorageAdvice, width=25)
        self.txtStorage.grid(row=1, column=3)

        self.lblDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Dose, width=25)
        self.txtDose.grid(row=2, column=1)

        self.lblDUseMachine =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machines:", padx=2, pady=2)
        self.lblDUseMachine.grid(row=2, column=2, sticky=W)
        self.txtDUseMachine=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DrivingUsingMachines, width=25)
        self.txtDUseMachine.grid(row=2, column=3)

        self.lblNoOfTablets =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="No of Tablets:", padx=2, pady=2)
        self.lblNoOfTablets.grid(row=3, column=0, sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=NumberTablets, width=25)
        self.txtNoOfTablets.grid(row=3, column=1)

        self.lblUseMedication =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="How to use Medications:", padx=2, pady=2)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=HowtoUseMedications, width=25)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Lot, width=25)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient ID:", padx=2, pady=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientID, width=25)
        self.txtPatientID.grid(row=4, column=3)

        self.lblIssuedDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date:", padx=2, pady=2)
        self.lblIssuedDate.grid(row=5, column=0, sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=IssuedDate, width=25)
        self.txtIssuedDate.grid(row=5, column=1)

        self.lblNHSNumber =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NHS Number:", padx=2, pady=2)
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=NHSNumber, width=25)
        self.txtNHSNumber.grid(row=5, column=3)

        self.lblExpDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Expiry Date:", padx=2, pady=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=ExpDate, width=25)
        self.txtExpDate.grid(row=6, column=1)

        self.lblPatientName =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Name:", padx=2, pady=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientName, width=25)
        self.txtPatientName.grid(row=6, column=3)

        self.lblDailyDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose:", padx=2, pady=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DailyDose, width=25)
        self.txtDailyDose.grid(row=7, column=1)

        self.lblDateofBirth =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth:", padx=2, pady=2)
        self.lblDateofBirth.grid(row=7, column=2, sticky=W)
        self.txtDateofBirth=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DateofBirth, width=25)
        self.txtDateofBirth.grid(row=7, column=3)

        self.lblSideEffects =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="SideEffects:", padx=2, pady=2)
        self.lblSideEffects.grid(row=8, column=0, sticky=W)
        self.txtSideEffects=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PossibleSideEffects, width=25)
        self.txtSideEffects.grid(row=8, column=1)

        self.lblPatientAddress =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Address:", padx=2, pady=2)
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientAddress, width=25)
        self.txtPatientAddress.grid(row=8, column=3)

        #===============================================================DataFrameRight==================================================================================================

        self.txtPrescription=Text(DataFrameRIGHT, font=('arial', 12, 'bold'),width = 43, height=14, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #===============================================================ButtonFrame==================================================================================================

        self.btnPrescription=Button(ButtonFrame, text='Prescription', font=('arial', 12,'bold'), width = 24, bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)        
        self.btnReceipt=Button(ButtonFrame, text='Receipt', font=('arial', 12,'bold'), width = 24, bd=4,
                               command=iReceipt)
        self.btnReceipt.grid(row=0, column=1)
        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial', 12,'bold'), width = 24, bd=4,
                              command=iDelete)
        self.btnDelete.grid(row=0, column=2)
        self.btnReset=Button(ButtonFrame, text='Reset', font=('arial', 12,'bold'), width = 24, bd=4,
                             command=iReset)
        self.btnReset.grid(row=0, column=3)
        self.btnExit=Button(ButtonFrame, text='Exit', font=('arial', 12,'bold'), width = 24, bd=4,
                            command=iExit)
        self.btnExit.grid(row=0, column=4)

        self.lblLabel=Label(FrameDetail, font=('arial', 10, 'bold'), pady=6, text="Name of Tablets\tReference No.\tDosage\tNo. of Tablet\tLot\tIssued Date\t Exp. Date\tDaily Dose\tStorage Adv\tNHS Number\tPatients Name\tDOB\tAddress")
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail=Text(FrameDetail, font=('arial', 12, 'bold'),width = 141, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=0, column=0)

class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Registration ")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()                
        Postcode=StringVar()
        Telephone=StringVar()
        DoctorID=StringVar()
        Department=StringVar()
        Degree=StringVar()
        DutyTime=StringVar()
        


        def iExit():
            iExit = tkinter.messagebox.askyesno("Doctor Registration ", "Confirm if you want to exit")
            if iExit>0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")                
            Postcode.set("")
            Telephone.set("")
            DoctorID.set("")
            Department.set("")
            Degree.set("")
            DutyTime.set("")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askyesno("Doctor Registration ", "Confirm if you want to add a new\ record")
            if iResetRecord>0:
                Reset()
            elif iResetRecord <=0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return

        def Doctor_ID():
            x = random.randint(10903, 600873)
            randomDoctorID = str(x)
            DoctorID.set(randomDoctorID)

        def Receipt():
            #self.patientlist.insert(END,"\t" + ReferenceNo.get()+ "\t\t" +Firstname.get() + "\t\t" +Surname.get()+"\t\t"+Address.get() +"\t\t" +DateofOrder.get()+"\t\t" +Telephone.get() +"\t\t" +Membership.get() +"\n")
            self.doctorlist.insert(END,"\t" "Firstname of patient="+ Firstname.get()+ "\t""\n")
            self.doctorlist.insert(END,"\t" "Surname of patient="+ Surname.get()+ "\t""\n")  
            self.doctorlist.insert(END,"\t" "Address="+ Address.get()+ "\t""\n")
            self.doctorlist.insert(END,"\t" "Department="+Department.get()+ "\t""\n")

            self.doctorlist.insert(END,"\t" ".........................................contact.................................""\t\t""\n")
            
        
        def  database4(*args):
            
            firstname=Firstname.get()
            surname=Surname.get()
            address=Address.get()
            postcode=Postcode.get()
            telephone=Telephone.get()
            department=Department.get()
            doctorid=DoctorID.get()
            degree=Degree.get()
            dutytime=DutyTime.get()
            conn=sqlite3.connect("Doctor.db")
            with conn:
                cursor=conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS doctor(Firstname TEXT,Surname TEXT,Address TEXT,Postcode INTEGER,Telephone NUMERIC,Department TEXT,DoctorID NUMERIC primary key,Degree TEXT,DutyTime INTEGER)")
                cursor.execute("INSERT INTO doctor(Firstname,Surname,Address, Postcode,Telephone,Department,DoctorID,Degree,DutyTime)VALUES(?,?,?,?,?,?,?,?,?)",(firstname,surname,address,postcode,telephone,department,doctorid,degree,dutytime))
                
                conn.commit()
                #showinfo( title = "doctor data", message = "Data inserted To table")
        def displaydata4():
            conn=sqlite3.connect("Doctor.db")
            cursor=conn.cursor()
            cursor.execute("select * from doctor")
            row=cursor.fetchall()
            conn.close()
            return row
        def view_data4():
            #Ref_no()
            for row in displaydata4():
                
                self.doctorlist.insert(END,"Firstname=",row[0],
                                        "Surname=",row[1],
                                        "Address=",row[2],
                                        "Postcode=",row[3],
                                        "Telephone=",row[4],
                                        "Department=",row[5],
                                        "doctorID=",row[6],
                                        "Degree=",row[7],
                                        "dutytime=",row[8],"\n")    
        
        def deletedata4():
            doctorid=DoctorID.get()
            conn=sqlite3.connect("Doctor.db")
            cursor=conn.cursor()
            cursor.execute("DELETE FROM doctor WHERE DoctorID=?",(doctorid,))
            conn.commit()
            #showinfo( title = "doctor data", message = "Data deleted sucessfully")
            conn.close()
        
               
        
        def update4():
            doctorid=DoctorID.get()
            firstname=Firstname.get()
            surname=Surname.get()
            address=Address.get()
            postcode=Postcode.get()
            telephone=Telephone.get()
            department=Department.get()
            degree=Degree.get()
            dutytime=DutyTime.get()
            
            conn=sqlite3.connect("Doctor.db")
            cursor=conn.cursor()
            cursor.execute("UPDATE doctor SET Firstname=?,Surname=?,Address=?,Postcode=?,Telephone=?,Department=?,Degree=?,DutyTime=? WHERE DoctorID=?",(firstname,surname,address,postcode,telephone,department,degree,dutytime,doctorid))
            conn.commit()
            #showinfo( title = "doctor data", message = " doctor data update sucessfully")
            conn.close
            
            
            
        Mainframe=Frame(self.frame)
        Mainframe.grid()
        TitleFrame=Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame,font=('arial',59,'bold'),text=" Doctor Registration ",padx=2)
        self.lblTitle.grid()

        MemberDetailsFrame = LabelFrame(Mainframe, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,font=('arial',12,'bold'),text ='Patient Name',relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame, bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        self.lblDoctorID=Label(MembersName_F,font=('arial',14,'bold'),text=" DoctorID ",bd=7)
        self.lblDoctorID.grid(row=0 ,column=0, sticky=W)
        self.txtDoctorID=Entry(MembersName_F,font=('arial',14,'bold'), bd=7,textvariable=DoctorID, insertwidth=2)
        self.txtDoctorID.grid(row=0 ,column=1)

        self.lblFirstname=Label(MembersName_F,font=('arial',14,'bold'),text=" First Name ",bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname=Label(MembersName_F,font=('arial',14,'bold'),text=" Surname ",bd=7)
        self.lblSurname.grid(row=2 ,column=0, sticky=W)
        self.txtSurname=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=2 ,column=1)

        self.lblAddress=Label(MembersName_F,font=('arial',14,'bold'),text=" Address ",bd=7)
        self.lblAddress.grid(row=3 ,column=0, sticky=W)
        self.txtAddress=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3 ,column=1)

        self.lblPostcode=Label(MembersName_F,font=('arial',14,'bold'),text=" Postcode ",bd=7)
        self.lblPostcode.grid(row=4 ,column=0, sticky=W)
        self.txtPostcode=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Postcode,insertwidth=2)
        self.txtPostcode.grid(row=4 ,column=1)

        self.lblTelephone=Label(MembersName_F,font=('arial',14,'bold'),text=" Telephone ",bd=7)
        self.lblTelephone.grid(row=5 ,column=0, sticky=W)
        self.txtTelephone=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Telephone,insertwidth=2)
        self.txtTelephone.grid(row=5 ,column=1)

        self.lblDepartment=Label(MembersName_F,font=('arial',14,'bold'),text=" Department ",bd=7)
        self.lblDepartment.grid(row=6 ,column=0, sticky=W)
        self.txtDepartment=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Department,insertwidth=2)
        self.txtDepartment.grid(row=6 ,column=1)

        self.lblDegree=Label(MembersName_F,font=('arial',14,'bold'),text=" Degree",bd=7)
        self.lblDegree.grid(row=7 ,column=0, sticky=W)
        self.txtDegree=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=Degree,insertwidth=2)
        self.txtDegree.grid(row=7 ,column=1)

        self.lblDutyTime=Label(MembersName_F,font=('arial',14,'bold'),text=" Duty Time ",bd=7)
        self.lblDutyTime.grid(row=8 ,column=0, sticky=W)
        self.txtDutyTime=Entry(MembersName_F,font=('arial',14,'bold'), bd=7, textvariable=DutyTime,insertwidth=2)
        self.txtDutyTime.grid(row=8 ,column=1)




       
        self.lblProve_of_ID=Label(MembersName_F,font=('arial',14,'bold'),text=" Prove of ID ",bd=7)
        self.lblProve_of_ID.grid(row=9 ,column=0, sticky=W)

        self.cboProve_of_ID=ttk.Combobox(MembersName_F,textvariable = var1, state='readonly', font=('arial',14,'bold'), width=19)
        self.cboProve_of_ID['value']=('','Pilot License', 'Driving License','Passport','PAN Id')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=9 ,column=1, sticky=W)

        
        
        self.btnsubmit=Button(MembersName_F,padx=18,bd=7,font=("arial",14,"bold"),width=11,
                    text="submit",command=database4).grid(row=10,column=1)
        
        #self.lblLabel=Label(Receipt_ButtonFrame,font=('arial',10,'bold'),pady=10,text=" \tDoctor ID\tFirstname\t Surname\t Address\t\t Telephone\tDepartment\tDegree  ",bd=7)
        #self.lblLabel.grid(row=0 ,column=0, columnspan=4)

        
        self.doctorlist = Listbox(Receipt_ButtonFrame,width=112, height=22, font=('arial',10,'bold'))
        self.doctorlist.grid(row=1,column=0, columnspan=6)

        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Receipt ", command= Receipt).grid(row =2, column=0)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" patientdetails", command=view_data4 ).grid(row =2, column=1)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" update ", command= update4).grid(row =2, column=2)
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" delete ", command= deletedata4).grid(row =2, column=3)
        
        self.btnReset=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Reset ", command=Reset ).grid(row =2, column=4)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18, bd=7, font=('arial',9,'bold'),width=13, text=" Exit ", command=iExit).grid(row =2, column=5)





if __name__ == '__main__':
    main()
