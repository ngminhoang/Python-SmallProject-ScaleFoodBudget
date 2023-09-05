#!pip install pyomo
#!apt-get install -y -qq glpk-utils
#from google.colab import drive
#drive.mount("/content/gdrive")
#from google.colab import files
import pandas as pd
from pyomo import *
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
#from glpk import *

def objfprice(model): # hàm obj
  return sum(model.p[i,8]*model.x[i] for i in model.i)
def objfweight(model): # hàm obj
  return sum(model.p[i,1]*model.x[i] for i in model.i) 
def cs2(model,x): # hàm constraint 
  return sum(model.p[i,2]*model.x[i] for i in model.i) >=x 
def cs3(model,x): # hàm constraint 
  return sum(model.p[i,3]*model.x[i] for i in model.i) >=x
def cs4(model,x): # hàm constraint 
  return sum(model.p[i,4]*model.x[i] for i in model.i) >=x
def cs5(model,x): # hàm constraint 
  return sum(model.p[i,5]*model.x[i] for i in model.i) >=x
def cs6(model,x): # hàm constraint 
  return sum(model.p[i,6]*model.x[i] for i in model.i) >=x
def cs7(model,x): # hàm constraint 
  return sum(model.p[i,7]*model.x[i] for i in model.i) >=x
def cs8(model,x): # hàm constraint 
  return sum(model.p[i,2]*model.x[i] for i in model.i) <=x+100
def cs9(model,x): # hàm constraint 
  return sum(model.p[i,3]*model.x[i] for i in model.i) <=x+30
def cs10(model,x): # hàm constraint 
  return sum(model.p[i,4]*model.x[i] for i in model.i) <=x+30
def cs11(model,x): # hàm constraint 
  return sum(model.p[i,5]*model.x[i] for i in model.i) <=x+30
def cs12(model,x): # hàm constraint 
  return sum(model.p[i,6]*model.x[i] for i in model.i) <=x+30
def cs13(model,x): # hàm constraint 
  return sum(model.p[i,7]*model.x[i] for i in model.i) <=x+30

def scale(calo,pro,fat,satfat,fiber,carb):
  data = pd.read_csv("./nutrients_csvfile.csv")

  data0 = data.iloc[:,2:9].values
  data1 = data.iloc[:,0].values
  data2 = data.iloc[:,2].values
  number = 335
  a=[]
  for i in range(0,number): 
        a.append(data0[i])
  for i in range(0,number): 
        a[i]= list(a[i])     
  for i in range(0,number):
    for j in range (0,7):
        a[i][j] = float(a[i][j])    
  b = {}
  for i in range(0,number): 
    for j in range (0,7):
      b[i+1,j+1] = a[i][j]
  model= pyo.ConcreteModel() 
  model.i = pyo.RangeSet(1,number) # tạo rangeset 
  model.j = pyo.RangeSet(1,7) 
  model.p = pyo.Param( model.i,model.j,initialize = b) 
  p = model.p
  model.x=pyo.Var(model.i,within=pyo.NonNegativeReals)
  model.Obj = pyo.Objective(rule = objfweight, sense = pyo.minimize)
  model.Const2=pyo.Constraint(rule = cs2(model,calo))
  model.Const3=pyo.Constraint(rule = cs3(model,pro))
  model.Const4=pyo.Constraint(rule = cs4(model,fat))
  model.Const5=pyo.Constraint(rule = cs5(model,satfat))
  model.Const6=pyo.Constraint(rule = cs6(model,fiber))
  model.Const7=pyo.Constraint(rule = cs7(model,carb))
  model.Const8=pyo.Constraint(rule = cs8(model,calo))
  model.Const9=pyo.Constraint(rule = cs9(model,pro))
  model.Const10=pyo.Constraint(rule = cs10(model,fat))
  model.Const11=pyo.Constraint(rule = cs11(model,fiber))
  model.Const12=pyo.Constraint(rule = cs12(model,satfat))
  model.Const13=pyo.Constraint(rule = cs13(model,carb))
  optm = SolverFactory('glpk')
  result = optm.solve(model)
  return model
  #ff = model.Obj()
  #fff = str()
  #for i in range(0,number):
  #  food = model.x[i+1]()*float(data2[i])
  #  if (food > 0.0):
  #    print(data1[i],': ' + str(food))
  #    fff+=str(data1[i]) + ': ' + str(food)
  #print('Sum of weight: ',model.Obj())
  #fff+='Sum of weight: '+ str(ff)
  #return fff
  #return ff
def scaleprice(calo,pro,fat,satfat,fiber,carb):
  data = pd.read_csv("./nutrients_csvfile.csv")

  data0 = data.iloc[:,2:10].values
  data1 = data.iloc[:,0].values
  data2 = data.iloc[:,9].values
  number = 335
  a=[]
  for i in range(0,number):
        a.append(data0[i])
  for i in range(0,number):
        a[i]= list(a[i])
  for i in range(0,number):
    for j in range (0,8):
        a[i][j] = float(a[i][j])
  b = {}
  for i in range(0,number):
    for j in range (0,8):
      b[i+1,j+1] = a[i][j]
  model= pyo.ConcreteModel()
  model.i = pyo.RangeSet(1,number) # tạo rangeset
  model.j = pyo.RangeSet(1,8)
  model.p = pyo.Param( model.i,model.j,initialize = b)
  p = model.p
  model.x=pyo.Var(model.i,within=pyo.NonNegativeReals)
  model.Obj = pyo.Objective(rule = objfprice, sense = pyo.minimize)
  model.Const2=pyo.Constraint(rule = cs2(model,calo))
  model.Const3=pyo.Constraint(rule = cs3(model,pro))
  model.Const4=pyo.Constraint(rule = cs4(model,fat))
  model.Const5=pyo.Constraint(rule = cs5(model,satfat))
  model.Const6=pyo.Constraint(rule = cs6(model,fiber))
  model.Const7=pyo.Constraint(rule = cs7(model,carb))
  model.Const8=pyo.Constraint(rule = cs8(model,calo))
  model.Const9=pyo.Constraint(rule = cs9(model,pro))
  model.Const10=pyo.Constraint(rule = cs10(model,fat))
  model.Const11=pyo.Constraint(rule = cs11(model,fiber))
  model.Const12=pyo.Constraint(rule = cs12(model,satfat))
  model.Const13=pyo.Constraint(rule = cs13(model,carb))
  optm = SolverFactory('glpk')
  result = optm.solve(model)
  return model


#print(scale(2000,200,200,200,200,200).x[1]())