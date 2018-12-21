from OCRClass.KCClass import KC
from Utils import *

from metadata.InvoiceNumber import *
from metadata.InvoiceDate import *
from metadata.InvoiceAmount import *

def KeyCandidates(textBlob,KEY):
    """Returns list of possible textBox matching the KEY

    Parameters
    ----------
    textBlob : list
        list of all the textBox identified in the document
        or
        list of the the interested textBox Objects

    KEY : dict
        Dictionary of relevant keys with their weights

    Returns
    -------
    list
        a list of textBox extracted
    """
    possibleKey = []
    #return textBox Object
    for text in textBlob:
        keyCheck = KC(text.data,KEY)
        if keyCheck.isCandidate():
            possibleKey.append((text, keyCheck.candidateScore()))

    possibleKey = sorted(possibleKey, key=sortFunction1, reverse=True)
    return possibleKey

def isPresent(possibleKey, KEY_SEARCH):
    """Factory Method for first extraction from keys detected itself

    Parameters
    ----------
    possibleKey : list
        list of all the identified possible key, each element
        is a textBox Object.

    SEARCH_STRATEGY : str
        values: "LEFT" or "DOWN"
        it defines the direction where the values are most probable
        to find in.

    Returns
    -------
    tuple
        a tuple (True/False,"Value Extracted","LEFT/DOWN")
        True is value found
        "Value Extracted" if the value is present
        "LEFT" if the key denotes possibility to look in left direction for Values
    """
    if KEY_SEARCH == "INVOICE_NUMBER":
        return IPInvoiceNumber(possibleKey)

    if KEY_SEARCH == "INVOICE_DATE":
        return IPInvoiceDate(possibleKey)

    if KEY_SEARCH == "INVOICE_AMOUNT":
        return IPInvoiceAmount(possibleKey)


def extractFromNear(textBlob, possibleKey, KEY_SEARCH,SEARCH_STRATEGY):
    """ Factory Method for Extraction

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
        a string denoting the invoice number extracted or empty string
    """
    if KEY_SEARCH == "INVOICE_NUMBER":
        return EFNInvoiceNumber(textBlob, possibleKey,SEARCH_STRATEGY)

    if KEY_SEARCH == "INVOICE_DATE":
        return EFNInvoiceDate(textBlob, possibleKey,SEARCH_STRATEGY)

    if KEY_SEARCH == "INVOICE_AMOUNT":
        SEARCH_STRATEGY = "LEFT"
        return EFNInvoiceAmount(textBlob, possibleKey,SEARCH_STRATEGY)