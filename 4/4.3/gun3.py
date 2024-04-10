class Gun:
    def __init__(self) -> None:
        self.count=0
    def shoot(self):
        self.count+=1
        if self.count%2==1:
            print("pif")
        else:
            print('paf')
    def shots_count(self):
        return self.count
    def shots_reset(self):
        self.count=0