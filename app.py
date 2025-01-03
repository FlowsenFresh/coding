player_life = 100
monster_life = 20
player_attack = 10
monster_attack = 3

while player_life > 0 and monster_life > 0:
  choice = input('Gib A für Attacke oder L für Laufen ein: ')
  if choice == 'A':
    monster_life -= player_attack
    player_life -= monster_attack
    print(f'\nDu versursacht dem Monster {player_attack} Schaden damit hat das Monster noch: {monster_life} Leben \nDu hast noch: {player_life}')
    if monster_life <= 0:
      print('Du hast das Monster besiegt Glückwunsch!')
      break

    if player_life <= 0:
      print('Du wurdest besiegt!')
      break

print('Spiel vorbei! Bis zum nächsten mal')