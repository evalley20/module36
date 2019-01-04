import RoboPiLib as RPL
import setup
def break()
  x = RPL.analogRead(4)
  speed0 = -0.000776 * x ** 2 + 0.583894 * x + 1492.43
  speed1 = -0.000776 * x ** 2 + 0.583894 * x + 1492.43
  print('this is the speed0', speed0)
  print('this is the speed1', speed1)

  if speed0 and speed1 >= 0:
    RPL.servoWrite(0,int(speed0)) 
    RPL.servoWrite(1,int(speed1))
break()
