class TypeTable():
    pass

def critChanceCalculation():
    return 1

def damageCalculation(PokemonLevel, MovePower, PokemonAttack, TargetDefense, STAB, Type1, Type2):
    Damage = ((2*PokemonLevel*critChanceCalculation()/5 + 2) * MovePower * PokemonAttack/TargetDefense/50 +2) *STAB * Type1* Type2
    return Damage

