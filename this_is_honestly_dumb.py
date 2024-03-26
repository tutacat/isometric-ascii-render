#!/bin/env python3
import enum

class Direction(enum.Enum):
    down = 0
    up = 1
    north = 2
    east = 3
    south = 4
    west = 5

class Vector3(tuple):
    x = 0
    y = 0
    z = 0
    def __init__(self,x=0,y=0,z=0):
        self.value=(x,y,z)
        del self.up,self.down,self.north,self.east,self.south,self.west
    def __mul__(self,mul):
        methods = mul.__dir__()
        if "__float__" in methods:
            return Vector3(self.x*float(mul),self.y*float(mul),self.z*float(mul))
        elif "__iter__" in methods:
            mul = tuple(mul)
            if len(mul)==3:
                    return Vector3(self.x*float(mul[0]),self.y*float(mul[1]),self.z*float(mul[2]))
            else:
                raise ValueError("Expected length 3")
            
    up = Vector3(0,1,0)
    down = Vector3(0,-1,0)
    north = Vector3(0,0,1)
    east = Vector3(1,0,0)
    south = Vector3(0,0,-1)
    west = Vector3(-1,0,0)
    def value_get(self):
        return (self.x,self.y,self.z)
    def value_set(self, position):
        self.x,self.y,self.z=position
    def value_del(self):
        return
    value = property(value_get,value_set,value_del)
    

block_shapes: {
 0: {
 "name": "none",
 "render": False,
 "south": False,
 "west": False,
 "north": False,
 "top": False,
 "middle": False,
 "bottom": False,
 "slab": 0
 },
 1: {
 "name": "block",
 "render": True,
 "south": True,
 "west": True,
 "north": True,
 "top": True,
 "middle": False,
 "bottom": True,
 "slab": 0
 },
 2: {
 "name":"bottom_half"
 "render": True,
 "south": True,
 "west": True,
 "north": True,
 "top": False,
 "middle": True,
 "bottom": True,
 "slab": 1
 },
 3: {
 "name":"top_half"
 "render": True,
 "south":True,
 "west":True,
 "north":True,
 "top":True,
 "middle":True,
 "bottom": False,
 "slab":2
 }
}

shape_ids = {s["name"]:s for s in block_shapes}

blocks_data = {
    0: {
        "name": "air",
        "shape": "none",
    1: "stone"
    2: "slab_bottom",
    3: "slab_top",
}

block_ids: {b["name"]:b for b in blocks_data}




frame_symbol = { # what do you mean
 " ": "air"
 "#": "stone"
}
frame_blocks = back to the front
[
 ["     ",
  "    #",
  "   # ",
  "     ",],
 [
  "     ",
  "  #  ",
  "  #  "
 "#####",
  ]
]
frame_blocks = tiny demo
[
 [
 " # "
 "###",
  ]
]

block_w = 12
block_h = 6
z_scale = 0.5


# back to front, upside down
for i in range(len(frame_blocks)):
    frame_blocks[i].reverse()

size_z = len(frame_blocks)
size_y = len(frame_blocks[0])
size_x = len(frame_blocks[0][0])

output_h = max(block_h * size_y, block_h * z_scale * size_z) + 1
output_w = max(block_w * size_x, block_w * z_scale * size_z) + 1

output = [" " * output_w] * output_h

x=0
y=0
z=0

while z <= size_z: # z order
    while y <= min(size_y,len(frame_blocks[z]):
        while x <= min(size_x, len(frame_blocks[z][y])):
            block = frame_symbol[frame_blocks[z][y][x]]
            block_id = block_names
            x += 1
        y += 1
    z += 1
