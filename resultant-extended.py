import math



def calculate_resultant():
    x_vectors = []
    y_vectors =[]
    while True:
        vector = input("\nEnter the size of vector or q to quit:")
        if vector== 'q':
            break
        else:
            vector_angle = input("Enter the angle between the vector and x axis(counter wise) :")

            x_value = float(vector)*math.cos(math.radians(float(vector_angle)))
            x_vectors.append(x_value)
            y_value = float(vector)*math.sin(math.radians(float(vector_angle)))
            y_vectors.append(y_value)

    

    total_x = sum(x_vectors)
    total_y = sum(y_vectors)

    
    
    resultant_size = round(math.sqrt(total_x**2+total_y**2),4)
    angle = round(math.degrees(math.atan(total_y/total_x)),4)

    print(f'\nYou have a resultant of {resultant_size} which makes a {angle} degree angle with the X axis\n')

calculate_resultant()

