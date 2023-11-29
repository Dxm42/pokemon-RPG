import random
class Pokemon:
  def __init__(self, especie, level=None, nome=None):
    self.especie = especie
    
    if level:      
      self.level = level
    else:
      self.level = random.randint(1, 100)
    
    if nome:
      self.nome = nome
    else:
      self.nome = especie
    
    self.ataque = self.level * 5
    self.vida = self.level * 10
    
  def __str__(self) -> str:
    return '{} ({})'.format(self.nome, self.level)
  
  def atacar(self, pokemon):
    ataque_efetivo =  int(self.ataque * random.random() * 1.3)
    pokemon.vida = pokemon.vida - ataque_efetivo
    print(f'{pokemon} perdeu {ataque_efetivo:.0f} pontos de vida')

    if pokemon.vida <= 0:
      print('{} foi derrotado'.format(pokemon))
      return True
    else:
      return False
      
# Herança - Para Herdar uma classe usa-se parenteses -> (classe a ser herdada)
class PokemonEletrico(Pokemon):
  tipo = 'Eletric'
  def atacar(self, pokemon):
    print('{} lançou um ataque de trovão em {}'.format(self, pokemon))
    return super().atacar(pokemon)
  
class PokemonFogo(Pokemon):
  tipo = 'Fire'
  def atacar(self, pokemon):
    print('{} lançou um ataque de fogo em {}'.format(self, pokemon))
    return super().atacar(pokemon)
  
class PokemonAgua(Pokemon):
  tipo = 'Water'
  def atacar(self, pokemon):
    print('{} lançou um ataque de aguá em {}'.format(self, pokemon))
    return super().atacar(pokemon)
  