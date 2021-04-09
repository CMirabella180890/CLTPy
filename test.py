# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:58:33 2021

@author: claum
 Definizione del problema utilizzato come esempio: 
     
     Laminato bilanciato simmetrico con la seguente sequenza: 
         [(0°/45°/-45°/90)s]
     Materiale delle singole lamine noto.   
     
 Scopo del codice: 
     
     Il codice si presuppone come obiettivo la costruzione di uno 
     strumento capace di calcolare tensioni e deformazioni nelle 
     singole lamine mediante gli strumenti della Teoria Classica 
     della Laminazione. 
     
 Estensioni future:
     
     Esso può essere modificato per prevedere 
     una logica modulare, capace di ospitare dati di ogni possibile
     materiale composito di interesse (mediante la definizione di
     opportune classi e/o moduli che raccolgano i dati).
"""
def pause():
    programPause = input("Press the <ENTER> key to continue...")
# =========================================================================
# DECLARATION
# In this section of the code all the relevant modules are loaded from the 
# file esercizio_laminato_mathcad.py and from the built-in Python libraries.
import numpy as np
from esercizio_laminato_mathcad import Q_matrix, rotation_matrix, psi_matrix
# =========================================================================
# INPUT DATA
# In this section we define all the appropriate variables to solve the problem.
# It is possible to obtain inputs from .json file in a successive version of 
# the program.
E11   = 125*1E9     # [Pa]
E22   = 12.5*1E9    # [Pa]
G12   = 6.8*1E9     # [Pa]
ni12  = 0.38
t_ply = 0.2                                        # Single ply thickness in [mm]
theta = np.array([0, 45, -45, 90, 90, -45, 45, 0]) # Orientations in [deg]
z_ply = np.array([t_ply*(-4), t_ply*(-3), t_ply*(-2),\
                  t_ply*(-1), 0, t_ply*(1), t_ply*(2),\
                      t_ply*(3), t_ply*(4)])       # Distances from midplane in [mm]
# Allocating empty lists to store all the evaluated matrices
Q_lam = [0, 0, 0, 0, 0, 0, 0, 0]
T     = [0, 0, 0, 0, 0, 0, 0, 0]
TT    = [0, 0, 0, 0, 0, 0, 0, 0]
# =========================================================================
# Q MATRIX ASSEMBLAGE
# =========================================================================
Object_Q = Q_matrix(E11, E22, ni12, G12)
Q        = Object_Q.Q # Q MATRIX IN [Pa]
# =========================================================================
# ROTATION MATRICES STORED INSIDE A LIST
# =========================================================================
j = 0
for i in range(len(theta)):
    print("\n Ply number: ", j)
    j     = j + 1
    x     = theta[i]
    y     = rotation_matrix(x)
    t     = y.T
    tt    = t.transpose()
    T[i]  = t
    TT[i] = tt
# =========================================================================
# PRINT ROTATION MATRICES IN A CONVENIENT WAY FOR CHECKING
# =========================================================================
# for i in range(len(T)): 
#     print("Ply oriented at: THETA = ", theta[i], " [deg]")
#     print("---------------------------\n")
#     print("T MATRIX")
#     print(T[i], "\n")
#     print("T TRANSPOSE MATRIX")
#     print(TT[i], "\n")   
# =========================================================================  
# CALCULATE Q MATRICES INSIDE THE LAMINATE PRINCIPAL REFERENCE FRAME
# ========================================================================= 
for i in range(len(Q_lam)):
    Q_lam[i] = np.dot(np.dot(T[i], Q), TT[i])
    print("\n Ply oriented at: THETA = ", theta[i], " [deg]")
    print(" ---------------------------")
    print(" CORRESPONDING Q MATRIX\n", " --------------------------- ")
    print(Q_lam[i], " in [Pa]\n")
# =========================================================================  
# CALCULATE A, B, D MATRICES
# =========================================================================
print(" **********************")
pause()
# =========================================================================
a = [0, 0, 0, 0, 0, 0, 0, 0] 
for i in range(len(Q_lam)):
    #q    = Q_lam[i]
    a[i] = np.dot(Q_lam[i], (z_ply[i+1] - z_ply[i]))
    print(" PARTIAL MATRIX TO BUILD A: ", i)
    print(" --------------------------- ")
    print(a[i], " in [Pa]*mm \n")       
A = sum(a)
A = A*(1E-3) 
for i in range(3):
    for j in range(3):
        if (abs(A[i][j])<1E-8): 
            A[i][j] = 0
print(" MATRIX A FOR THE LAMINATE: ") 
print(" --------------------------- \n", A, " in [Pa]*mm\n")
# =========================================================================
b = [0, 0, 0, 0, 0, 0, 0, 0] 
for i in range(len(Q_lam)):
    #q    = Q_lam[i]
    s1   = (z_ply[i+1])**2
    s0   = (z_ply[i])**2
    x    = (s1 - s0)
    b[i] = np.dot(Q_lam[i], x)
    b[i] = 0.5*b[i]*(1E-6)
    print(" PARTIAL MATRIX TO BUILD B: ", i)
    print(" --------------------------- ")
    print(b[i], " in [Pa]*(mm**2) \n")  
B = sum(b)
for i in range(3):
    for j in range(3):
        if (abs(B[i][j])<1E-9): 
            B[i][j] = 0
print(" MATRIX B FOR THE LAMINATE: ") 
print(" --------------------------- \n", B, " in [Pa]*(mm**2)\n")    
# =========================================================================
d = [0, 0, 0, 0, 0, 0, 0, 0] 
for i in range(len(Q_lam)):
    #q    = Q_lam[i]
    x    = (z_ply[i+1]**3 - z_ply[i]**3)
    d[i] = np.dot(Q_lam[i], x)
    print(" PARTIAL MATRIX TO BUILD D: ", i)
    print(" --------------------------- ")
    print(b[i], " in [Pa]*(mm**3) \n")     
D = (1/3)*sum(d)
D = D*(1E-9)
for i in range(3):
    for j in range(3):
        if (abs(A[i][j])<1E-8): 
            A[i][j] = 0
print(" MATRIX D FOR THE LAMINATE: ") 
print(" --------------------------- \n", D, " in [Pa]*(mm**3) \n")
# =========================================================================
print(" **********************")
pause()
# =========================================================================   
# =========================================================================  
# CALCULATE INVERSE A, B, D MATRICES
# =========================================================================
try:
    Ainv = np.linalg.inv(A)
    print(" INVERSE OF A FOR THE LAMINATE: ") 
    print(" --------------------------- \n", Ainv, " in [Pa**-1]*[mm**-1]\n")
except np.linalg.LinAlgError:
    s    = (3,3)
    Ainv = np.zeros(s)
    print(" *********************************************************** ")
    print(' A is a singular matrix and its inverse cannot be calculated.\n')
    print(" *********************************************************** ")
# =========================================================================  
try:
    Binv = np.linalg.inv(B)
    print(" INVERSE OF B FOR THE LAMINATE: ") 
    print(" --------------------------- \n", Binv, " in [Pa**-1]*[mm**-2]\n")
except np.linalg.LinAlgError:
    s    = (3,3)
    Binv = np.zeros(s)
    print(" *********************************************************** ")
    print('B is a singular matrix and its inverse cannot be calculated.\n')
    print(" *********************************************************** ")
# =========================================================================  
try:
    Dinv = np.linalg.inv(D)
    print(" INVERSE OF D FOR THE LAMINATE: ") 
    print(" --------------------------- \n", Dinv, " in [Pa**-1]*[mm**-3]\n")
except np.linalg.LinAlgError:
    s    = (3,3)
    Dinv = np.zeros(s)
    print(" *********************************************************** ")
    print('D is a singular matrix and its inverse cannot be calculated.\n')
    print(" *********************************************************** ")    
# =========================================================================  
# ENGINEERING PROPERTIES
# =========================================================================
# Change the code to have properly defined classes to implement these formulas.
Ex   = (1)/(8*t_ply*Ainv[0,0])
Ey   = (1)/(8*t_ply*Ainv[1,1])
Gxy  = (1)/(8*t_ply*Ainv[2,2])
nixy = (-Ainv[0,1])/(Ainv[0,0])
niyx = (-Ainv[1,0])/(Ainv[1,1])
print(" LAMINATE ENGINEERING PROPERTIES: ")
print(" --------------------------- ")
print("Ex   = ", "%.4E" % Ex)
print("Ey   = ", "%.4E" % Ey)
print("Gxy  = ", "%.4E" % Gxy)
print("nixy = ", nixy)
print("niyx = ", niyx)
print(" --------------------------- ")
# =========================================================================
print(" *** PRESS ENTER TO CONTINUE ***")
pause()
# =========================================================================
# =========================================================================  
# EXAMPLE CALCULATION
# =========================================================================
Loads = np.array([95000, 0, 0, 0, 0, 0]).reshape(-1,1) # N/mm
ab    = np.vstack((Ainv, Binv))
bd    = np.vstack((Binv, Dinv))
abd   = np.hstack((ab, bd))
print(" ---------------------------- ")
print(" ----- Block matrix abd ----- ")
np.set_printoptions(precision=3)
print(abd)
print(" ---------------------------- \n")
np.set_printoptions(precision=9)
eps   = abd @ Loads
epsilon = eps[0:3:1]
kappa   = eps[3:6:1]
print("\n EPSILON VECTOR:\n", " --------------------------- ")
print(" eps   =\n", epsilon)
print("\n CURVATURE VECTOR:\n", " --------------------------- ")
print(" kappa =\n", kappa)
# =========================================================================
print(" **********************")
pause()
# =========================================================================
# =========================================================================
# STRESS CALCULATIONS 
# =========================================================================
sigma_l = [0, 0, 0, 0, 0, 0, 0, 0] 
for i in range(len(Q_lam)):
    q        = Q_lam[i]
    sigma_l[i] = q @ epsilon
    print("\n ----- Tension ----- ")
    print(" Ply numer: ", i)
    print(" --------------------- ")
    print(" THETA = ", theta[i])
    print(" --------------------- ")
    print(" SIGMA = \n", sigma_l[i])
# =========================================================================
print(" **********************")
pause()
# =========================================================================
# =========================================================================
Psi     = [0, 0, 0, 0, 0, 0, 0, 0]
Psi_inv = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(theta)):
    print("\n Ply number: ", i)
    x          = theta[i]
    y          = psi_matrix(x)
    ppsi       = y.psi
    psiinv     = np.linalg.inv(ppsi)
    Psi[i]     = ppsi
    Psi_inv[i] = psiinv
# =========================================================================
# DEFORMATIONS
# =========================================================================
eps_l = [0, 0, 0, 0, 0, 0, 0, 0] 
for i in range(len(Q_lam)):
    z        = Psi_inv[i]
    eps_l[i] = z @ epsilon
    print("\n --- Deformation --- ")
    print(" Ply number: ", i)
    print(" --------------------- ")
    print(" THETA = ", theta[i])
    print(" --------------------- ")
    print(" EPSILON = \n", eps_l[i])    
# =========================================================================    
# =========================================================================
# =========================================================================
