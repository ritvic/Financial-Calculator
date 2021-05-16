from tkinter import *
import tkinter.messagebox
import webbrowser
from PIL import Image, ImageTk

window = Tk()
window.title("Financial Calculator")
window.resizable(width=False,height=False)

image_picture = Image.open("stock.jpg")
image_picture=image_picture.resize((500,500))
pho = ImageTk.PhotoImage(image_picture)
t_label = Label(image = pho)
t_label.pack()

#TO EXIT THE MAIN WINDOW
def iExit():
    iExit = tkinter.messagebox.askyesno("Financial Calculator", "Do you want to exit ?")
    if iExit > 0:
        window.destroy()
        return

#PROFIT MARGIN CALCULATOR CODE
def Marg_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calculator window
            windo = Tk()
            windo.title("Profit Margin Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Cost", bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Sale Revenue",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Gross Margin",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Gross Profit",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.margin = StringVar()
            lblMontyment = Label(windo, textvariable=self.margin,bg='LightSteelBlue1').grid(row=3, column=2, sticky=E)

            self.profit = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.profit,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("http://calculator.net/margin-calculator.html"))
            link.grid(row=6, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Profit Margin Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=1, sticky=W)

        def go(self, a, b):#To calculatae future value
            futurevalue = 100 - a / b * 100
            return futurevalue

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.go(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()))
            self.margin.set(format(futureValue, '10.3f'))
            i = float(self.annualInterestRateVar.get())-float(self.loanAmountVar.get())
            self.profit.set(format(i, '10.3f'))

    LoanCalculator()

#DISCOUNT CALCULATOR CODE
def Disc_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a claculator window
            windo = Tk()
            windo.title("Discount Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Original Price",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Discount",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Price after Discount",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="You Saved",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            lblMontyment = Label(windo, textvariable=self.numberOfYearsVar,bg='LightSteelBlue1').grid(row=3, column=2, sticky=E)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/discount-calculator.html"))
            link.grid(row=6, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Discount Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()))
            self.numberOfYearsVar.set(format(futureValue, '10.3f'))
            d= float(self.loanAmountVar.get()) - futureValue
            self.futureValueVar.set(format(d,'10.3f'))

        def getfutureValue(self, a,b):#To calculate the future value
            c = a * (1-b/100)
            return c

    LoanCalculator()

#SALES TAX CALCULATOR CODE
def Sale_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calculator window
            windo = Tk()
            windo.title("Sales Tax Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Original Price",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Sales Tax",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="VAT",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="After Tax Price ",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/sales-tax-calculator.html"))
            link.grid(row=6, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Sales Tax Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=5, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get())/1200)
            self.futureValueVar.set(format(futureValue, '10.3f'))

        def getfutureValue(self, loanAmount, annualInterestRate, numberOfYears):#To calculate future value
            futurevalue = loanAmount * (1 + annualInterestRate*12 + numberOfYears*12)
            return futurevalue

    LoanCalculator()

