from tkinter import *
from math import *
import string

root = Tk()  

#Function to calculate everything
def enter_click(event): 
      global SabCow, SabBull, BuffBull, BuffCow, RoanCow, RoanBull, Six_Months, One_Year, Two_Year, Three_Year, Big
      
      M1_int = float(M1.get())
      M2_int = float(M2.get())
      M3_int = float(M3.get())
      M4_int = float(M4.get())
      M5_int = float(M5.get())
      F1_int = float(F1.get())
      F2_int = float(F2.get())
      F3_int = float(F3.get())
      F4_int = float(F4.get())
      F5_int = float(F5.get())
      
      if A.get() == 1 :
            f1_weight = F1_int * ((SabCow * 25)/Six_Months)
            f2_weight = F2_int * ((SabCow * 40)/One_Year) 
            f3_weight = F3_int * ((SabCow * 70)/Two_Year)
            f4_weight = F4_int * ((SabCow * 85)/Three_Year)
            f5_weight = F5_int * SabCow
            m1_weight = M1_int * ((SabBull * 25)/Six_Months)
            m2_weight = M2_int * ((SabBull * 40)/One_Year)
            m3_weight = M3_int * ((SabBull * 70)/Two_Year)
            m4_weight = M4_int * ((SabBull * 85)/Three_Year)
            m5_weight = M5_int * SabBull            
              
            Weight_Female = f1_weight + f2_weight + f3_weight + f4_weight + f5_weight
            Weight_Male = m1_weight + m2_weight + m3_weight + m4_weight + m5_weight
            Total_Weight = Weight_Female + Weight_Male
            Total_Food = Total_Weight * Big
            water_needed = (F2_int + F3_int + F4_int + F5_int + M2_int + M3_int + M4_int + M5_int) * 9
            animal = "Sable"  
            result_text = "Animal: " + str(animal) + "\nTotal Food Requierd: " + str(Total_Food) + "KG \nTotal Weight: " + str(Total_Weight) + "KG \nWater Requierd Daily: " + str(water_needed) + " L"
            o =Label(root, text=result_text, justify=LEFT, padx=5, pady=10).grid(row=7)
            print(result_text)
      
      elif A.get() == 2 :
            f1_weight = F1_int * ((BuffCow * 25)/Six_Months)
            f2_weight = F2_int * ((BuffCow * 40)/One_Year)
            f3_weight = F3_int * ((BuffCow * 70)/Two_Year)
            f4_weight = F4_int * ((BuffCow * 85)/Three_Year)
            f5_weight = F5_int * SabCow
            m1_weight = M1_int * ((BuffBull * 25)/Six_Months)
            m2_weight = M2_int * ((BuffBull * 40)/One_Year)
            m3_weight = M3_int * ((BuffBull * 70)/Two_Year)
            m4_weight = M4_int * ((BuffBull * 85)/Three_Year)
            m5_weight = M5_int * BuffBull              
              
            Weight_Female = f1_weight + f2_weight + f3_weight + f4_weight + f5_weight
            Weight_Male = m1_weight + m2_weight + m3_weight + m4_weight + m5_weight
            Total_Weight = Weight_Female + Weight_Male
            Total_Food = Total_Weight * Big
            water_needed = (F2_int + F3_int + F4_int + F5_int + M2_int + M3_int + M4_int + M5_int) * 30
            animal = "Buffalo"
            result_text = "Animal: " + str(animal) + "\nTotal Food Requierd: " + str(Total_Food) + " KG \nTotal Weight: " + str(Total_Weight) + " KG \nWater Requierd Daily: " + str(water_needed) + " L"
            o =Label(root, text=result_text, justify=LEFT, padx=5, pady=10).grid(row=7)
            print(result_text)          
      
              
      elif A.get() == 3 :
            f1_weight = F1_int * ((RoanCow * 25)/Six_Months)
            f2_weight = F2_int * ((RoanCow * 40)/One_Year)
            f3_weight = F3_int * ((RoanCow * 70)/Two_Year)
            f4_weight = F4_int * ((RoanCow * 85)/Three_Year)
            f5_weight = F5_int * RoanCow
            m1_weight = M1_int * ((RoanBull * 25)/Six_Months)
            m2_weight = M2_int * ((RoanBull * 40)/One_Year)
            m3_weight = M3_int * ((RoanBull * 70)/Two_Year)
            m4_weight = M4_int * ((RoanBull * 85)/Three_Year)
            m5_weight = M5_int * RoanBull
              
            Weight_Female = f1_weight + f2_weight + f3_weight + f4_weight + f5_weight 
            Weight_Male = m1_weight + m2_weight + m3_weight + m4_weight + m5_weight
            Total_Weight = Weight_Female + Weight_Male
            Total_Food = Total_Weight * Big
            water_needed = (F2_int + F3_int + F4_int + F5_int + M2_int + M3_int + M4_int + M5_int) * 10
            animal = "Roan"
            result_text = "Animal: " + str(animal) + "\nTotal Food Requierd: " + str(Total_Food) + "KG \nTotal Weight: " + str(Total_Weight) + "KG \nWater Requierd Daily: " + str(water_needed) + " L"
            o = Label(root, text=result_text, justify=LEFT, padx=5, pady=10).grid(row=7)
            print(result_text)          


