
from .tikzeng import *

# Conv
def to_Conv_simple( name, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_ConvHidden_simple( name, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_ConvHidden_simple_cyan( name, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" ", opacity=(0.5, 0.5) ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        fill={rgb:blue,2;green,1;black,0.3},
        bandfill={rgb:blue,2;green,1;black,0.5},
        opacity="""+ str(opacity[0]) +""",
        bandopacity="""+ str(opacity[1]) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_shift_connection( of, to, pos=(1, -1)):
    return r"""
\draw ("""+ of +"""-east)+("""+ str(pos[0]) +""",0,0,) coordinate ("""+of+"""-out);
\draw ("""+ to +"""-west)+("""+ str(pos[1]) +""",0,0) coordinate ("""+to+"""-in);
\draw [connection]  ("""+of+"""-east)  
-- node {\midarrow}("""+of+"""-out)
-- node {\midarrow}("""+to+"""-in)
-- node {\midarrow} ("""+to+"""-west);
"""

def to_interspace_connection( of, to, pos=(1, -1)):
    return r"""
\draw ("""+ of +"""-east)+("""+ str(pos[0]) +""",0,0,) coordinate ("""+of+"""-out);
\draw ("""+ to +"""-west)+("""+ str(pos[1]) +""",0,0) coordinate ("""+to+"""-in);
\draw [connection]  ("""+of+"""-out)
-- node {\midarrow}("""+to+"""-in);
"""

def start_connection( to, pos=(1, -1)):
    return r"""
\draw ("""+ str(pos[0]) +""",0,0) coordinate (out);
\draw ("""+ to +"""-west)+("""+ str(pos[1]) +""",0,0) coordinate ("""+to+"""-in);
\draw [connection]  (out)
-- ("""+to+"""-in);
"""
# \draw [connection]  (out)
# -- node {\midarrow}("""+to+"""-in);

def end_connection( of, pos=(3, 4)):
    return r"""
\draw ("""+ of +"""-east)+("""+ str(pos[0]) +""",0,0,) coordinate ("""+of+"""-out);
\draw ("""+ of +"""-east)+("""+ str(pos[1]) +""",0,0) coordinate ("""+of+"""-in);
\draw [densely dashed]  ("""+of+"""-out)
-- ("""+of+"""-in);
"""
# \draw [connection]  ("""+of+"""-out)
# -- node {\midarrow}("""+of+"""-in);

