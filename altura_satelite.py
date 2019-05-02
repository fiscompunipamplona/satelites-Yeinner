G=6.67e-11
mt=5.97e24
Rt=6371e3
pi=3.1416
print("Segundo punto")
T=float(input("entre el periodo T: "))
h=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("La altura en km es:",h*(1e-3))
print("Tercer punto")
T=5400
h=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("La altura del satelite con un periodo de 90 min en km es:",h*(1e-3))
T=2700
h=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("La altura del satelite con un periodo de 45 min en km es:",h*(1e-3))
T=86400
h=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("La altura del satelite con un periodo de un día en km es:",h*(1e-3))
print("Cuarto punto")
T_1=86148
h_1=(((G*mt*T_1**2)/(4*pi**2))**(1/3))-Rt
print("La diferencia de alturas de un día geosincrónico con un día sideral en km es:",(h-h_1)*(1e-3))                                 
