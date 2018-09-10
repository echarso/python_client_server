
pool = 0
class Controller:
    def __init__(self):
        print "Create controller!!!!!"

    def decrease(self,value):
        global pool
        if pool - value >= -100.0 :
            pool = pool-value
        return str(pool)

    def increase(self,value):
        global pool
        if pool + value <= 100.0 :
            pool = pool+value
        return str(pool)
