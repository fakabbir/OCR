"""Configuration file

This python script allows the user to store the trained or predefined
weights for keywords that should be searched in the document for identifying
the keys.

NOTE: Python would return false for 0.7+0.2 == 0.9

It assumes that the weights will sum up to or greater than 0.9 in order
to qualify as a valid possible key.
"""
KEY_INVOICE_NUMBER = {"invoice": 0.7, "number": 0.25, "No": 0.2, "#": 0.2, ":": 0.23, "date": -0.7}
KEY_INVOICE_DATE = {"invoice": 0.3, "number": -0.7, "no": -1.7, "#": 0.2, ":": 0.23, "date": 0.7, "issue": 0.7}
KEY_AMOUNT = {"due": 0.7, "amount": 0.2, "balance": 0.21, "total": 0.9, ":": 0.23, "date": -0.7, "reimbursement": 0.71,
       "net": 0.2, "$": .3, "remit": 0.4, "sub": -0.7}
KEY_TERMS = {"payment": 0.21, "terms": 0.7, "balance": 0.21}