animal = StringVar()

water_needed = float()

#Animal Weight
BuffBull = 750
BuffCow = 650
SabBull = 230
SabCow = 210
RoanBull = 270
RoanCow = 240

#Animal Ages to Weight

Six_Months = 125
One_Year = 140
Two_Year = 170
Three_Year = 185
  
#Percentage Food

Big = 2/102
Small = 5/105

#Tkinter
A = IntVar()
A.set(1)
result_text = StringVar()

f1_weight = DoubleVar()
f2_weight = DoubleVar()
f3_weight = DoubleVar()
f4_weight = DoubleVar()
f5_weight = DoubleVar()
m1_weight = DoubleVar()
m2_weight = DoubleVar()
m3_weight = DoubleVar()
m4_weight = DoubleVar()
m5_weight = DoubleVar()

#GUI

w =Label(root, text="Choose an Animal:", justify=LEFT, padx=5, pady=10).grid(row=0)

Label(root, text="Age", padx=5, pady=20).grid(row=0, column=2)
Label(root, text="M", padx=5, pady=20).grid(row=0, column=3)
Label(root, text="F", padx=5, pady=20).grid(row=0, column=4)

Radiobutton(root, text="Sable", padx=20, variable=A, value=1).grid(row=1)
Radiobutton(root, text="Buffalo", padx=20, variable=A, value=2).grid(row=2)
Radiobutton(root, text="Roan", padx=20, variable=A, value=3).grid(row=3)


Label(root, text="6 Months :").grid(row=1, column=2)
Label(root, text="1 Year :").grid(row=2, column=2)
Label(root, text="2 Years :").grid(row=3, column=2)
Label(root, text="3 Years :").grid(row=4, column=2)
Label(root, text="4 Years :").grid(row=5, column=2)

M1 = Entry(root)
M2 = Entry(root)
M3 = Entry(root)
M4 = Entry(root)
M5 = Entry(root)
F1 = Entry(root)
F2 = Entry(root)
F3 = Entry(root)
F4 = Entry(root)
F5 = Entry(root)

M1.grid(row=1, column=3)
M2.grid(row=2, column=3)
M3.grid(row=3, column=3)
M4.grid(row=4, column=3)
M5.grid(row=5, column=3)
F1.grid(row=1, column=4)
F2.grid(row=2, column=4)
F3.grid(row=3, column=4)
F4.grid(row=4, column=4)
F5.grid(row=5, column=4)

M1.insert(10,"0")   
M2.insert(10,"0")   
M3.insert(10,"0")   
M4.insert(10,"0")   
M5.insert(10,"0")   
F1.insert(10,"0")     
F2.insert(10,"0")   
F3.insert(10,"0")   
F4.insert(10,"0")   
F5.insert(10,"0")   
#Calculation button and event
  
enter_button=Button(root, text="Enter")
enter_button.grid(row=6)
enter_button.bind("<Enter>",enter_click)
enter_button.bind("<Return>",enter_click)

root.mainloop()