#INFLATION CALCULATOR CODE
def Infl_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calculator window
            windo = Tk()
            windo.title("Inflation Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Present Value",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Inflation Rate",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Forward Flat Rate Inflation Value",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Backward Flat Rate Inflation Value",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.incrementVar = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.incrementVar,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/inflation-calculator.html"))
            link.grid(row=7, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator
                wExit = tkinter.messagebox.askyesno("Inflation Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))
            increment =  self.getincrement(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))

            self.futureValueVar.set(format(futureValue, '10.3f'))
            self.incrementVar.set(format(increment, '10.3f'))

        def getfutureValue(self, loanAmount, annualInterestRate, numberOfYears):#To calculate future value
            futurevalue = loanAmount * ((1 + annualInterestRate*12) ** numberOfYears)
            return futurevalue
        def getincrement(self, loanAmount, annualInterestRate, numberOfYears):#To calculate increment value
            futurevalue = loanAmount / ((1 + annualInterestRate * 12) ** numberOfYears)
            return futurevalue

    LoanCalculator()

#SALARY CALCULATOR CODE
def Sala_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calculator window
            windo = Tk()
            windo.title("Salary Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Basic Salary",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="House Rent Allowance",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Transport Allowance",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="FBP Allowance",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Statutory Bonus",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)
            Label(windo, text="Income Tax",bg='LightSteelBlue1').grid(row=6, column=1, sticky=W)
            Label(windo, text="Provident Fund",bg='LightSteelBlue1').grid(row=7, column=1, sticky=W)
            Label(windo, text="Gross Salary",bg='LightSteelBlue1').grid(row=8, column=1, sticky=W)
            Label(windo, text="Net Salary",bg='LightSteelBlue1').grid(row=9, column=1, sticky=W)

            self.BasicSalaryVar = StringVar()
            Entry(windo, textvariable=self.BasicSalaryVar, justify=RIGHT).grid(row=1, column=2)

            self.HouseRentAllowanceVar = StringVar()
            Entry(windo, textvariable=self.HouseRentAllowanceVar, justify=RIGHT).grid(row=2, column=2)

            self.TransportAllowanceVar = StringVar()
            Entry(windo, textvariable=self.TransportAllowanceVar, justify=RIGHT).grid(row=3, column=2)

            self.FBPAllowanceVar = StringVar()
            Entry(windo, textvariable=self.FBPAllowanceVar, justify=RIGHT).grid(row=4, column=2)

            self.StatuoryBonusVar = StringVar()
            Entry(windo, textvariable=self.StatuoryBonusVar, justify=RIGHT).grid(row=5, column=2)

            self.IncomeTaxVar = StringVar()
            Entry(windo, textvariable=self.IncomeTaxVar, justify=RIGHT).grid(row=6, column=2)

            self.ProvidentFundVar = StringVar()
            Entry(windo, textvariable=self.ProvidentFundVar, justify=RIGHT).grid(row=7, column=2)

            self.GrossSalaryVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.GrossSalaryVar,bg='LightSteelBlue1').grid(row=8, column=2, sticky=E)

            self.NetSalaryVar = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.NetSalaryVar,bg='LightSteelBlue1').grid(row=9, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/salary-calculator.html"))
            link.grid(row=11, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator
                wExit = tkinter.messagebox.askyesno("Salary Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=10, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=10, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            gross= self.getgross(float(self.BasicSalaryVar.get()),float(self.HouseRentAllowanceVar.get()),float(self.TransportAllowanceVar.get()),float(self.FBPAllowanceVar.get()), float(self.StatuoryBonusVar.get()))

            self.GrossSalaryVar.set(format(gross, '10.3f'))
            net = float(self.GrossSalaryVar.get()) - float(self.ProvidentFundVar.get()) - float(self.IncomeTaxVar.get())
            self.NetSalaryVar.set(format(net, '10.3f'))

        def getgross(self, a,b,c,d,e):#To calculate gross value
            futurevalue = a+b+c+d+e
            return futurevalue

    LoanCalculator()

#PRESENT VALUE CALCULATOR CODE
def Pres_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calcutor window
            windo = Tk()
            windo.title("Present Value Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Future Value Amount",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Annual Interest Rate",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Present Value",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Decrease in Value",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.increment = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.increment,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/present-value-calculator.html"))
            link.grid(row=7, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Present Value Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))


            self.futureValueVar.set(format(futureValue, '10.3f'))
            increaseinvalue = - float(self.futureValueVar.get()) + float(self.loanAmountVar.get())
            self.increment.set(format(increaseinvalue, '10.3f'))

        def getfutureValue(self, loanAmount, annualInterestRate, numberOfYears):#To calculate the future value
            futurevalue = loanAmount / ((1 + annualInterestRate*12) ** numberOfYears)
            return futurevalue

    LoanCalculator()

#FUTUTRE VALUE CALCULATOR CODE
def Futu_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #To create a calculator window
            windo = Tk()
            windo.title("Future Value Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Present Value",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Annual Interest Rate",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Future Value",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Increase in Value",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.increment = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.increment,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/future-value-calculator.html"))
            link.grid(row=7, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Future Value Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=1, sticky=W)

        def computePayment(self):#To calculte and display desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))


            self.futureValueVar.set(format(futureValue, '10.3f'))
            increaseinvalue = float(self.futureValueVar.get()) - float(self.loanAmountVar.get())
            self.increment.set(format(increaseinvalue, '10.3f'))

        def getfutureValue(self, loanAmount, annualInterestRate, numberOfYears):#To calculate future value
            futurevalue = loanAmount * ((1 + annualInterestRate*12) ** numberOfYears)
            return futurevalue

    LoanCalculator()

