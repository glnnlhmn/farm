# tests/conftest.py

import pytest

@pytest.fixture
def expected_interaction_one_animal():
    return {
        "pig_chicken": "This morning in the barn yard there is a pig and a chicken. You hear the pig oink and the chicken cluck!",
        "pig_cow": "This morning in the barn yard there is a pig and a cow. You hear the pig oink and the cow moo!",
        "chicken_pig": "This morning in the barn yard there is a chicken and a pig. You hear the chicken cluck and the pig oink!",
        "chicken_cow": "This morning in the barn yard there is a chicken and a cow. You hear the chicken cluck and the cow moo!",
        "cow_pig": "This morning in the barn yard there is a cow and a pig. You hear the cow moo and the pig oink!",
        "cow_chicken": "This morning in the barn yard there is a cow and a chicken. You hear the cow moo and the chicken cluck!"
    }

@pytest.fixture
def expected_interaction_two_animals():
    return {
        "pig_chicken_cow": "This morning in the barn yard there is a pig, a chicken, and a cow. You hear the pig oink, the chicken cluck, and the cow moo!",
        "pig_cow_chicken": "This morning in the barn yard there is a pig, a cow, and a chicken. You hear the pig oink, the cow moo, and the chicken cluck!",
        "chicken_pig_cow": "This morning in the barn yard there is a chicken, a pig, and a cow. You hear the chicken cluck, the pig oink, and the cow moo!",
        "chicken_cow_pig": "This morning in the barn yard there is a chicken, a cow, and a pig. You hear the chicken cluck, the cow moo, and the pig oink!",
        "cow_pig_chicken": "This morning in the barn yard there is a cow, a pig, and a chicken. You hear the cow moo, the pig oink, and the chicken cluck!",
        "cow_chicken_pig": "This morning in the barn yard there is a cow, a chicken, and a pig. You hear the cow moo, the chicken cluck, and the pig oink!"
    }