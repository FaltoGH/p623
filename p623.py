with open("/home/data/colorP6File.ppm","rb") as f:
 lines=f.readlines()
assert len(lines)==5
first_line=lines[0]
assert first_line[0]==ord('P')
assert first_line[1]==ord('6')
n=ord('\n')
assert first_line[2]==n
comment=lines[1]
assert comment[0]==ord('#')
tokens=lines[2].split()
width=int(tokens[0])
height=int(tokens[1])
data=lines[4]
maxval=int(lines[3])
assert maxval==255
datalen=len(data)
size=width*height
assert datalen==(size*3+height-1)
asciis=""
for i in range(height):
 for j in range(width):
  k=width*i+3*j+i
  r=data[k]
  g=data[k+1]
  b=data[k+2]
  s="%3d %3d %3d "%(int(r),int(g),int(b))
  asciis+=s
 asciis+="\n"
lines[4]=asciis.encode()
with open("colorP3File.ppm","wb") as f:
 f.writelines(lines)

