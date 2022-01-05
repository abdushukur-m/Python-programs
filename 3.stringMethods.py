ism = 'Abdushukur'
familiya = 'Mukhiddinov'
ismFam=f"Salom, mening ismim {ism}. {ism} {familiya}." #f-string function

print('upper method', ismFam.upper()) #upper method
print('lower method', ismFam.lower()) #lower method
print('title method', ismFam.title()) #title method
print('Salom, mening ismim Abdushukur. Abdushukur Mukhiddinov'.title())
print('capitalize method', ismFam.capitalize()) #capitalize method
print('Salom, mening ismim Abdushukur. Abdushukur Mukhiddinov'.capitalize())

meva ='     olma     '
print('Men '+meva+"ni yaxshi ko'raman") 
print('Men '+meva.lstrip()+"ni yaxshi ko'raman") #lstrip method
print('Men '+meva.rstrip()+"ni yaxshi ko'raman") #rstrip method
print('Men '+meva.strip()+"ni yaxshi ko'raman") #strip method
meva=meva.strip()
print('Men '+meva+"ni yaxshi ko'raman") 
