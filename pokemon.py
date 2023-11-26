class Pokemon:
  def __init__(self, tipo, especie):
    self.tipo = tipo
    self.especie = especie
    
  def __str__(self) -> str:
    return '{} ({})'.format(self.especie, self.tipo)
  
  def atacar(self, pokemon):
    print('{} atacou {}'.format(self, pokemon))
  
  
  
  
meu_pokemon = Pokemon('fogo', 'charmander')
meu_pokemon1 = Pokemon('agua', 'bulbasaur')

print(meu_pokemon)
meu_pokemon.atacar(meu_pokemon1)