#AMORTIZATION CALCULTOR CODE
def Amor_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating a calculator window
            windo = Tk()
            windo.title("Amortization Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Loan Amount",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Annual Interest Rate",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Monthly Payment",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Total Interest",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)
            Label(windo, text="Total Payment",bg='LightSteelBlue1').grid(row=6, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.monthlyPaymentVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.monthlyPaymentVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.totalInterestVar = StringVar()
            lblTotalInterest = Label(windo, textvariable=self.totalInterestVar,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            self.totalPaymentVar = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.totalPaymentVar,bg='LightSteelBlue1').grid(row=6, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/amortization-calculator.html"))
            link.grid(row=8, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the calculator window
                wExit = tkinter.messagebox.askyesno("Amortization Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=7, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=7, column=1, sticky=W)

        def computePayment(self):#To calculate and display the desired values
            monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))

            self.monthlyPaymentVar.set(format(monthlyPayment, '10.3f'))
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 * float(self.numberOfYearsVar.get())

            self.totalPaymentVar.set(format(totalPayment, '10.3f'))
            totalInterest = float(self.totalPaymentVar.get()) - float(self.loanAmountVar.get())
            self.totalInterestVar.set(format(totalInterest, '10.3f'))

        def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):#To calculate monthly payment
            monthlyPayment = loanAmount * monthlyInterestRate / (1- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment

    LoanCalculator()

#ROI CALCULATOR CODE
def ROI_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            #Creating calculator window

            windo = Tk()
            windo.title("ROI Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Amount Invested",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="ROI",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Total Returns",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Investment Gain",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)
            Label(windo, text="Amount Invested",bg='LightSteelBlue1').grid(row=8, column=1, sticky=W)
            Label(windo, text="Total Returns",bg='LightSteelBlue1').grid(row=9, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=10, column=1, sticky=W)
            Label(windo, text="ROI",bg='LightSteelBlue1').grid(row=11, column=1, sticky=W)
            Label(windo, text="Annualised Returns",bg='LightSteelBlue1').grid(row=12, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.futureValueVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.futureValueVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.increment = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.increment,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=6, column=2, sticky=E)

            self.invested= StringVar()
            Entry(windo, textvariable=self.invested, justify=RIGHT).grid(row=8, column=2)

            self.returns = StringVar()
            Entry(windo, textvariable=self.returns, justify=RIGHT).grid(row=9, column=2)

            self.years = StringVar()
            Entry(windo, textvariable=self.years, justify=RIGHT).grid(row=10, column=2)

            self.ROI = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.ROI,bg='LightSteelBlue1').grid(row=11, column=2, sticky=E)

            self.annualised = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.annualised,bg='LightSteelBlue1').grid(row=12, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/roi-calculator.html"))
            link.grid(row=14, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=1)

            def wExit():#To exit the claculator window
                wExit = tkinter.messagebox.askyesno("ROI Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.cPayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=13, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=13, column=1, sticky=W)

        def cPayment(self):
            percent = self.getValue(float(self.invested.get()),float(self.returns.get()))
            self.ROI.set(format(percent, '10.3f'))
            ann = self.giveme(float(percent)/100+1,float(self.years.get()))
            self.annualised.set(format(ann, '10.3f'))

        def getValue(self,a,b):
            c= (b-a)/a*100
            return c

        def giveme(self,a,b):
            c= 100*(a**(1/b)-1)
            return c

        def computePayment(self):#To calculate and display the desired values
            futureValue = self.getfutureValue(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))

            self.futureValueVar.set(format(futureValue, '10.3f'))
            increaseinvalue = float(self.futureValueVar.get()) - float(self.loanAmountVar.get())
            self.increment.set(format(increaseinvalue, '10.3f'))

        def getfutureValue(self, loanAmount, annualInterestRate, numberOfYears):#To calculate the future value
            futurevalue = loanAmount * ((1 + annualInterestRate*12) ** numberOfYears)
            return futurevalue

    LoanCalculator()

#LOAN CALCULATOR CODE
def Loan_Calc():
    window.destroy()
    class LoanCalculator:
        def __init__(self):
            # Creating calculator window
            windo = Tk()
            windo.title("Loan Calculator")
            windo.configure(bg='LightSteelBlue1')
            Label(windo, text="Loan Amount",bg='LightSteelBlue1').grid(row=1, column=1, sticky=W)
            Label(windo, text="Annual Interest Rate",bg='LightSteelBlue1').grid(row=2, column=1, sticky=W)
            Label(windo, text="Number of Years",bg='LightSteelBlue1').grid(row=3, column=1, sticky=W)
            Label(windo, text="Monthly Payment",bg='LightSteelBlue1').grid(row=4, column=1, sticky=W)
            Label(windo, text="Total Interest",bg='LightSteelBlue1').grid(row=5, column=1, sticky=W)
            Label(windo, text="Total Payment",bg='LightSteelBlue1').grid(row=6, column=1, sticky=W)

            self.loanAmountVar = StringVar()
            Entry(windo, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)

            self.annualInterestRateVar = StringVar()
            Entry(windo, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2)

            self.numberOfYearsVar = StringVar()
            Entry(windo, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2)

            self.monthlyPaymentVar = StringVar()
            lblMonthlyPayment = Label(windo, textvariable=self.monthlyPaymentVar,bg='LightSteelBlue1').grid(row=4, column=2, sticky=E)

            self.totalInterestVar = StringVar()
            lblTotalInterest = Label(windo, textvariable=self.totalInterestVar,bg='LightSteelBlue1').grid(row=5, column=2, sticky=E)

            self.totalPaymentVar = StringVar()
            lblTotalPayment = Label(windo, textvariable=self.totalPaymentVar,bg='LightSteelBlue1').grid(row=6, column=2, sticky=E)

            link = Label(windo, text="Link", fg="blue",bg='LightSteelBlue1')
            link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.calculator.net/loan-calculator.html"))
            link.grid(row=8, column=2, sticky=W + E)
            link.grid_columnconfigure(2, weight=0)

            def wExit():#To exit calculator
                wExit = tkinter.messagebox.askyesno("Loan Calculator", "Do you want to exit ?")
                if wExit > 0:
                    windo.destroy()
                    return

            btComputePayment = Button(windo, text="Compute Payment",command=self.computePayment,fg='blue',bg='Azure',relief=SUNKEN).grid(row=7, column=2, sticky=E)
            Button(windo, text="Exit", command=wExit,fg='blue',bg='Azure',relief=SUNKEN).grid(row=7, column=1, sticky=W)

        def computePayment(self):#To calcute and display desired value
            monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200, float(self.numberOfYearsVar.get()))

            self.monthlyPaymentVar.set(format(monthlyPayment, '10.3f'))
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 * float(self.numberOfYearsVar.get())

            self.totalPaymentVar.set(format(totalPayment, '10.3f'))
            totalInterest = float(self.totalPaymentVar.get()) - float(self.loanAmountVar.get())
            self.totalInterestVar.set(format(totalInterest, '10.3f'))

        def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):#To calculate monthly payment
            monthlyPayment = loanAmount * monthlyInterestRate / (1- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment

    LoanCalculator()

#Creating a frame
calc = Frame(window)
menubar = Menu(calc,background='blue', fg='white')
filemenu = Menu(menubar, tearoff=False, background='deep sky blue')

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label="Loan Calculator", command=Loan_Calc)
filemenu.add_command(label="ROI Calculator", command=ROI_Calc)
filemenu.add_command(label="Amortization Calculator", command=Amor_Calc)
filemenu.add_command(label="Future Value Calculator", command=Futu_Calc)
filemenu.add_command(label="Present Value Calculator", command=Pres_Calc)
filemenu.add_command(label="Salary Calculator", command=Sala_Calc)
filemenu.add_command(label="Inflation Calculator", command=Infl_Calc)
filemenu.add_command(label="Sales Tax Calculator", command=Sale_Calc)
filemenu.add_command(label="Discount Calculator", command=Disc_Calc)
filemenu.add_command(label="Profit Margin Calculator", command=Marg_Calc)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

window.config(menu=menubar)

window.mainloop()