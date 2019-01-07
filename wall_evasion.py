def approach_and_turn16():
  reading = RPL.digitalRead(16)
  if reading == 0:
    RPL.servoWrite(0,1450)
    RPL.servoWrite(1,1610)
  elif:
    RPL.servoWrite(0,1450)
    RPL.servoWrite(1,1550)
approach_and_turn16()

def approach_and_turn17():
  reading = RPL.digitalRead(17)
  if reading == 0:
    RPL.servoWrite(0,1610)
    RPL.servoWrite(1,1450)
  elif:
    RPL.servoWrite(0,1550)
    RPL.servoWrite(1,1450)
approach_and_turn17()
