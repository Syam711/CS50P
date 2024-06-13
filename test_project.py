import project as p

def test_generate_random_number():
    assert (0 < p.generate_random_number(1) and p.generate_random_number(1) < 10)
    assert (9 < p.generate_random_number(2) and p.generate_random_number(2) < 100)
    assert (99 < p.generate_random_number(3) and p.generate_random_number(3) < 1000)

def test_set_difficulty():
    assert p.set_difficulty(1,'1') == 10
    assert p.set_difficulty(1,'3') == 5
    assert p.set_difficulty(2,'2') == 64
    assert p.set_difficulty(3,'3') == 125

def test_compare_guess():
    assert p.compare_guess(1,2,7) == (0,['X'])
    assert p.compare_guess(1,7,7) == (1,['7'])
    assert p.compare_guess(2,52,56) == (1,['5','X'])
    assert p.compare_guess(3,245,671) == (0,['X','X','X'])

def test_evaluate_guess():
    assert p.evaluate_guess(1,2,2) == 1
    assert p.evaluate_guess(2,43,21) == 0
    assert p.evaluate_guess(1,43,41) == None

