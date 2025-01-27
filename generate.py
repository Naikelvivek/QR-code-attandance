from MyQR import myqr
import os
import base64

f = open('students.txt', 'r')
lines = f.read().split("\n")
f.close()  # It's a good practice to close the file after reading it
print(lines)

for i in range(len(lines)):
    if lines[i]:  # Check if the line is not empty
        data = lines[i].encode()
        name = base64.b64encode(data)
        version, level, qr_name = myqr.run(
            str(name),
            level='H',
            version=1,
            
            picture='bg.png',
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=str(lines[i] + '.bmp'),
            save_dir=os.getcwd()
        )
