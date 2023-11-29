from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
  print(f'Olá {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada')
  
  pikachu = PokemonEletrico('Pikachu')
  charmander = PokemonFogo('Charmander')
  squirtle = PokemonAgua('Squirtle')
  
  print('Você possui 3 escolhas: ')
  print('1 -', pikachu)
  print('2 -', charmander)
  print('3 -', squirtle)
  
  while True:
    escolha = input('Escolha o seu Pokemon: ')
    
    if escolha == '1':
      player.capturar(pikachu)
      break
    elif escolha == '2':
      player.capturar(charmander)
      break
    elif escolha == '3':
      player.capturar(squirtle)
      break
    else:
      print('Escolha inválida')
      

player = Player('Lucas')    
escolher_pokemon_inicial(player)
player.mostrar_dinheiro()
#player.mostrar_pokemons()

#inimigo1 = Inimigo(name='Gary', pokemons=[PokemonAgua('Squirtle')])


#player.batalhar(inimigo1)
player.explorar()
player.mostrar_pokemons()
