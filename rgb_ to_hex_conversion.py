# The rgb function is incomplete. Complete it so that passing
# in RGB decimal values will result in a hexadecimal representation
# being returned. Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3

def rgb(r, g, b):
    rgb = [0 if i < 0 else i for i in [r,g,b]]
    rgb = [255 if i > 255 else i for i in rgb]
    text = ''.join([f"{int(i):02x}" for i in rgb])
    return text.upper()

print(rgb(-1,2, 266))
print(rgb(0,0,0))