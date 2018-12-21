from Utils import *

def EFNInvoiceAmount(textBlob, possibleKey,SEARCH_STRATEGY):
    """Gets the possible invoice amount from the list of textBox

    Parameters
    ----------
    textBlob : list
        list of all the textBox identified in the document
        or
        list of the the interested textBox Objects

    possibleKey : list
        list of all the identified possible key, each element
        is a textBox Object.

    SEARCH_STRATEGY : str
        values: "LEFT" or "DOWN"
        it defines the direction where the values are most probable
        to find in.

    Returns
    -------
    str
        a string denoting the invoice amount extracted or empty string
    """
    for i in possibleKey:
        p = getNear(textBlob,i,SEARCH_STRATEGY,LIMIT_ = 3)
        extracts  = isInvoiceNumberInNear(p)
        if extracts[0]:
            return  extracts[1]

    return ""

def IPInvoiceAmount(possibleKey):
    """Gets the possible invoice amount from the list of possible key.
    It looks for the value within the key textBox identified

    Parameters
    ----------
    possibleKey : list
        list of all the identified possible key, each element
        is a textBox Object.

    Returns
    -------
    tuple
        a tuple (True/False,"Value Extracted","LEFT/DOWN")
        True is value found
        "Value Extracted" if the value is present
        "LEFT" if the key denotes possibility to look in left direction for Values
    """
    SEARCH_STRATEGY = "RIGHT"
    for i in possibleKey:
        if "$" in i[0].data:
            SEARCH_STRATEGY = "LEFT"
            if len(i[0].data.split("$")[-1].strip())>1 :
                return  True,i[0].data.split("$")[-1].strip()
            #return EFNInvoiceNumber(i,SEARCH_STRATEGY = "LEFT")
    return False,"Answer",SEARCH_STRATEGY


def qualifiesInvoiceNumber(result):
    """Gets string and returns if the string qualifies as an Invoice
    Amount.

    Parameters
    ----------
    result : str
        string value for the extracted value for invoice amount key

    Returns
    -------
    bool
        a boolean value denoting is the value qualifies or not
    """
    result = "".join(result.split(" "))
    return  True #not str.isalpha(result)

def isInvoiceNumberInNear(p):
    """Gets the possible textbox

    Parameters
    ----------
    p : list
        list of possible values textBox

    Returns
    -------
    str
        final string value for extracted amount
    """
    # TODO implement a closeness score
    if qualifiesInvoiceNumber(p[0][0].data):
        return "True",p[0][0].data
    return True, p[1][0].data




