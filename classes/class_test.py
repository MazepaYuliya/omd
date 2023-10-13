class BasePokemon:
    def __init__(self, name, category):
        self.name = name  # Имя покемона
        self.category = category  # Категория покемона

    def __str__(self):
        return f"{self.name}/{self.category}"


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self.weaknesses = weaknesses  # Слабости покемона

    @property
    def weakness(self):
        return self.weaknesses[0] if self.weaknesses else ''


base_charmander = BasePokemon(name='Charmander', category='Lizard')
print(base_charmander)

bulbasaur = Pokemon(
   name='Bulbasaur',
   category='seed',
   weaknesses=('fire', 'psychic', 'flying', 'ice')
)
print(bulbasaur.weakness)
