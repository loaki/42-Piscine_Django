import sys
import antigravity

class ValidationError(Exception):
    def __init__(self, msg="Incorrect arg"):
        print(msg)
    
def geohash():
    if len(sys.argv) != 4:
        return print('wrong args : latitude, longitude, datedowjones')
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        dowjones = sys.argv[3].encode('utf-8')
    except Exception as e:
        return ValidationError(e)
    antigravity.geohash(latitude, longitude, dowjones)

if __name__=='__main__':
    geohash()