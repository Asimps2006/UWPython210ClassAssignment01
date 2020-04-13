# ****************************************************************************
# Title:  break_me.py  lesson01
# Written By:  Andy Simpson
# Date: 04/12/2020
# ****************************************************************************

# Global Variables -------------------------------------------------------------------- #


# Processing  --------------------------------------------------------------- #
class BreakStuff:
    """  Performs Processing tasks """

    @staticmethod
    def name_error():
        """ Reads data from a file into a list of dictionary rows

        :return: (string) the "Name" Error Type Message
        """
        try:
            4 + spam*3
        except Exception as e:
            print(e)
            return e.__cause__

    @staticmethod
    def type_error():
        """ Reads data from a file into a list of dictionary rows

        :return: (string) the "Name" Error Type Message
        """
        try:
            badtype = 2 + "two"

            print("Bad Type Error %s") % badtype
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def syntax_error():
        """ Reads data from a file into a list of dictionary rows

        :return: (string) the "Name" Error Type Message
        """
        try:
            while True :
                print('Hello world')
        except Exception as e:
            print(e)
            return e.__cause__

    @staticmethod
    def attribute_error():
        """ Reads data from a file into a list of dictionary rows

        :return: (string) the "Name" Error Type Message
        """
        try:
            x = 10
            x.append(6)
        except Exception as e:
            print(e)
            return e

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts


# BreakStuff.name_error()
# strError = BreakStuff.type_error()
# BreakStuff.syntax_error()
BreakStuff.attribute_error()
#print(strError)
print("Finished")
