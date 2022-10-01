import math

class Convert():

    def grade_adjust(velocity, grade):
        # adapted from https://medium.com/strava-engineering/an-improved-gap-model-8b07ae8886c3
        factor = .0015*(grade**2)+(.0301*grade)+.997
        return velocity*(1/factor)

    def miles_to_km(distance):
        return distance*1.60934

    def time_lst_to_minutes(lst):
        minutes = 60*lst[0] + lst[1] + lst[2]/60
        return minutes

    def time_minutes_to_str(t):
        hours = math.floor(t/60)
        minutes = math.floor(t%60)
        seconds = int(round(60*(t - (hours*60 + minutes)), 0))
        if minutes == 60:
            minutes = 0
            hours+=1
        if seconds == 60:
            seconds =0
            minutes+=1
        if hours == 0:
            return f"{minutes:02}:{seconds:02}"
        else:
            return f"{hours:02}:{minutes:02}:{seconds:02}"

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
        max_iter = 300
        count = 0
        while (True):
            if count > max_iter:
                print(f"Exceeded {max_iter} iterations!")
                return old_guess
            f = ((((0.000104) * (distance**2) * (old_guess**-2)) + ((0.182258)*distance*(old_guess**-1)) -4.6)/((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)) - vdot
            df = ((((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)*((-0.000208)*(distance**2) * (old_guess**-3)) - ((0.182258) * distance * (old_guess**-2))) - (vdot * ((0.2989558)*(math.exp( -0.1932605*old_guess)) + (0.1894393) * (math.exp(-0.012778*old_guess))))) / (((0.2989558*math.exp( -0.1932605*old_guess)) + (0.1894393 * math.exp(-0.012778*old_guess)) + 0.8)**2)
            new_guess = old_guess-(f/df)
            if (old_guess-new_guess) < .0001:
                return new_guess
            else:
                count+=1
                old_guess = new_guess

    def get_vdot(distance, t):
        '''
        This funcion calculates vdot for a given distance (meters) and time (minutes)
        inputs: float(distance); float(time)
        output: float(vdot)
        '''
        old_guess = 100
        max_iter = 350
        count = 0
        while (True):
            if count > max_iter:
                print(f"Exceeded {max_iter} iterations!")
                return old_guess
            f = ((((0.000104) * (distance**2) * (t**-2)) + ((0.182258)*distance*(t**-1)) -4.6)/((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)) - old_guess
            df = ((((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)*((-0.000208)*(distance**2) * (t**-3)) - ((0.182258) * distance * (t**-2))) - (old_guess * ((0.2989558)*(math.exp( -0.1932605*t)) + (0.1894393) * (math.exp(-0.012778*t))))) / (((0.2989558*math.exp( -0.1932605*t)) + (0.1894393 * math.exp(-0.012778*t)) + 0.8)**2)
            new_guess = old_guess-(f/df)
            if (old_guess-new_guess) < .0001:
                return new_guess
            else:
                count+=1
                old_guess = new_guess

class Predict():
    def performance(vdot, distance, grade):
        '''This function calculates a race time for a given vdot, distance, and grade
        inputs: decimal(vdot); decimal(distance in meters); decimal(grade as %)
        output: string(time)
        '''
        time_flat = VDOT.get_time(distance, vdot)
        velocity_flat = distance/time_flat
        velocity_adjusted = Convert.grade_adjust(velocity_flat, grade)
        time_adjusted = distance/velocity_adjusted
        return Convert.time_minutes_to_str(time_adjusted)