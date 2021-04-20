# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:18:02 2021

@author: claum
"""
# ============================================================================
def inch2millimeter(x):
    return x*25.4
# ============================================================================
def pause():
    input("Enter to proceed...")
# ============================================================================
def fahrenheit2kelvin(x):
    """
    CONVERTS TEMPERATURES IN [F°] TO [K]
    Parameters
    ----------
        x : FLOAT
            Temperature in [F°].
    Returns
    -------
        FLOAT
            Temperature in [K].

    """
    return (x-32)*(5/9)+273.15
# ============================================================================
def psi2pascal(x):
    """
    CONVERTS PRESSURES IN [psi] TO [Pa]
    Parameters
    ----------
        x : FLOAT
            Pressure in [psi].
    Returns
    -------
        FLOAT
            Pressure in [Pa]
        
    """
    return x*6894.7572931783
# ============================================================================
import json 
from types import SimpleNamespace
import numpy as np
from collections import defaultdict
# =======================================
JSONFileName = "composites_data.json"
with open(JSONFileName, "r") as f:
    # ===================================
    # COMPOSITE MATERIALS DATABASE
    # ===================================
    composites_data = json.load(f)
# ===================================================
#   DEFINING AN OBJECT WITH ALL THE MATERIALS
# ===================================================    
materials_data    = SimpleNamespace(**composites_data)
materials_data_SI = {}
type(materials_data_SI)
name_mat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
prop_mat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(name_mat)):
    for key, value in composites_data.items():
        name_mat[i] = key
        prop_mat[i] = value
        print(" Testing name_mat: ", name_mat[i])
        materials_data_SI[name_mat[i]] = prop_mat[i]
# Object with all the properties to be converted in SI units
materials_data_SI = SimpleNamespace(**materials_data_SI)
print(" A new dictionary to fill with SI values: ", materials_data_SI)  
pause()
# Filling the new object with SI units
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.AS3501CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
pause()
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.AS43502CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.AS452503CarbonBismaleimide.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
for key, value in materials_data_SI.AS452503CarbonBismaleimide.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.AS4APC2CarbonPEEK.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.GY70934CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.GenericEGlassEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.GenericIM6Epoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.GenericKevlar149Epoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.GenericSGlassEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.IM6APC2CarbonPEEK.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.S2449SP381SGlassEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.T3005208CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.T300934CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
key   = 0
value = 0
conv  = 0
for key, value in materials_data_SI.T300976CarbonEpoxy.items():
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    if value["Unit"]=="psi":
        conv           = psi2pascal(value["Value"])
        value["Unit"]  = "Pa"
        value["Value"] = conv
        print(" Converted in SI: ", value["Value"], value["Unit"])
    elif value["Unit"]=="in/in":
        value["Unit"] = "mm/mm"
    elif value["Unit"]=="in/in/F":
        conv           = fahrenheit2kelvin(value["Value"])
        value["Unit"]  = "mm/mmm/K"
        value["Value"] = conv 
    print(" Converted properties: ")
    print(" Property: ", key)
    print(" Value: ", value["Value"], value["Unit"])
    materials_data_SI    
# ============================================================================
# MATERIALS LIBRARY
# ============================================================================
with open(JSONFileName, "r") as f:
    composites_data = json.load(f)
    materials_data  = SimpleNamespace(**composites_data)
class MATERIALS: 
    """
    Composite materials data:
        
        TENSILE_MODULUS_E1: Young modulus longitudinal to the fibers
        TENSILE_MODULUS_E2: Young modulus transverse to the fibers
        SHEAR_MODULUS_G12: Shear elastic modulus 
        POISSON_RATIO_V12: Poisson ratio 
        THERMAL_EXP_CTE1: Thermal expansion coeff. longitudinal to the fibers
        THERMAL_EXP_CTE2: Thermal expansion coeff. transverse to the fibers
        MOISTURE_EXP_CME1: Moisture expansion coeff. longitudinal to the fibers
        MOISTURE_EXP_CME2: Moisture expansion coeff. transverse to the fibers
        TENSILE_STRENGTH_XT: Tensile strength of the material longitudinal to 
                             the fibers
        COMPRESSIVE_STRENGHT_XC: Compressive strength of the material longitu-
                                 dinal to the fibers
        TENSILE_STRENGTH_YT: Tensile strength of the material transverse to 
                             the fibers
        COMPRESSIVE_STRENGHT_YC: Compressive strength of the material trans-
                                 verse to the fibers      
        SHEAR_STRENGTH_S: Shear strength of the material
        
    Unit of measures:    
        TENSILE_MODULUS_E1      --> [psi or Pa]
        TENSILE_MODULUS_E2      --> [psi or Pa]
        SHEAR_MODULUS_G12       --> [psi or Pa]
        POISSON_RATIO_V12       --> [Non dimensional]
        THERMAL_EXP_CTE1        --> [in/in/F or mm/mmm/K]
        THERMAL_EXP_CTE2        --> [in/in/F or mm/mmm/K]
        MOISTURE_EXP_CME1       --> [in/in or mm/mmm]
        MOISTURE_EXP_CME2       --> [in/in or mm/mmm]
        TENSILE_STRENGTH_XT     --> [psi or Pa]
        COMPRESSIVE_STRENGHT_XC --> [psi or Pa]
        TENSILE_STRENGTH_YT     --> [psi or Pa]
        COMPRESSIVE_STRENGHT_YC --> [psi or Pa]   
        SHEAR_STRENGTH_S        --> [psi or Pa]
        
    Calling materials: 
            AS_3501_CARBON_EPOXY          
            AS4_3501_6_CARBON_EPOXY      
            AS4_3502_CARBON_EXPOXY       
            AS4_52503_CARBON_BISMALEIMIDE 
            AS4_APC2_CARBON_PEEK          
            GY7_0934_CARBON_EPOXY         
            GENERIC_E_GLASS_EPOXY        
            GENERIC_IM6_EPOXY             
            GENERIC_KEVLAR_149_EPOXY     
            GENERIC_S_GLASS_EPOXY         
            IM6_APC2_CARBON_PEEK          
            S_2449_SP381_S_GLASS_EPOXY    
            T_300_5208_CARBON_EPOXY       
            T_300_934_CARBON_EPOXY       
            T_300_976_CARBON_EPOXY      
        
    """
    # ENGINEERING SYSTEM VALUES
    AS_3501_CARBON_EPOXY          = materials_data.AS3501CarbonEpoxy 
    AS4_3501_6_CARBON_EPOXY       = materials_data.AS435016CarbonEpoxy
    AS4_3502_CARBON_EXPOXY        = materials_data.AS43502CarbonEpoxy
    AS4_52503_CARBON_BISMALEIMIDE = materials_data.AS452503CarbonBismaleimide
    AS4_APC2_CARBON_PEEK          = materials_data.AS4APC2CarbonPEEK
    GY7_0934_CARBON_EPOXY         = materials_data.GY70934CarbonEpoxy
    GENERIC_E_GLASS_EPOXY         = materials_data.GenericEGlassEpoxy
    GENERIC_IM6_EPOXY             = materials_data.GenericIM6Epoxy
    GENERIC_KEVLAR_149_EPOXY      = materials_data.GenericKevlar149Epoxy
    GENERIC_S_GLASS_EPOXY         = materials_data.GenericSGlassEpoxy
    IM6_APC2_CARBON_PEEK          = materials_data.IM6APC2CarbonPEEK
    S_2449_SP381_S_GLASS_EPOXY    = materials_data.S2449SP381SGlassEpoxy
    T_300_5208_CARBON_EPOXY       = materials_data.T3005208CarbonEpoxy
    T_300_934_CARBON_EPOXY        = materials_data.T300934CarbonEpoxy
    T_300_976_CARBON_EPOXY        = materials_data.T300976CarbonEpoxy
    # INTERNATIONL SYSTEM VALUES
    SI_AS_3501_CARBON_EPOXY          = materials_data_SI.AS3501CarbonEpoxy 
    SI_AS4_3501_6_CARBON_EPOXY       = materials_data_SI.AS435016CarbonEpoxy 
    SI_AS4_3502_CARBON_EXPOXY        = materials_data_SI.AS43502CarbonEpoxy
    SI_AS4_52503_CARBON_BISMALEIMIDE = materials_data_SI.AS452503CarbonBismaleimide
    SI_AS4_APC2_CARBON_PEEK          = materials_data_SI.AS4APC2CarbonPEEK 
    SI_GY7_0934_CARBON_EPOXY         = materials_data_SI.GY70934CarbonEpoxy
    SI_GENERIC_E_GLASS_EPOXY         = materials_data_SI.GenericEGlassEpoxy
    SI_GENERIC_IM6_EPOXY             = materials_data_SI.GenericIM6Epoxy 
    SI_GENERIC_KEVLAR_149_EPOXY      = materials_data_SI.GenericKevlar149Epoxy
    SI_GENERIC_S_GLASS_EPOXY         = materials_data_SI.GenericSGlassEpoxy 
    SI_IM6_APC2_CARBON_PEEK          = materials_data_SI.IM6APC2CarbonPEEK
    SI_S_2449_SP381_S_GLASS_EPOXY    = materials_data_SI.S2449SP381SGlassEpoxy
    SI_T_300_5208_CARBON_EPOXY       = materials_data_SI.T3005208CarbonEpoxy
    SI_T_300_934_CARBON_EPOXY        = materials_data_SI.T300934CarbonEpoxy
    SI_T_300_976_CARBON_EPOXY        = materials_data_SI.T300976CarbonEpoxy
# ****************************************************************************
# CLASSICAL LAMINATION THEORY 
# ****************************************************************************
t_ply = {"Value":0.200,"Unit":"mm"}  # Single ply thickness in [mm]
theta = np.array([0.0, 45.0, -45.0, 90.0, 90.0, -45.0, 45.0, 0.0]) # Orientations in [deg]
# ****************************************************************************
class CLT(object):
    """
    CLASSICAL LAMINATION THEORY
    """
    def __init__(self, t_ply, lam_seq):
        """
        INITIALIZATION.

        Parameters
        ----------
        t_ply : DICT
              Must be defined as 
              t_ply = {"Value":value, "Unit":unit of measure}
              Acceptable units: [in] or [mm]
        lam_seq : LIST or ARRAY
              A lamination sequence properly defined. For instance:
                  np.array([0, 45, -45, 90, 90, -45, 45, 0])
        Returns
        -------
              Safety Margins of the laminate.

        """
        self.t_ply, self.lam_seq = t_ply, lam_seq
        # ===============================================================
        self.eng_mat = [
        MATERIALS.AS_3501_CARBON_EPOXY,          
        MATERIALS.AS4_3501_6_CARBON_EPOXY,      
        MATERIALS.AS4_3502_CARBON_EXPOXY,       
        MATERIALS.AS4_52503_CARBON_BISMALEIMIDE, 
        MATERIALS.AS4_APC2_CARBON_PEEK,          
        MATERIALS.GY7_0934_CARBON_EPOXY,         
        MATERIALS.GENERIC_E_GLASS_EPOXY,        
        MATERIALS.GENERIC_IM6_EPOXY,             
        MATERIALS.GENERIC_KEVLAR_149_EPOXY,     
        MATERIALS.GENERIC_S_GLASS_EPOXY,         
        MATERIALS.IM6_APC2_CARBON_PEEK,          
        MATERIALS.S_2449_SP381_S_GLASS_EPOXY,    
        MATERIALS.T_300_5208_CARBON_EPOXY,       
        MATERIALS.T_300_934_CARBON_EPOXY,       
        MATERIALS.T_300_976_CARBON_EPOXY 
        ]
        # ===============================================================
        self.si_mat = [
        MATERIALS.SI_AS_3501_CARBON_EPOXY,     
        MATERIALS.SI_AS4_3501_6_CARBON_EPOXY,        
        MATERIALS.SI_AS4_3502_CARBON_EXPOXY,        
        MATERIALS.SI_AS4_52503_CARBON_BISMALEIMIDE, 
        MATERIALS.SI_AS4_APC2_CARBON_PEEK,          
        MATERIALS.SI_GY7_0934_CARBON_EPOXY,         
        MATERIALS.SI_GENERIC_E_GLASS_EPOXY,         
        MATERIALS.SI_GENERIC_IM6_EPOXY,             
        MATERIALS.SI_GENERIC_KEVLAR_149_EPOXY,      
        MATERIALS.SI_GENERIC_S_GLASS_EPOXY,         
        MATERIALS.SI_IM6_APC2_CARBON_PEEK,          
        MATERIALS.SI_S_2449_SP381_S_GLASS_EPOXY,    
        MATERIALS.SI_T_300_5208_CARBON_EPOXY,       
        MATERIALS.SI_T_300_934_CARBON_EPOXY,        
        MATERIALS.SI_T_300_976_CARBON_EPOXY        
        ]
        # ===============================================================
        self.name = [ 
        "AS_3501_CARBON_EPOXY",          
        "AS4_3501_6_CARBON_EPOXY",      
        "AS4_3502_CARBON_EXPOXY",       
        "AS4_52503_CARBON_BISMALEIMIDE", 
        "AS4_APC2_CARBON_PEEK",          
        "GY7_0934_CARBON_EPOXY",         
        "GENERIC_E_GLASS_EPOXY",       
        "GENERIC_IM6_EPOXY",             
        "GENERIC_KEVLAR_149_EPOXY",     
        "GENERIC_S_GLASS_EPOXY"         
        "IM6_APC2_CARBON_PEEK",          
        "S_2449_SP381_S_GLASS_EPOXY",    
        "T_300_5208_CARBON_EPOXY",       
        "T_300_934_CARBON_EPOXY",       
        "T_300_976_CARBON_EPOXY" 
        ]
        # ===============================================================
        print(" *** SELECT A MATERIAL *** ")
        code     = 0
        for key in composites_data.items():
            print(" Material name: ", key[0])
        for i in range(len(self.name)):
            code = code + 1 
            print(" Code: ", code - 1)
        # ===============================================================    
        self.s = input(" Enter 0 for Engineering units or 1 for SI Units: ")
        s      = self.s 
        s      = int(s)
        if (t_ply["Unit"] == "mm" and s == 0):
            print(" Ply thickness is expressed in millimeters!")
            print(" You must select properties in SI units.")
            self.s = 1
        elif (t_ply["Unit"] == "in" and s == 1):
            print(" Ply thickness is expressed in inches!")
            print(" You must select properties in Engineering units.")
            self.s = 0
        self.c      = input(" Select the desidered material: ")
        # =============================================================== 
        self.mat       = self.mat_choose(self.s, self.c, self.si_mat,\
                                         self.eng_mat, self.name)
        self.show_prop = self.mat_show(self.mat)    
        self.z         = self.z_ply(t_ply, lam_seq)
        # ===============================================================  
        self.Q           = self.Q_matrix(self.mat)
        self.Tsig        = [0]*len(lam_seq)
        self.Tsig_transp = [0]*len(lam_seq)
        self.Teps        = [0]*len(lam_seq)
        self.Teps_transp = [0]*len(lam_seq)
        # ===============================================================
        for i in range(len(lam_seq)):
            # T SIGMA MATRIX
            self.Tsig[i]        = self.Tsigma_matrix(lam_seq[i])
            self.Tsig_transp[i] = self.Tsig[i].transpose()
            # T EPSILON MATRIX
            self.Teps[i]        = self.Teps_matrix(lam_seq[i])
            self.Teps_transp[i] = self.Teps[i].transpose()
        # ===============================================================  
        self.Qlam = [0]*len(lam_seq)
        for i in range(len(lam_seq)):
            self.Qlam[i] = self.Qlam_matrix(self.Q, self.Tsig[i],\
                                            self.Tsig_transp[i], lam_seq[i])
        # ===============================================================  
        self.A = self.A_matrix(self.Qlam, self.z, t_ply)        
        self.B = self.B_matrix(self.Qlam, self.z, t_ply)  
        self.D = self.D_matrix(self.Qlam, self.z, t_ply)
        # =========================================================================  
        # CALCULATE INVERSE A, B, D MATRICES
        # =========================================================================
        try:
            self.Ainv = np.linalg.inv(self.A["Value"])
            self.a    = {"Value":self.Ainv, "Unit":"("+self.A["Unit"]+")"+"^-1"}
            print(" INVERSE OF A FOR THE LAMINATE: ")
            print(" --------------------------- \n", self.a["Value"], " in ",\
                  self.a["Unit"])
        except np.linalg.LinAlgError:
            s    = (3,3)
            self.Ainv = np.zeros(s)
            self.a    = {"Value":self.Ainv, "Unit":"("+self.A["Unit"]+")"+"^-1"}
            print("\n *********************************************************** ")
            print(' A IS A SINGULAR MATRIX AND ITS INVERSE CANNOT BE CALCULATED.\n')
            print(" *********************************************************** \n")
        # =========================================================================
        try:
            self.Binv = np.linalg.inv(self.B["Value"])
            self.b    = {"Value":self.Binv, "Unit":"("+self.B["Unit"]+")"+"^-1"}
            print(" INVERSE OF B FOR THE LAMINATE: ")
            print(" --------------------------- \n", self.b["Value"], " in ",\
                  self.b["Unit"])
        except np.linalg.LinAlgError:
            s    = (3,3)
            self.Binv = np.zeros(s)
            self.b    = {"Value":self.Binv, "Unit":"("+self.B["Unit"]+")"+"^-1"}
            print("\n *********************************************************** ")
            print('B IS A SINGULAR MATRIX AND ITS INVERSE CANNOT BE CALCULATED.\n')
            print(" *********************************************************** \n")
        # =========================================================================
        try:
            self.Dinv = np.linalg.inv(self.D["Value"])
            self.d    = {"Value":self.Dinv, "Unit":"("+self.D["Unit"]+")"+"^-1"}
            print(" INVERSE OF D FOR THE LAMINATE: ")
            print(" --------------------------- \n", self.d["Value"], " in ",\
                  self.d["Unit"])
        except np.linalg.LinAlgError:
            s    = (3,3)
            self.Dinv = np.zeros(s)
            self.d    = {"Value":self.Dinv, "Unit":"("+self.D["Unit"]+")"+"^-1"}
            print("\n *********************************************************** ")
            print('D IS A SINGULAR MATRIX AND ITS INVERSE CANNOT BE CALCULATED.\n')
            print(" *********************************************************** \n")
        pause()
        # =========================================================================
        self.load      = np.zeros((6,1))
        self.load_dict = [0]*len(self.load)
        for i in range(len(self.load)):
            print("STORING LOAD IN: ", i)
            if (i<3 and t_ply["Unit"] == "mm"):
                self.load[i] = input("AXIAL LOAD (N/mm): ")
                self.load_dict[i] = {"Value":self.load[i], "Unit":"N*mm^-1"}
            elif (i<3 and t_ply["Unit"] == "in"):
                self.load[i] = input("AXIAL LOAD (lbf/in): ")
                self.load_dict[i] = {"Value":self.load[i], "Unit":"lbf*in^-1"}
            elif (i>=3 and t_ply["Unit"] == "mm"): 
                self.load[i] = input("FLEXURAL LOAD (N): ")
                self.load_dict[i] = {"Value":self.load[i], "Unit":"N"}
            elif (i>=3 and t_ply["Unit"] == "in"): 
                self.load[i] = input("FLEXURAL LOAD (lbf): ")
                self.load_dict[i] = {"Value":self.load[i], "Unit":"lbf"}
        # =========================================================================  
        # cALCULATIONS RELATED TO STRESS AND STRAIN IN THE PRINCIPAL PLANE
        # =========================================================================
        ab       = np.vstack((self.a["Value"], self.b["Value"]))
        bd       = np.vstack((self.b["Value"], self.d["Value"]))
        self.abd = np.hstack((ab, bd))
        print(" ---------------------------- ")
        print(" ----- BLOCK MATRIX abd ----- ")
        np.set_printoptions(precision=3)
        print(self.abd)
        print(" ---------------------------- \n")
        np.set_printoptions(precision=9)
        self.eps   = self.abd @ self.load
        self.epsilon = self.eps[0:3:1]
        self.kappa   = self.eps[3:6:1]
        self.kappa_dict = {"Value":self.kappa, "Unit":t_ply["Unit"]+"^-1"}
        print("\n EPSILON VECTOR:\n", " --------------------------- ")
        print(" eps   =\n", self.epsilon)
        print("\n CURVATURE VECTOR:\n", " --------------------------- ")
        print(" kappa =\n", self.kappa)
        self.eps_i = [0]*len(self.Qlam)
        for i in range(len(self.eps_i)):
            self.eps_i[i] = self.epsilon + self.kappa*(self.z[i]+self.z[i+1])
            print(" **** LOCAL STRAIN PLY ", i, " **** ")
            print(" eps_i = \n", self.eps_i[i])
            print(" ********************************** ")
        # =========================================================================
        self.sigma_laminate = self.stress_laminate(self.Qlam, t_ply,\
                                                   self.epsilon, lam_seq)
        self.sigma_lamina   = self.stress_lamina(self.Tsig,\
                                                 self.sigma_laminate, lam_seq)
        self.strain_lamina  = self.strain_lamina(self.Teps, self.epsilon,\
                                                 lam_seq)
        self.Margin_of_Safety_Max_Stress = self.max_stress_crit(self.mat,\
                                                     self.sigma_lamina, lam_seq)
        self.Margin_of_Safety_Max_Strain = self.max_strain_crit(self.mat,\
                                                     self.strain_lamina, lam_seq)
        self.Margin_of_Safety_Tsai_Hill  = self.tsai_hill(self.mat,\
                                                     self.sigma_lamina, lam_seq)    
# ============================================================================        
    def mat_choose(self, s, code, si_mat, eng_mat, name):
        """
        A function to select the material.

        Parameters
        ----------
        switch : INT
            switch = 0 --> Engineering units
            switch = 1 --> SI units
        code : INT
            An integer from 0 to 14 to select material.
        si_mat : DICTIONARY
            Materials properties in SI Units. 
        eng_mat : DICTIONARY
            Materials properties in engineering units.
        name : LIST
            Name of materials.
        Returns
        -------
        mat : FLOAT
            Selected material.

        """
        mat  = {}
        s    = int(s)
        code = int(code)
        if s == 0:
            x      = name[code]
            x      = str(x)
            print(x)
            y      = dict(eng_mat[code])
            mat[x] = y
        elif s == 1:
            z      = name[code]
            z      = str(z)
            k      = dict(si_mat[code])
            mat[z] = k
        # =======================================    
        return mat
# ============================================================================
    def mat_show(self, mat):
        """
        A function to show chosen material properties.

        Parameters
        ----------
        mat : DICT
            Materials of the ply which will be used.

        Returns
        -------
        Print the materials properties inside the terminal.

        """
        print("\n *** PROPERTIES *** ")
        print(" ****************** ")
        for key in mat.items():
            print(" Selected material: ", key[0])
            print(" ****************** ")
            for prop, value in key[1].items():
                print(" ", prop, " = ", value["Value"], value["Unit"])
# ============================================================================
    def z_ply(self, t_ply, lam_seq):
        """
        CALCULATES PLY DISTANCES FROM MIDPLANE

        Parameters
        ----------
        t_ply : DICT
            A dictionary which contains the single ply thickness and the
            corresponding unit of measures.
        lam_seq : LIST or ARRAY
            Lamination sequence stored inside an array.

        Returns
        -------
        z_ply : ARRAY
            Array which contains distances from midplane

        """
        thick = t_ply["Value"]
        l     = len(lam_seq)
        l     = int(l)
        h     = np.linspace(-l//2, l//2, l+1)
        z_ply = np.zeros(len(h))
        # =======================================
        for i in range(len(h)):
            z_ply[i] = thick*h[i]
        # =======================================
        print(" \n Plies distances from the plate midplane:")
        print(" z_ply = \n", z_ply)
         # =======================================   
        return z_ply   
# ============================================================================
    def Q_matrix(self, mat):
        x = {} 
        for key in mat.items():
            for prop, value in key[1].items():
                x[prop] = value
        # =======================================
        E11  = x["TensileModulusE1"]["Value"]
        E22  = x["TensileModulusE2"]["Value"]
        ni12 = x["PoissonRatiov12"]["Value"]
        G12  = x["ShearModulusG12"]["Value"]
        # =======================================        
        Q00 = E11/(1 - (ni12**2)*(E22/E11))
        Q11 = E22/(1 - (ni12**2)*(E22/E11))
        Q01 = (ni12*E22)/(1 - (ni12**2)*(E22/E11))
        Q22 = G12
        # =======================================
        q = np.array([[Q00, Q01, 0.0],
                      [Q01, Q11, 0.0],
                      [0.0, 0.0, Q22]])
        Q = {"Value":q, "Unit":x["TensileModulusE1"]["Unit"]}
        # =======================================
        print("\n *********************** \n", " Q - matrix ")
        print(" *********************** \n", " Q = ")
        print(Q["Value"], " in ", Q["Unit"])
        # =======================================
        return Q
# ============================================================================
    def Tsigma_matrix(self, theta): 
        theta_rad = np.deg2rad(theta)
        m         = np.cos(theta_rad)
        n         = np.sin(theta_rad)
        s         = (3,3)
        Tsigma    = np.zeros(s)
        Tsigma[0,0] = m**2
        Tsigma[0,1] = n**2
        Tsigma[0,2] = 2*m*n
        Tsigma[1,0] = n**2
        Tsigma[1,1] = m**2
        Tsigma[1,2] = -2*m*n
        Tsigma[2,0] = -m*n
        Tsigma[2,1] = m*n
        Tsigma[2,2] = m**2 - n**2
		# =======================================
        tol = 1.0E-9
        Tsigma[np.abs(Tsigma) < tol] = 0.0
        # =======================================
        # =======================================
        print("\n *********************** \n", " T_sigma - matrix ")
        print( " THETA = ", theta, " [deg]")
        print(" *********************** \n", " T_sigma = ")
        print(Tsigma)
        # =======================================
        return Tsigma
# ============================================================================
    def Teps_matrix(self, theta): 
        theta_rad = np.deg2rad(theta)
        m         = np.cos(theta_rad)
        n         = np.sin(theta_rad)
        s         = (3,3)
        Teps    = np.zeros(s)
        Teps[0,0] = m**2
        Teps[0,1] = n**2
        Teps[0,2] = -m*n
        Teps[1,0] = n**2
        Teps[1,1] = m**2
        Teps[1,2] = m*n
        Teps[2,0] = 2*m*n
        Teps[2,1] = -2*m*n
        Teps[2,2] = m**2 - n**2
		# =======================================
        tol = 1.0E-9
        Teps[np.abs(Teps) < tol] = 0.0
        # =======================================
        # =======================================
        print("\n *********************** \n", " T_epsilon - matrix ")
        print( " THETA = ", theta, " [deg]")
        print(" *********************** \n", " T_epsilon = ")
        print(Teps)
        # =======================================
        return Teps  
# =========================================================================
    def Qlam_matrix(self, Q, Tsig, Tsig_transp, theta):  
        Q_l  = np.dot(np.dot(Tsig, Q["Value"]), Tsig_transp)
        Q_u  = Q["Unit"]
        Qlam = {"Value":Q_l, "Unit":Q_u}
        print("\n Ply oriented at: THETA = ", theta, " [deg]")
        print(" ---------------------------")
        print(" CORRESPONDING Q MATRIX\n", " --------------------------- ")
        print(Qlam["Value"], " in ", Qlam["Unit"])      
        return Qlam
# =========================================================================
    def A_matrix(self, Qlam, z_ply, t_ply):
        a = [0]*len(Qlam)
        for i in range(len(Qlam)):
            a[i] = np.dot(Qlam[i]["Value"], (z_ply[i+1] - z_ply[i]))
            print(" PARTIAL MATRIX TO BUILD A: ", i)
            print(" --------------------------- ")
            print(a[i], " in ", Qlam[i]["Unit"]+"*"+t_ply["Unit"])       
        A = sum(a)
        A = A*(1E-3) 
        for i in range(3):
            for j in range(3):
                if (abs(A[i][j])<1E-8): 
                    A[i][j] = 0
        Alam = {"Value":A, "Unit":Qlam[0]["Unit"]+"*"+t_ply["Unit"]}
        print(" **************************** ")
        print("\n MATRIX A FOR THE LAMINATE: ") 
        print(" ---------------------------")
        print("A = ", Alam["Value"], " in ", Alam["Unit"], "\n")
        return Alam
# =========================================================================
    def B_matrix(self, Qlam, z_ply, t_ply):
        b = [0]*len(Qlam)
        for i in range(len(Qlam)):
            s1   = (z_ply[i+1])**2
            s0   = (z_ply[i])**2
            x    = (s1 - s0)
            b[i] = np.dot(Qlam[i]["Value"], x)
            b[i] = 0.5*b[i]*(1E-6)
            print(" PARTIAL MATRIX TO BUILD B: ", i)
            print(" --------------------------- ")
            print(b[i], " in ", Qlam[0]["Unit"]+"*"+t_ply["Unit"]+"^2") 
        B = sum(b)
        for i in range(3):
            for j in range(3):
                if (abs(B[i][j])<1E-9): 
                    B[i][j] = 0
        Blam = {"Value":B, "Unit":Qlam[0]["Unit"]+"*"+t_ply["Unit"]+"^2"}
        print(" **************************** ")
        print("\n MATRIX B FOR THE LAMINATE: ") 
        print(" ---------------------------")
        print("B = ", Blam["Value"], " in ", Blam["Unit"], "\n")
        return Blam
# =========================================================================
    def D_matrix(self, Qlam, z_ply, t_ply):
        d = [0]*len(Qlam)
        for i in range(len(Qlam)):
            s1   = (z_ply[i+1])**3
            s0   = (z_ply[i])**3
            x    = (s1 - s0)
            d[i] = np.dot(Qlam[i]["Value"], x)
            print(" PARTIAL MATRIX TO BUILD D: ", i)
            print(" --------------------------- ")
            print(d[i], " in ", Qlam[0]["Unit"]+"*"+t_ply["Unit"]+"^3") 
        D = (1/3)*sum(d)
        D = D*(1E-9)
        for i in range(3):
            for j in range(3):
                if (abs(D[i][j])<1E-9): 
                    D[i][j] = 0
        Dlam = {"Value":D, "Unit":Qlam[0]["Unit"]+"*"+t_ply["Unit"]+"^3"}
        print(" **************************** ")
        print("\n MATRIX D FOR THE LAMINATE: ") 
        print(" ---------------------------")
        print("D = ", Dlam["Value"], " in ", Dlam["Unit"], "\n")
        return Dlam
# =========================================================================
    def stress_laminate(self, Qlam, t_ply, epsilon, lam_seq):
        sigma_lam  = [0]*len(Qlam)
        sigma_dict = {}
        for i in range(len(Qlam)):
            theta        = lam_seq[i]
            sigma_lam[i] = Qlam[i]["Value"] @ epsilon
            sigma_dict   = {"Value":sigma_lam[i], "Unit":Qlam[0]["Unit"]}
            print("\n ----- LAMINATE STRESS ----- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            print(" --------------------- ")
            print(" SIGMA LAMINATE = \n", sigma_dict["Value"], sigma_dict["Unit"])
            sigma_lam[i] = sigma_dict
            
        return sigma_lam
# =========================================================================
    def stress_lamina(self, Tsig, sigma_lam, lam_seq):
        stress_lam  = [0]*len(lam_seq)
        stress_dict = {}
        for i in range(len(lam_seq)):
            theta        = lam_seq[i]
            Tsig_inv     = np.linalg.inv(Tsig[i])
            stress_lam[i] = Tsig_inv @ sigma_lam[i]["Value"]
            stress_dict   = {"Value":stress_lam[i], "Unit":sigma_lam[i]["Unit"]}
            print("\n ----- LAMINA STRESS ----- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            print(" --------------------- ")
            print(" SIGMA LAMINA = \n", stress_dict["Value"], stress_dict["Unit"])
            stress_lam[i] = stress_dict
            
        return stress_lam
# =========================================================================
    def strain_lamina(self, Teps, epsilon, lam_seq):
        strain_lam  = [0]*len(lam_seq)
        strain_dict = {}
        for i in range(len(lam_seq)):
            theta        = lam_seq[i]
            Teps_inv     = np.linalg.inv(Teps[i])
            strain_lam[i] = Teps_inv @ epsilon
            strain_dict   = {"Value":strain_lam[i], "Unit":"Non-dim."}
            print("\n ----- LAMINA STRAIN ----- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            print(" --------------------- ")
            print(" EPSILON LAMINA = \n", strain_dict["Value"], strain_dict["Unit"])
            strain_lam[i] = strain_dict
            
        return strain_lam   
# =========================================================================
    def max_stress_crit(self, mat, tension_lamina, lam_seq):
        print("\n *** PROPERTIES *** ")
        print(" ****************** ")
        for key in mat.items():
            print(" Selected material: ", key[0])
            print(" ****************** ")
            for prop, value in key[1].items():
                if (prop == "TensileStrengthXt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUT = value["Value"]
                if (prop == "CompressiveStrengthXc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUC = value["Value"]
                if (prop == "TensileStrengthYt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUT = value["Value"]
                if (prop == "CompressiveStrengthYc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUC = value["Value"]
                if (prop == "ShearStrengthS"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    tau_U = value["Value"]
                    
        theta  = 0 
        stress = 0
        mos    = np.array([0.0, 0.0, 0.0])
        MS     = [0]*len(lam_seq)
        for i in range(len(lam_seq)):
            theta = lam_seq[i]
            print("\n --------------------- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            stress = tension_lamina[i].values()
            stress = list(stress)
            stress = stress[0]
            for j in range(len(stress)):  
                # X DIRECTION
                if (stress[j]>=0 and j == 0):
                    print("\n **** TENSILE STRESS 1 **** ")
                    if (stress[j]>=sigma_xUT):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", stress[j], " > ", sigma_xUT)
                        print(" TENSILE STRESS IS GREATER THAN ALLOWABLE ")
                    elif (stress[j]<sigma_xUT):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ TENSILE RESIDUAL STRENGTH ++++ ")
                        ms1 = ((sigma_xUT)/(stress[j])) - 1
                        print(" M. S. = ", ms1)
                        mos[j] = ms1
                elif (stress[j]<0 and j == 0):
                    print("\n **** COMPRESSIVE STRESS 1 **** ")
                    if (abs(stress[j])>=abs(sigma_xUC)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", abs(stress[j]), " > ",\
                              abs(sigma_xUC))
                        print(" COMPRESSIVE STRESS IS GREATER THAN ALLOWABLE ")
                    elif (abs(stress[j])<abs(sigma_xUC)):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ COMPRESSIVE RESIDUAL STRENGTH ++++ ")
                        ms1 = (abs(sigma_xUC)/abs(stress[j])) - 1
                        print(" M. S. = ", ms1)
                        mos[j] = ms1
                elif (stress[j] == 0 and j == 0):
                    print("\n ++++ NO STRESS ALONG 1 ++++")
                # Y DIRECTION          
                if (stress[j]>=0 and j == 1):
                    print("\n **** TENSILE STRESS 2 **** ")
                    if (stress[j]>=sigma_yUT):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", stress[j], " > ", sigma_yUT)
                        print(" TENSILE STRESS IS GREATER THAN ALLOWABLE ")
                    elif (stress[j]<sigma_yUT):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ TENSILE RESIDUAL STRENGTH ++++ ")
                        ms2 = (sigma_yUT/stress[j]) - 1
                        print(" M. S. = ", ms2)
                        mos[j] = ms2
                elif (stress[j]<0 and j == 1):
                    print("\n **** COMPRESSIVE STRESS 2 **** ")
                    if (abs(stress[j])>=abs(sigma_yUC)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", abs(stress[j]), " > ",\
                              abs(sigma_yUT))
                        print(" COMPRESSIVE STRESS IS GREATER THAN ALLOWABLE ")
                    elif (abs(stress[j])<abs(sigma_yUC)):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ COMPRESSIVE RESIDUAL STRENGTH ++++ ")
                        ms2 = (abs(sigma_yUC)/abs(stress[j])) - 1
                        print(" M. S. = ", ms2)
                        mos[j] = ms2
                elif (stress[j] == 0 and j == 1):
                    print("\n ++++ NO STRESS ALONG 2 ++++")                        
                # SHEAR   
                if (stress[j] == 0 and j == 2):
                    print("\n ++++ NO STRESS IN SHEAR ++++")        
                elif (stress[j] != 0 and j == 2):
                    print("\n **** SHEAR STRESS **** ")
                    if (abs(stress[j])>=abs(tau_U)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", stress[j], " > ", tau_U)
                        print(" SHEAR STRESS IS GREATER THAN ALLOWABLE ")
                    elif (stress[j]<tau_U):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ SHEAR RESIDUAL STRENGTH ++++ ")
                        mss = (abs(tau_U)/abs(stress[j])) - 1
                        print(" M. S. = ", mss)
                        mos[j] = mss                        
            # FILLING A LIST WITH M. S. VECTORS
            MS[i] = mos 
            mos   = np.array([0.0, 0.0, 0.0])
            ms1   = 0.0 
            ms2   = 0.0 
            mss   = 0.0
            
        return MS
# =========================================================================
    def max_strain_crit(self, mat, deformation_lamina, lam_seq):
        print("\n *** PROPERTIES *** ")
        print(" ****************** ")
        for key in mat.items():
            print(" Selected material: ", key[0])
            print(" ****************** ")
            for prop, value in key[1].items():
                if (prop == "TensileModulusE1"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    E1 = value["Value"]
                if (prop == "TensileModulusE2"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    E2 = value["Value"]
                if (prop == "ShearModulusG12"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    G12 = value["Value"]
                if (prop == "PoissonRatiov12"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    ni12 = value["Value"]
                if (prop == "TensileStrengthXt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUT = value["Value"]
                if (prop == "CompressiveStrengthXc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUC = value["Value"]
                if (prop == "TensileStrengthYt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUT = value["Value"]
                if (prop == "CompressiveStrengthYc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUC = value["Value"]
                if (prop == "ShearStrengthS"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    tau_U = value["Value"]
        # ALLOWABLES
        eps1UT = sigma_xUT/E1
        eps1UC = sigma_xUC/E1
        eps2UT = sigma_yUT/E2
        eps2UC = sigma_yUC/E2
        gam_6  = tau_U/G12
        # CALCULATIONS            
        theta  = 0 
        strain = 0
        mos    = np.array([0.0, 0.0, 0.0])
        MS     = [0]*len(lam_seq)
        for i in range(len(lam_seq)):
            theta = lam_seq[i]
            print("\n --------------------- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            strain = deformation_lamina[i].values()
            strain = list(strain)
            strain = strain[0] 
            for j in range(len(strain)):  
                # X DIRECTION
                if (strain[j]>=0 and j == 0):
                    print("\n **** TENSILE STRAIN 1 **** ")
                    if (strain[j]>=eps1UT):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", strain[j], " > ", eps1UT)
                        print(" TENSILE STRAIN IS GREATER THAN ALLOWABLE ")
                    elif (strain[j]<eps1UT):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ TENSILE RESIDUAL STRENGTH ++++ ")
                        ms1 = (eps1UT/strain[j]) - 1
                        print(" M. S. = ", ms1)
                        mos[j] = ms1
                elif (strain[j]<0 and j == 0):
                    print("\n **** COMPRESSIVE STRAIN 1 **** ")
                    if (abs(strain[j])>=abs(eps1UC)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", abs(strain[j]), " > ",\
                              abs(eps1UC))
                        print(" COMPRESSIVE STRAIN IS GREATER THAN ALLOWABLE ")
                    elif (abs(strain[j])<abs(eps1UC)):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ COMPRESSIVE RESIDUAL STRENGTH ++++ ")
                        ms1 = (abs(eps1UC)/abs(strain[j])) - 1
                        print(" M. S. = ", ms1)
                        mos[j] = ms1
                elif (strain[j] == 0 and j == 0):
                    print("\n ++++ NO STRESS ALONG 1 ++++")
                # Y DIRECTION          
                if (strain[j]>=0 and j == 1):
                    print("\n **** TENSILE STRAIN 2 **** ")
                    if (strain[j]>=eps2UT):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", strain[j], " > ", eps2UT)
                        print(" TENSILE STRAIN IS GREATER THAN ALLOWABLE ")
                    elif (strain[j]<eps2UT):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ TENSILE RESIDUAL STRENGTH ++++ ")
                        ms2 = (eps2UT/strain[j]) - 1
                        print(" M. S. = ", ms2)
                        mos[j] = ms2
                elif (strain[j]<0 and j == 1):
                    print("\n **** COMPRESSIVE STRAIN 2 **** ")
                    if (abs(strain[j])>=abs(eps2UC)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", abs(strain[j]), " > ",\
                              abs(eps2UC))
                        print(" COMPRESSIVE STRAIN IS GREATER THAN ALLOWABLE ")
                    elif (abs(strain[j])<abs(eps2UC)):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ COMPRESSIVE RESIDUAL STRENGTH ++++ ")
                        ms2 = (abs(eps2UC)/abs(strain[j])) - 1
                        print(" M. S. = ", ms2)
                        mos[j] = ms2
                elif (strain[j] == 0 and j == 1):
                    print("\n ++++ NO STRESS ALONG 2 ++++")                        
                # SHEAR   
                if (strain[j] == 0 and j == 2):
                    print("\n ++++ NO STRESS IN SHEAR ++++")        
                elif (strain[j] != 0 and j == 2):
                    print("\n **** SHEAR STRESS **** ")
                    if (abs(strain[j])>=abs(gam_6)):
                        print(" ++++ FAILURE! ++++ ")
                        print(" ", strain[j], " > ", gam_6)
                        print(" SHEAR STRESS IS GREATER THAN ALLOWABLE ")
                    elif (abs(strain[j])<abs(gam_6)):
                        print(" ++++ MARGIN OF SAFETY ++++ ")
                        print(" ++++ SHEAR RESIDUAL STRENGTH ++++ ")
                        mss = (abs(gam_6)/abs(strain[j])) - 1
                        print(" M. S. = ", mss)
                        mos[j] = mss                        
            # FILLING A LIST WITH M. S. VECTORS
            MS[i] = mos 
            mos   = np.array([0.0, 0.0, 0.0])
            strain = 0
            ms1   = 0.0 
            ms2   = 0.0 
            mss   = 0.0
            
        return MS    
# =========================================================================
    def tsai_hill(self, mat, tension_lamina, lam_seq):
        print("\n *** PROPERTIES *** ")
        print(" ****************** ")
        for key in mat.items():
            print(" Selected material: ", key[0])
            print(" ****************** ")
            for prop, value in key[1].items():
                if (prop == "TensileStrengthXt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUT = value["Value"]
                if (prop == "CompressiveStrengthXc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_xUC = value["Value"]
                if (prop == "TensileStrengthYt"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUT = value["Value"]
                if (prop == "CompressiveStrengthYc"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    sigma_yUC = value["Value"]
                if (prop == "ShearStrengthS"):
                    print(" ", prop, " = ", value["Value"], value["Unit"])
                    tau_U = value["Value"]
                    
        # TENSILE COEFFICIENTS
        AT = 1/(sigma_xUT**2)
        BT = 1/(sigma_yUT**2)
        D  = 1/(tau_U**2)
        # TENSILE COEFFICIENTS
        AC = 1/(sigma_xUC**2)
        BC = 1/(sigma_yUC**2)
        D  = 1/(tau_U**2)
        stress = 0
        mos    = 0.0
        MS     = [0]*len(lam_seq)
        for i in range(len(lam_seq)):
            theta = lam_seq[i]
            print("\n --------------------- ")
            print(" PLY NUMBER: ", i)
            print(" --------------------- ")
            print(" THETA = ", theta)
            stress = tension_lamina[i].values()
            stress = list(stress)
            stress = stress[0]            
            for j in range(len(stress)):  
                # C COEFFICIENT
                if (j==0):
                    if(stress[j]>=0):
                        C  = 1/(sigma_xUT**2)
                        xy = stress[j]*stress[j+1]
                        c  = xy*C
                    elif (stress[j]<0):
                        C  = 1/(sigma_xUC**2)
                        xy = stress[j]*stress[j+1]
                        c  = xy*C
                    elif (stress[j]==0):
                        c  = 0
                # X DIRECTION
                if (stress[j]>=0 and j == 0):
                    print("\n **** TENSILE STRESS 1 **** ")
                    x = stress[j]**2
                    a = x*AT
                elif (stress[j]<0 and j == 0):
                    print("\n **** COMPRESSIVE STRESS 1 **** ")
                    x = stress[j]**2
                    a = x*AC
                elif (stress[j] == 0 and j == 0):
                    print("\n ++++ NO STRESS ALONG 1 ++++")
                    a = 0
                # Y DIRECTION          
                if (stress[j]>=0 and j == 1):
                    print("\n **** TENSILE STRESS 2 **** ")
                    y = stress[j]**2
                    b = y*BT
                elif (stress[j]<0 and j == 1):
                    print("\n **** COMPRESSIVE STRESS 2 **** ")
                    y = stress[j]**2
                    b = y*BC
                elif (stress[j] == 0 and j == 1):
                    print("\n ++++ NO STRESS ALONG 2 ++++")  
                    b = 0   
                # SHEAR   
                if (stress[j] == 0 and j == 2):
                    print("\n ++++ NO STRESS IN SHEAR ++++") 
                    d = 0
                elif (stress[j] != 0 and j == 2):
                    print("\n **** SHEAR STRESS **** ")
                    z = stress[j]**2
                    d = z*D  
            # FILLING A LIST WITH M. S. VECTORS
            mos   = a + b - c + d - 1
            print(" ++++ MARGIN OF SAFETY ++++ ")
            print(" M. S. = ", mos)
            MS[i] = mos 
            mos   = 0.0
            a, b, c, d = 0.0, 0.0, 0.0, 0.0
            
        return MS
