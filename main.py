joueurs = {}
nombre_joueurs = input("Combien de joueurs ? \n> ")
nbr_jr = int(nombre_joueurs)

for i in range(nbr_jr):
  j = i + 1
  k = input(f"Quel est le nom du joueur {j} ? \n> ")
  joueurs[j] = {"nom":k}

table_joueurs = {}
table_joueurs[0] = joueurs[nbr_jr]
table_joueurs.update(joueurs)
table_joueurs[nbr_jr+1] = joueurs[1]

print("\n**********\nFin du premier âge")
for i, j in joueurs.items():
  k = input("Combien d'armées a {} ?\n> ".format(j["nom"]))
  j["age_un"] = int(k)

for i in range(1,nbr_jr+1):
  print("\nCalcul du score de {}...".format(table_joueurs[i]["nom"]))
  combat_un = table_joueurs[i]["age_un"] - table_joueurs[i-1]["age_un"]
  combat_deux = table_joueurs[i]["age_un"] - table_joueurs[i+1]["age_un"]
  total = combat_un + combat_deux
  print(f"A la fin du premier âge, le score a bougé de {total}")
  joueurs[i]["score_un"] = total

print("\n**********\nFin du deuxième âge")
for i, j in joueurs.items():
  k = input("Combien d'armées a {} ?\n> ".format(j["nom"]))
  j["age_deux"] = int(k)

for i in range(1,nbr_jr+1):
  print("\nCalcul du score de {}...".format(table_joueurs[i]["nom"]))
  combat_un = table_joueurs[i]["age_deux"] - table_joueurs[i-1]["age_deux"]
  if combat_un > 0:
    combat_un *= 3
  combat_deux = table_joueurs[i]["age_deux"] - table_joueurs[i+1]["age_deux"]
  if combat_deux > 0:
    combat_deux *= 3
  total = combat_un + combat_deux
  print(f"A la fin du deuxième âge, le score a bougé de {total}")
  joueurs[i]["score_deux"] = total

print("\n**********\nFin du troisième âge")
for i, j in joueurs.items():
  k = input("Combien d'armées a {} ?\n> ".format(j["nom"]))
  j["age_trois"] = int(k)

for i in range(1,nbr_jr+1):
  print("\nCalcul du score de {}...".format(table_joueurs[i]["nom"]))
  combat_un = table_joueurs[i]["age_trois"] - table_joueurs[i-1]["age_trois"]
  if combat_un > 0:
    combat_un *= 5
  combat_deux = table_joueurs[i]["age_trois"] - table_joueurs[i+1]["age_trois"]
  if combat_deux > 0:
    combat_deux *= 5
  total = combat_un + combat_deux
  print(f"A la fin du troisième âge, le score a bougé de {total}")
  joueurs[i]["score_trois"] = total

print("\n*********\nPartie finie")
for i in range(1, nbr_jr+1):
  print("\nVoici le bilan pour {} :".format(joueurs[i]["nom"]))
  print("Points après le premier âge : {}".format(joueurs[i]["score_un"]))
  print("Points après le deuxième âge : {}".format(joueurs[i]["score_deux"]))
  print("Points après le troisième âge : {}".format(joueurs[i]["score_trois"]))
  total = joueurs[i]["score_un"] + joueurs[i]["score_deux"] + joueurs[i]["score_trois"]
  print("Total des points dûs aux combats : {}".format(total))