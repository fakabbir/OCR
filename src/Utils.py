from bs4 import BeautifulSoup
from OCRClass.textBoxClass import textBox

def isNear(l,t,l0,t0):
    """Gets the coordinates of two points and returns
    the square of distance between them.
    For any point above 50 pixels from the base region
    it return 500000.

    Parameters
    ----------
    l : int
        x coordinate of the text region interested
    t : int
        y coordinate of the text region interested
    l0 : int
        x coordinate of the text region comparing with.
    t0 : int
        y coordinate of the text region comparing with

    Returns
    -------
    int
        an integer representing the square of distance between the points
    """
    l = float(l)
    t = float(t)
    l0 = float(l0)
    t0 = float(t0)
    #print("Hello")
    # TODO put top as well as down bar to the values
    if t0-50>t:
       return 500000
    return (l-l0)*(l-l0) + (t-t0)*(t-t0)

def Slope(l,t,l0,t0):
    """Gets the coordinates of two points and returns
    the slope of line formed by them.

    Parameters
    ----------
    l : int
        x coordinate of the text region interested
    t : int
        y coordinate of the text region interested
    l0 : int
        x coordinate of the text region comparing with.
    t0 : int
        y coordinate of the text region comparing with

    Returns
    -------
    float
        a float value representing the slope of line formed by the two points
    """
    l = float(l)
    t = float(t)
    l0 = float(l0)
    t0 = float(t0)
    return abs((t-t0)/(0.001+l-l0))

def getNear(textBlob,pref,SEARCH_STRATEGY,LIMIT_ = 3):
    """Returns the nearest possible textBox based on search strategy

    Parameters
    ----------
    textBlob : list
        list of possible textBox
    pref : textBox
        base textBox
    SEARCH_STRATEGY: str
        "LEFT/RIGHT": REpresent the optimal search direction

    LIMIT_: int
        number of results to return
    Returns
    -------
    list
        a list of textBox
    """

    Blob = []
    resultBlob = []

    for i in textBlob:


        nearScore = isNear(i.l, i.t, pref[0].l, pref[0].t)
        slopeScore = Slope(i.l, i.t, pref[0].l, pref[0].t)

        # TODO Correct the sequence here
        if i.page == pref[0].page and nearScore < 300000 and not (i.l == pref[0].l and i.t ==pref[0].t):
            Blob.append((i,nearScore,slopeScore))

    # ARRANGE IN SEARCH_STRATEGY PREFERENENCE
    # TODO results are getting out of bound errors
    if SEARCH_STRATEGY == "LEFT":
        resultBlob.append(sorted(Blob,key=sortFunction2,reverse=False)[0])
        resultBlob.append(sorted(Blob, key=sortFunction1, reverse=False)[0])
        #resultBlob.append(sorted(Blob, key=sortFunction2, reverse=False)[1])
    else:
        resultBlob.append(sorted(Blob,key=sortFunction1,reverse=False)[0])
        resultBlob.append(sorted(Blob, key=sortFunction2, reverse=False)[0])
        #resultBlob.append(sorted(Blob, key=sortFunction1, reverse=False)[1])

    return resultBlob

def sortFunction2(x):
    """KEY FUNCTION FOR inbuild sorted func
    returns the 3rd value from the tuple

    Parameters
    ----------
    x : tuple

    Returns
    -------
    float
        3rd value of the tuple input
    """
    return x[2]

def sortFunction1(x):
    """KEY FUNCTION FOR inbuild sorted func
    returns the 2nd value from the tuple

    Parameters
    ----------
    x : tuple

    Returns
    -------
    float
        2nd value of the tuple input
    """
    return x[1]

def soupExtractor(Soup):
    """Gets BeautifulSoup and return list of textBox

    Parameters
    ----------
    Soup : bs4 Soup Object
        BeautifulSoup Object loaded with the file
    Returns
    -------
    list
        a list of textBox extracted from the document
    """
    pages = Soup.findAll("page")
    textBlob = []

    for i_page, page in enumerate(pages):

        paragraphs = page.findAll("par")
        for i_paragraph, paragraph in enumerate(paragraphs):

            lines = paragraph.findAll("line")
            for i_line, line in enumerate(lines):
                data_ = "".join(line.getText().split("\n"))
                textObj = textBox(data_, i_page, i_paragraph, i_line,
                                  line['l'], line['t'], line['r'], line['b'])

                textBlob.append(textObj)
    return textBlob

def gettextBlob(filePath):
    """Gets filepath and return list of textBox

    Parameters
    ----------
    filePath : str
        The file location of the spreadsheet
    Returns
    -------
    list
        a list of textBox extracted from the document
    """
    fileHandler = open(filePath).read()
    Soup = BeautifulSoup(fileHandler,features="html.parser")
    return soupExtractor(Soup)