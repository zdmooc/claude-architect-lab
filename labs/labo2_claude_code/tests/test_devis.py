from src.devis import calculer_prime


def test_prime_conducteur_experimente():
    assert calculer_prime(30, 1.0) == 400.0


def test_majoration_jeune_conducteur_avant_25_ans():
    assert calculer_prime(24, 1.0) == 600.0


def test_pas_de_majoration_a_25_ans_exactement():
    assert calculer_prime(25, 1.0) == 400.0


def test_coefficient_plafonne():
    assert calculer_prime(40, 10.0) == 1400.0
