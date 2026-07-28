import pytest
from app.logic import is_eligible_for_loan


def test_eligible_user():
    assert is_eligible_for_loan(income= 60000, age= 25, employment_status= 'employed') == True
    
    
def test_underage_user():
    assert is_eligible_for_loan(income= 60000, age= 19, employment_status= 'employed') == False
    
def test_low_income_user():
    assert is_eligible_for_loan(income= 30000, age= 25, employment_status= 'employed') == False
    

def test_unemployed_user():
    assert is_eligible_for_loan(income= 60000, age= 25, employment_status= 'unemployed') == False
    

def test_boundary_case():
    assert is_eligible_for_loan(income= 50000, age= 21, employment_status= 'employed') == True
    
