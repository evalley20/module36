import RoboPiLib as RPL
import wall_evasion
RPL.pinMode(16,RPL.INPUT)
RPL.pinMode(17,RPL.INPUT)
while True:
  approach_and_turn16()
  approach_and_turn17()
