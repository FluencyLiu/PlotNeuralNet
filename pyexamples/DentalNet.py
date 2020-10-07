
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *
from pycore.diy_blocks import *

feat = [16,64,128]
base_width = 4
length = 40

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    # to_input( '../examples/fcn8s/cats.jpg' ),
    # to_ConvHidden_simple(name='image', offset="(0,0,0)", to="(0,0,0)", width=length, height=length, depth=length ),

    # encoder
    # down0
    to_ConvHidden_simple(name='down0', offset="(2,0,0)", to="(0,0,0)", width=base_width, height=length/2, depth=length/2 ),
    start_connection("down0", pos=(0, -1)),

    # down1
    to_ConvHidden_simple(name='down1', offset="(1,0,0)", to='(down0-east)', width=base_width/feat[0]*feat[1], height=length/4, depth=length/4 ),
    to_connection("down0", "down1"),

    # down2
    to_ConvHidden_simple(name='down2', offset="(1,0,0)", to='(down1-east)', width=base_width/feat[0]*feat[2], height=length/8, depth=length/8 ),
    to_connection("down1", "down2"),

    # branch1
    to_ConvHidden_simple_cyan(name='up1-2', offset="(4,0,-20)", to='(down2-east)', width=base_width/feat[0]*feat[1], height=length/4, depth=length/4, opacity=(0.5, 0.5) ),
    to_shift_connection( "down2", "up1-2", pos=(1.5,-2.5)),

    to_ConvHidden_simple_cyan(name='up1-1', offset="(1,0,0)", to='(up1-2-east)', width=base_width, height=length/2, depth=length/2, opacity=(0.5, 0.5) ),
    to_connection( "up1-2", "up1-1"),

    end_connection("up1-2"),

    # branch2
    to_ConvHidden_simple_cyan(name='up2-2', offset="(4,0,0)", to='(down2-east)', width=base_width/feat[0]*feat[1], height=length/4, depth=length/4, opacity=(0.5, 0.5) ),
    to_connection( "down2", "up2-2"),

    to_ConvHidden_simple_cyan(name='up2-1', offset="(1,0,0)", to='(up2-2-east)', width=base_width, height=length/2, depth=length/2, opacity=(0.5, 0.5) ),
    to_connection( "up2-2", "up2-1"),

    end_connection("up2-2"),

    # branch3
    to_ConvHidden_simple_cyan(name='up3-2', offset="(4,0,25)", to='(down2-east)', width=base_width/feat[0]*feat[1], height=length/4, depth=length/4, opacity=(0.5, 0.5) ),
    to_shift_connection( "down2", "up3-2", pos=(1.5,-2.5)),

    to_ConvHidden_simple_cyan(name='up3-1', offset="(1,0,0)", to='(up3-2-east)', width=base_width, height=length/2, depth=length/2, opacity=(0.5, 0.5) ),
    to_connection( "up3-2", "up3-1"),

    end_connection("up3-2"),

     
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
