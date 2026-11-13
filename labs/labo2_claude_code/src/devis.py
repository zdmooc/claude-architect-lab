"""Calcul de devis auto (fictif)."""
from src import bareme


def calculer_prime(age: int, coefficient_bonus_malus: float) -> float:
    """Prime annuelle en euros, arrondie au centime."""
    coeff = min(coefficient_bonus_malus, bareme.PLAFOND_COEFF)
    prime = bareme.PRIME_BASE * coeff
    if age < 25:
        prime *= 1 + bareme.MAJORATION_JEUNE_CONDUCTEUR
    return round(prime, 2)


if __name__ == "__main__":
    print(calculer_prime(30, 0.85))
