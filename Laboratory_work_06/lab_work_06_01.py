from math import cos, sin

def function_1(a, x):
    return (cos(a)-cos(x))**2-(sin(a)-sin(x))**2

def function_2(a, x):
    return -4*sin((a-x)/2)**2*cos(a+x)

with open("input.txt", "r") as input_file, \
        open("output.txt", "w") as output_file:
    header = "    a       x        y1        y2"
    print(header)
    output_file.write(header + "\n")
    for line in input_file:
        a, x = line.split()
        output_line = "{0:7.2f} {1:7.2f} {2:9.4f} {3:9.4f}".format(float(a),
                                                                    float(x),
                                                                    function_1(float(a), float(x)),
                                                                    function_2(float(a), float(x)))
        print(output_line)
        output_file.write(output_line + "\n")
