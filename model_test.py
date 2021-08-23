import joblib
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

scaler=joblib.load('scaler.pkl')
model=joblib.load('airfoil_noise_model.pkl')

#function that gives prediction about noise for naca 0012 airfoil.
def airfoil_noise(a,b,c,d,e,):
    inp={'frequency':a,'aoa':b,'chord_l':c,'velocity':d,'displacement_thick':e}
    temp=pd.DataFrame(inp,index=[1])
    scale_temp=scaler.transform(temp)
    result=model.predict(scale_temp)
    return f'NACA 0012 Airfoil Noise level :{result}dB'

#in function 'airfoil_noise()' we can pass the parametrs in following order:
#1. Frequency 
#2. Angle of Attack at which the airfoil is placed.
#3. chord length in meters.
#4. Freestream velocity of the air or the medium.
#5. Displacement Thickness created by airfoil boundry layer.

a=float(input('Frequency in Heartz: '))
b=float(input('Angle Of Attack in Degree: '))
c=float(input('Chord Length in Meters: '))
d=float(input('Free-Stream Velocity in Meters: '))
e=float(input('Displacement Thickness:  '))

airfoil_noise(a,b,c,d,e)