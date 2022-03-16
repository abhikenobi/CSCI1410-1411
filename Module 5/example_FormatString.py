#   formatOut.py
# See more examples in chapeter 5

# String formatting is an easy way to get beautiful output!
## <template-string>.format(<values>)
## <template-string> has the following format:
## {<index>:<format-specifier}
# Python 3.1, the index is optional. If it is omitted, the parameters
#    are filled into the slots in a left-to-right fashion
#

def main():
    # String formating
    print ("Hello {0} {1}, you may have won ${2}" .format("Mr.", "Smith", 10000))
    # change the order of the slot index
    print ("Hello {1} {0}, you may have won ${2}" .format("Mr.", "Smith", 10000))

    #Control the width and the precision of numeric value
    val = 3.1415169999
    #       " optional label or message {<index>:<format-specifier}".format(<values>)
    # for fixed-point (indicated by f) the precision gives the number of decimal places
    print ("val = {0:2.4f}".format(val)) # 3.1415

    # here we are not using f, so .4 specifies the number of significant digits to print,
    # which includes both the integer and decimal part.
    print ("val = {0:2.4}".format(val))  # 3.141

    # Justification
    # < left justification
    # > right justification
    # ^ center justification
    print("left   justification: {0:<10}".format("Hello!")
)
    print("right  justification: {0:>10}".format("Hello!"))
    print("center justification: {0:^10}".format("Hello!"))
   
main()

