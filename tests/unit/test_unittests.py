from src.FarmWisdom import Accounting
from src.FarmWisdom import FarmWisdom
import pytest
#from the folder import the python file

#pytest needs to be run from the lowest folder
#which has children both FarmWisdom.py and tests folders

#when you import a module, it executes the whole thing
#not just what you bind to your namespace

# the assertion needs to reference the namespace
# and be called test...something

def test_buy():
    bank_account = Accounting.Account(2000)
    bank_account.buy(15)
    assert bank_account.balance == 1985

def test_earn():
    bank_account = Accounting.Account(2000)
    bank_account.earnings(415)
    assert bank_account.balance == 2415 

def test_chickens():
    FarmWisdom.buyFlockOfChickens()
    assert len(FarmWisdom.assets) > 0

def test_exit():
    with pytest.raises(SystemExit) as e:
        FarmWisdom.goodRun()
    assert e.type == SystemExit