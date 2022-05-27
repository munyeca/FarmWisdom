from FarmWisdom import FarmWisdom
#from the folder import the python file
#the FarmWisdom folder is the highest level directory with an __init__ file

#pytest needs to be run from FarmWisdom_project
#which contains both FarmWisdom and tests folders

# the assertion needs to reference the namespace

def test_balance():
    assert FarmWisdom.balance is not None