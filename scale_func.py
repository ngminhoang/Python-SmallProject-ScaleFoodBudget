import pandas as pd
import io
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import array as arr

def scale(calo,pro,fat,satfat,fiber,carb):
    data = pd.read_csv('D:/DỮ LIỆU THAY Ổ CỨNG LẦN 2/DESTOP/Python/nutrients_csvfile.csv')
# tách label và cách thông số
    data0 = data.iloc[:,2:9].values
    data1 = data.iloc[:,0].values
    data2 = data.iloc[:,2].values
    number = 335

# các bước bên dưới là chuẩn hóa kiểu dữ liệu phải đưa vào pyomo là dạng dictionary
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
            b[i+1,j+1] = a[i][j] # bộ tham số b chưa dữ liệu dinh dưỡng từ data đã được chuẩn hóa về dạng dictionary

# tạo model
    model= pyo.ConcreteModel()
    model.i = pyo.RangeSet(1,number) # tạo rangeset từ 1 -> 335 đại diện cho 335 loại thực phẩm
    model.j = pyo.RangeSet(1,7) # tạo rangeset từ 1 -> 7 đại diện cho 7 loại dinh dưỡng
    model.p = pyo.Param( model.i,model.j,initialize = b) # áp bộ tham số b đã chuẩn hóa vào mô hình
    p = model.p
    model.x=pyo.Var(model.i,within=pyo.NonNegativeReals) # tạo 335 biến x
    model.Obj = pyo.Objective(rule = objf, sense = pyo.minimize) #hàm cần tối ưu
    model.Const2=pyo.Constraint(rule = cs2(model,calo)) # các hàm ràng buộc
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
    optm = SolverFactory('glpk')#,executable='C:/Users/Admin/Downloads/glpsol')
    optm.solve(model) # thực hiện tối hưu
    for i in range(0,number):
        food = model.x[i+1]()*float(data2[i]);
        if (food > 0.0):
            print(data1[i],': ',food)
    print('Sum of weight: ',model.Obj())

def objf(model): # hàm obj
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