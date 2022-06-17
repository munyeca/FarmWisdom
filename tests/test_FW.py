from FarmWisdom import FarmWisdom
#from the folder import the python file
#the FarmWisdom folder is the highest level directory with an __init__ file

#pytest needs to be run from FarmWisdom_project
#which contains both FarmWisdom and tests folders

# the assertion needs to reference the namespace
# and be called test...something

def test_balance():
    assert FarmWisdom.bank_account is not None
    
def test_assets_acquired():
    assert len(FarmWisdom.assets) > 0