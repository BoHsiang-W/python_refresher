from mymodule import divide

print("code.py:", __name__)  # code.py: __main__
print(divide(10, 2))  # 5.0
print(__name__)  # __main__

####################################################################################################
import sys

print(sys.path)  # finds the path of the module

####################################################################################################
import mymodule
import sys

print(sys.modules)  # shows all the modules that are imported
