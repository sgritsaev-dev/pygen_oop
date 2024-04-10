class Gun:
    def __init__(self) -> None:
        self.count=0
    def shoot(self):
        self.count+=1
        if self.count%2==1:
            print("pif")
        else:
            print('paf')

gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()