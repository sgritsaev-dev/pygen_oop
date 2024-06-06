class FuzzyString(str):
    def __eq__(self, other):  # ==
        if isinstance(other, (self.__class__, str)):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):  # !=
        if isinstance(other, (self.__class__, str)):
            return self.lower() != other.lower()
        return NotImplemented

    def __lt__(self, other):  # <
        if isinstance(other, (self.__class__, str)):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):  # >
        if isinstance(other, (self.__class__, str)):
            return self.lower() > other.lower()
        return NotImplemented

    def __le__(self, other):  # <=
        if isinstance(other, (self.__class__, str)):
            return self.lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other):  # >=
        if isinstance(other, (self.__class__, str)):
            return self.lower() >= other.lower()
        return NotImplemented

    def __contains__(self, other):  # other in self
        if isinstance(other, (self.__class__, str)):
            return other.lower() in self.lower()
        return NotImplemented
