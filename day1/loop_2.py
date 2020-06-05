for item in lst_mxd:
    if (type(item)==int) or (type(item) == float) :
        print('{} is a numerical datatype'.format(item))
    elif (isinstance(item,str)):
        print('{} is a string datatype'.format(item))
    else:
        print('{} :datatype unknown'.format(item))
