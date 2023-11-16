class Carro:
    def __init__(self, vel_max, vel_atual=0):
        self.vel_max=vel_max
        self.vel_atual=vel_atual
    
    def acelerar(self, delta=5):
        if self.vel_atual!=self.vel_max:
            if self.vel_atual+delta>=self.vel_max:
                delta = self.vel_max-self.vel_atual
            self.vel_atual+=delta
            return self.vel_atual
        else:
            return self.vel_atual
    
    def frear(self, delta=10):
        if self.vel_atual!=0:
            if self.vel_atual-delta<=0:
                delta = self.vel_atual
            self.vel_atual-=delta
            return self.vel_atual
        else:
            return self.vel_atual

if __name__=='__main__':
    c1 = Carro(180)


    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))