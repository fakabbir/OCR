class KC:
    """
    A class used to represent an Similarity between KEY and TEXT

    ...

    Attributes
    ----------
    text : str
        a formatted denoting the data/text stored in a textBox
    KEY : dict
        Dictionary of relevant keys with their weights
    isCandidateValue : bool
        boolean value representing if the text could be a good candidate
    TextKeySimilarityValue : float
        a score representing the similarity between text and key(represented by the dict)

    Methods
    -------
    TextKeySimilarity()
        Return: tuple
            (TRUE/FALSE, SCORE)
            TRUE means the score is good enough to be a candidate to consider
            SCORE represents the score associated with the claim
    """
    def __init__(self, text, KEY):
        self.text = text
        self.KEY = KEY
        self.isCandidateValue,self.TextKeySimilarityValue = self.TextKeySimilarity()

    def TextKeySimilarity(self):
        """ Returns the similarity tuple for key and text

        Return: tuple
            (TRUE/FALSE, SCORE)
            TRUE means the score is good enough to be a candidate to consider
            SCORE represents the score associated with the claim

        Parameters
        ----------

        Raises
        ------

        """
        score = 0
        TEXT = str.lower(self.text)
        TEXT = "".join(TEXT.split(" "))
        for k in self.KEY:
            if k in TEXT:
                score += self.KEY[k]

        return score >= 0.9, score

    def isCandidate(self):
        """Getter function for self.isCandidateValue

        Parameters
        ----------

        Raises
        ------
        """

        return self.isCandidateValue

    def candidateScore(self):
        """Getter function for self.TextKeySimilarityValue

        Parameters
        ----------

        Raises
        ------
        """
        return  self.TextKeySimilarityValue