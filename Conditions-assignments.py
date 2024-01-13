#1 --> Write a program to read the Richter magnitude value from the user and display
#      the result for the following conditions using if...elif...else statement.
#       Richter                                                  Magnitude Information
#       > 1.0 and < 2.0                                     Microearthquakes not felt or rarely felt
#       > 2.0 and < 4.0                                    Very rarely causes damage
#       > 4.0 and < 5.0                                    Damage done to weak buildings
#       > 5.0 and < 6.0                                    Cause damage to the poorly constructed building
#       > 6.0 and < 7.0                                     Causes damage to well-built structures
#       > 7.0 and < 8.0                                      Causes damage to most buildings
#       > 8.0 and < 9.0                                     Causes major destruction
#       > 9.0                                                    Causes unbelievable damage

#ans : 
magnitude = float(input("Enter the richter magnitude of earthquake : "))
if magnitude >= 1.0 and magnitude < 2.0:
    print("Microearthquakes not felt or rarely felt")
elif magnitude >= 2.0 and magnitude < 4.0:
    print("Very rarely causes damage")
elif magnitude >= 4.0 and magnitude < 5.0:
    print("Damage done to weak buildings")
elif magnitude >= 5.0 and magnitude < 6.0:
    print("Cause damage to the poorly constructed building")
elif magnitude >= 6.0 and magnitude < 7.0:
    print("Causes damage to well-built structures")
elif magnitude >= 7.0 and magnitude < 8.0:
    print("Causes damage to most buildings")
elif magnitude >= 8.0 and magnitude < 9.0:
    print("Causes major destruction")
elif magnitude >= 9.0:
    print("Causes unbelievable damage")
else:
    print("Magnitude value is not set properly")