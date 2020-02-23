# QUESTION 1


import math
depth = 1500 # in metres
Porosity = 20 #percent
Hydraulic_Conductivity = 410 #m/d
Organic_Content = 2 #percent
Bulk_Density = 1680 #kg/m^3
partitionceofficient = 10**2.61 #10^2.61 (k)

# a) Trichloroethelene falls under the DNAPLS category of NAPLS

# b) I expect to find gravel and sand because porosity is 20%

# c)
Hydraulic_Gradient = 5*10**(-4)
#Darcy's Law Q = kA(dh/dl)
#q = k(dh/dl)
# v = k H 1/n
k = Hydraulic_Conductivity
H = Hydraulic_Gradient
n = Porosity/100
v = k*H/n
Actual_Pore_velocity = v #m/d
print('Actual pore velocity: '+str(v))
#v = 1.025 #m/d

#d) Darcy Velocity = q = KH

q = k*H
print("Darcy Velocity:"+str(q))
#q = 0.205 m/d

#e)

#Retardation factor = R =  v/vp
# R = 1 +(pb)/n*ks
# pb = dry bulk density (kg/m^3 * 1 m^3/1000L* 1000000mg/kg)
pb = Bulk_Density *1/1000*1000000
foc = Organic_Content/100
kow = partitionceofficient
ks = 6.3*10**(-7)*foc*kow
Retardation_Factor = 1 + pb/n*ks
print('Retardation: '+ str(Retardation_Factor))
#Retardation:44.117

#f)

R = Retardation_Factor
vp = v/R
print("ActualVelocity " + str(vp))
#vp = 0.02323 m/d
# X = 0.02323 m/d * 365d/yr*2yrs
X = vp*365*2
print("Distance in 2 years "+str(X))
# X = 16.96 m

#g)

Pumping_rate = 0.2 #m^3/s
Q = Pumping_rate
width = 30
w = width
Y = w/2
pi = math.pi
B = 1500
# q = 0.205 m^3/d * 1 day/24hrs * 1 hr/60 mins * 1 min/60s
q = q*1/24*1/60*1/60
print('Darcy Velocity in m^3/s '+str(q))
# angle = tan^-1(Y/x)
#Y = Q/(2qB)*(1-angle/pi)
#Y*2*q*B/Q = (1-angle/pi)
#1 - Y*2*q*B/Q = angle/pi
#pi(1 - Y*2*q*B/Q) = angle
angle = pi*(1-Y*2*q*B/Q)
print('plume angle: ' +str(angle))
#tan(angle) = Y/X
# X = Y*tan(angle)
X = Y*math.tan(angle)
print(" Therefore the extraction should be done " + str(X) + " m in front of the plume")
#Therefore the extraction should be done 140.504 m in front of the plume

# Q. 2.

"""
a)
Environmental Benefits:
The organic waste can be sent to a different processing plant to be used as fertilizer 
Waste can be avoided by reusing organic waste on farms  so less fertilizer production is required


Economic Benefits:

Land can be used for commercial purposes instead of a landfill
Organic waste can be sold as fertilizer

Social Benefits:

Land can be used for residential or recreation purposes
Increases social awareness of environmental issues
Allows people to be more environmentally conscious by easily discarding organic waste

All information taken from lecture notes by Dr. Kinsley
b)
Ideas to improve compost/recycling rates
- A city can hand out flyers to display what goes where 
- Processing plastic bags (https://www.cbc.ca/news/canada/ottawa/ottawa-plastic-compost-rules-1.5192375)
- Adding compost and recycling to education curriculum
- Making child-friendly recycling flyers
- Having info sessions for people to ask questions about recycling

c) According to CBC news plastic bags are filtered out of the compost. 
https://www.cbc.ca/news/canada/ottawa/ottawa-plastic-compost-rules-1.5192375

d) Waste collected in bluebins are processed by the Ottawa Valley waste recovery centre at 900 Woito Station Rd, Pembroke, ON K8A 6W5.
The material in blue-bins sorted into different categories by hand or by machine. The material is then compacted and baled
to be sold to companies that can use these materials
https://ovwrc.com/recycling-facility/

"""
#Q. 3
# a)
Flowrate = 150000 #cfm
Concentration = 5.5 #gr/ft^3 cement PM
MaxOutlet = 0.02 #gr/ft^3
Spacing = 10 #in
V = 17000 #V
particle_size = 2 #um
dielectric_C = 5.5
k = dielectric_C
E = V * 1/1000* 1/(10/2)
P = 3*k/(k+2)
d = particle_size
#DriftVelocity = w = 8.42*10^(-3)*E^2*d*p
w = 8.42*10**(-3)*E**2*d*P
print('Drift Velocity '+str(w))

# b)

# n = (pmin - pmout)/pmin
n = (5.5-0.02)/5.5
Q = Flowrate*1/60 # convert from ft/min to ft/s
# n = 1 - exp(-Aw/Q)
#A = -Q/W * ln(1-n)
A = -Q/w*math.log(1-n)
print("Plate Area "+str(A))
#C)
Aperplate = 40*30
A2 = Aperplate
PlatesRequired = A/A2
print("PlatesRequired "+str(PlatesRequired))
