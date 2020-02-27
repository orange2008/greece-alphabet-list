# coding=gbk
import os
import json
import time
local = {"alpha": 'Α α',"beta": 'Β β',"gamma": 'Γ γ',"delta": 'Δ δ',"epsilon": 'Ε ε',"zeta": 'Ζ ζ',"eta": 'Η η',"theta": 'Θ θ',"iota": 'Ι ι',"kappa": 'Κ κ',"lambda": '∧ λ',"mu": 'Μ μ',"nu": 'Ν ν',"xi": 'Ξ ξ',"omicron": 'Ο ο',"pi": '∏ π',"rho": 'Ρ ρ',"sigma": '∑ σ',"tau": 'Τ τ',"upsilon": 'Υ υ',"phi": 'Φ φ',"chi": 'Χ χ',"psi": 'Ψ ψ',"omega": 'Ω ω'}
for eng,alp in local.items():
    print("English: " + eng + "  AlphaBet: " + alp)

os.system("pause")
