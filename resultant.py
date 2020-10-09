import math

first_vector = input("Enter First Vector: ")
second_vector = input("Enter Your second Vector : ")
angle = input("enter the angle between first and second vectors :")

def calculate_resultant(first_vector,second_vector,angle):
    first_vector = float(first_vector)
    second_vector =float(second_vector)
    angle = math.radians(float(angle))

    # calculate the size of resultant using the formula R^2=P^2+Q^2+2PQCosA
    resultant_size = math.sqrt((pow(first_vector,2)+pow(second_vector,2)+2*first_vector*second_vector*math.cos(angle)))

    # calculate the direction of resultant
    # tan alpha = (Q sin A)/ (p + Q cos A)

    # angle1 : angle between first vector(P) and the resultant vector
    
    angle1 = math.atan(second_vector*math.sin(angle)/(first_vector+second_vector*math.cos(angle)))

    return (resultant_size,angle1)

# it's time to call the function for duty

resultant = calculate_resultant(first_vector,second_vector,angle)
size = resultant[0]
angle = math.degrees(resultant[1])

print(f"\nThree is a vector of {size} \nAngle between first and resultant vector is {angle} degrees")

# It is working Guys :-)