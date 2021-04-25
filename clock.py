from datetime import datetime #imports datetieme package
class Clock: #constructs the clock class
  now = 0
  def time(): #constructs the time method
    now = datetime.now()
    now = str(now)
    now = now [11:-10] #trunctuates the time out of datetime
    return now
  def date(): #constructs the date method
    today = datetime.now()
    today = str(today)
    today = today [0:10] #trunctuates the date out of datetime
    return today
