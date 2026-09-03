# covert distant given in feet and inches into meter and centimeter.
feet = float(input('enter feet:'))
inch = float(input('enter inch:'))
meter = (feet *0.3048) + (inch * 0.0254)
centimeter = meter * 100

print('meter =',meter)
print('centimeter =', centimeter)

