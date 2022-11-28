def find_res(filename):
    with open(filename, 'rb') as img_file:
        img_file.seek(163)
        a = img_file.read(2)
        height = (a[0] << 8) + a[1]
        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
    print("Image Resolution is: ", width, "x",height)
find_res("Z:\Documents\Photos and Signature\Photos\GitHub Profile Pic (Current).jpg")