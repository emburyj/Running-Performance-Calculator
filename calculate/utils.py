import math

class Convert():
    def grade_adjust(velocity, grade):
        pass

class VDOT():
    '''
    source: http://www.simpsonassociatesinc.com/runningmath8.htm
    '''
    def get_time(distance, vdot):
        '''
        This funcion calculates time (min) for a given distance (meters) and vdot
        inputs: float(distance); float(vdot)
        output: float(time)
        '''
        old_guess = 300
        max_iter = 250
        count = 0
        while (True):
            if count > max_iter:
                print(f"Exceeded {max_iter} iterations!")
                return old_guess
            f = ((((0.000104) * (distance**2) * (old_guess**-2)) + ((0.182258)*distance*(old_guess**-1)) -4.6)/((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)) - vdot
            df = ((((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)*((-0.000208)*(distance**2) * (old_guess**-3)) - ((0.182258) * distance * (old_guess**-2))) - (vdot * ((0.2989558)*(math.exp( -0.1932605*old_guess)) + (0.1894393) * (math.exp(-0.012778*old_guess))))) / (((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)**2)
            new_guess = old_guess-(f/df)
            if (old_guess-new_guess) < .00001:
                return new_guess
            else:
                count+=1
                old_guess = new_guess

    def get_vdot(distance, t):
        '''
        This funcion calculates time (min) for a given distance (meters) and vdot
        inputs: float(distance); float(vdot)
        output: float(time)
        '''
        old_guess = 500
        max_iter = 250
        count = 0
        while (True):
            if count > max_iter:
                print(f"Exceeded {max_iter} iterations!")
                return old_guess
            f = ((((0.000104) * (distance**2) * (t**-2)) + ((0.182258)*distance*(t**-1)) -4.6)/((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)) - old_guess
            df = ((((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)*((-0.000208)*(distance**2) * (t**-3)) - ((0.182258) * distance * (t**-2))) - (old_guess * ((0.2989558)*(math.exp( -0.1932605*t)) + (0.1894393) * (math.exp(-0.012778*t))))) / (((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)**2)
            new_guess = old_guess-(f/df)
            if (old_guess-new_guess) < .001:
                return new_guess
            else:
                count+=1
                old_guess = new_guess

## Test
# dist = 5000
# vdot = 90
# t = VDOT.get_time(dist, vdot)
# print(f"With a vdot of {vdot}, I predict a time of {t}min for {dist}m")

dist = 5000
t = 16
vdot = VDOT.get_vdot(dist, t)
print(f"With a time of {t}min for the {dist}m, your vdot is {vdot}")