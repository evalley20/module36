import RoboPiLib as RPL
import setup
def break()
  x = RPL.analogRead(4)
  speed0 = - 0.000885 * x ** 2 + 0.558286 * x + 1481.5
  speed1 = - 0.000885 * x ** 2 + 0.558286 * x + 1481.5
  print('this is the speed0', speed0)
  print('this is the speed1', speed1)

  if speed0 and speed1 >= 0:
    RPL.servoWrite(0,int(speed0)) 
    RPL.servoWrite(1,int(speed1))
break()
