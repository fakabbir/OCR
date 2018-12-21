class textBox:
    """
    A class used to represent a text located in the file.

    ...

    Attributes
    ----------
    data : str
        a string to represent the text identified from hOCR
    page : int
        Page number for the located text
    para : int
        paragraph number for the located text
    l : int
        left corner coordinated for the located text
    t : int
        top corner coordinated for the located text
    r : int
        right corner coordinated for the located text
    b : int
        baseline corner coordinated for the located text

    """
    def __init__(self, data, page, para, line, l, t, r, b):
        """
        Parameters
        ----------
        data : str
            a string to represent the text identified from hOCR
        page : int
            Page number for the located text
        para : int
            paragraph number for the located text
        l : int
            left corner coordinated for the located text
        t : int
            top corner coordinated for the located text
        r : int
            right corner coordinated for the located text
        b : int
            baseline corner coordinated for the located text
    """
        self.data = data
        self.page = page
        self.para = para
        self.l = l
        self.t = t
        self.r = r
        self.b = b