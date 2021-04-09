# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:38:00 2021

@author: claum
"""
import numpy as np
# =========================================================================
class Q_matrix(object):
    """
    A class to automatically fill the Q matrix with all the appropriate 
    values of composite lamina elastic properties.
    """
    def __init__(self, E11, E22, ni12, G12):
        """
        Inizialization of class Q_matrix.

        Parameters
        ----------
        E11 : FLOAT
            Young Modulus longitudinal to the fibers in [GPa].
        E22 : FLOAT
            Young Modulus transverse to the fibers in [GPa].
        ni12 : FLOAT
            Poisson ratio.
        G12 : FLOAT
            Shear Modulus in [GPa].

        Returns
        -------
        The Q matrix properly filled.

        """
        self.E11, self.E22, self.ni12, self.G12 = E11, E22, ni12, G12
        # =================================================================
        self.Q11 = E11/(1 - (ni12**2)*(E22/E11))
        self.Q22 = E22/(1 - (ni12**2)*(E22/E11))
        self.Q12 = (ni12*E22)/(1 - (ni12**2)*(E22/E11))
        self.Q66 = G12
        self.Q   = self.fill_matrix(self.Q11, self.Q22, self.Q12, self.Q66)
        print("Assemblage of Q matrix for the selected ply.\n", " ---------------\n")
        print(" Q MATRIX IN [Pa]")
        print(" ---------------\n", self.Q, " in [Pa]")
        print(" ---------------\n")
        # =================================================================        
    def fill_matrix(self, Q11, Q22, Q12, Q66):
        s      = (3,3)
        Q      = np.zeros(s)
        Q[0,0] = Q11
        Q[1,1] = Q22
        Q[0,1] = Q12
        Q[1,0] = Q12
        Q[2,2] = Q66
        return Q
# =========================================================================    
class rotation_matrix(object):
    def __init__(self, theta):
        self.theta       = theta
        self.theta_rad   = np.deg2rad(theta)
        self.m           = np.cos(self.theta_rad)
        self.n           = np.sin(self.theta_rad)
        self.T           = self.fill_rot_matrix(self.m, self.n)
        self.T_transpose = self.T.transpose()
        print(" --------------- Rotation matrix T --------------- ")
        print(" --------------- Ply oriented at: THETA = ",theta, "[deg]")
        print(" T MATRIX")
        print(" ---------------\n", self.T)
        print(" ---------------")
        print("TRANSPOSED T MATRIX")
        print(" ---------------\n", self.T_transpose)
        print(" ---------------")
        # =================================================================
    def fill_rot_matrix(self, m, n):
        s      = (3,3)
        T      = np.zeros(s)
        T[0,0] = m**2
        T[0,1] = n**2
        T[0,2] = -2*m*n
        T[1,0] = n**2
        T[1,1] = m**2
        T[1,2] = 2*m*n
        T[2,0] = m*n
        T[2,1] = -m*n
        T[2,2] = m**2 - n**2
        tol = 1e-9
        T[np.abs(T) < tol] = 0
        return T
# =========================================================================    
class psi_matrix(object):
    def __init__(self, theta):
        self.theta       = theta
        self.theta_rad   = np.deg2rad(theta)
        self.m           = np.cos(self.theta_rad)
        self.n           = np.sin(self.theta_rad)
        self.psi           = self.fill_psi_matrix(self.m, self.n)
        self.psi_transpose = self.psi.transpose()
        print(" --------------- Rotation matrix PSI --------------- ")
        print(" --------------- Ply oriented at: THETA = ",theta, "[deg]")
        print(" PSI MATRIX")
        print(" ---------------\n", self.psi)
        print(" ---------------")
        print("TRANSPOSED PSI MATRIX")
        print(" ---------------\n", self.psi_transpose)
        print(" ---------------")
        # =================================================================
    def fill_psi_matrix(self, m, n):
        s      = (3,3)
        PSI    = np.zeros(s)
        PSI[0,0] = m**2
        PSI[0,1] = n**2
        PSI[0,2] = -m*n
        PSI[1,0] = n**2
        PSI[1,1] = m**2
        PSI[1,2] = m*n
        PSI[2,0] = 2*m*n
        PSI[2,1] = -2*m*n
        PSI[2,2] = m**2 - n**2
        tol = 1e-9
        PSI[np.abs(PSI) < tol] = 0
        return PSI     
# =========================================================================     
