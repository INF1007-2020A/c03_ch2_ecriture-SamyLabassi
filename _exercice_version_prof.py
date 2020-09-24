#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	puissance = (voltage ** 2) / resistance
	return puissance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	produit_scalaire = 0
	for index in range(len(v1)):
		produit_scalaire = produit_scalaire + (v1[index] * v2[index])

	if produit_scalaire == 0:
		return False
	else:
		return True

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	
	if len(values) != 0:
		denom = 0 
		somme = 0
		for v in values:
			if v >= 0:
				somme = somme + v
				denom += 1
		if denom == 0 :
			print('Aucune valeur positive dans la liste')
			return False
		else:
			moyenne = somme / denom
			return moyenne # La variable v contient une valeur de la liste.
	else:
		print('La liste est vide')

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		
		#if value >= 20:
		#	billet20 = (value / 20)
		#	billet10 = (((billets20 % 1) * 20)/10)
		#	billet5 = (((billets10 % 1) * 10)/5)
		#	billet1 = billets5 % 1) *5
		#	pass
		#elif value >= 10:
		#	pass
		#elif value >= 5:
		#	pass
		#elif value >= 1:
		#	pass

		billet20 = 0
		billet10 = 0
		billet5 = 0
		billet1 = 0
		while value >= 20:
			value -= 20
			billet20 += 1

		while value >= 10:
			value -= 10
			billet10 += 1

		while value >= 5:
			value -= 5
			billet5 +=1	
		while value >= 1:
			value -= 1
			billet1 += 1


	return (billet20, billet10, billet5, billet1);

if __name__ == "__main__":
	#print(dissipated_power(69, 420))
	#print(orthogonal((1, 1), (-1, 1)))
	#print(average([1, 4, -2, 10]))
	print(bills(137))
