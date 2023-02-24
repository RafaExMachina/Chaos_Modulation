"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, N=1024):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Vetor_media',   # will show up in GRC
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N=N
        self.rows_counter=0
        self.sum=0


    def work(self, input_items, output_items):
        """example: multiply with constant"""
        x=input_items[0]
        y=output_items[0]
        self.sum += np.sum(x,axis=0)
        self.rows_counter += len(x)
        y[:]=self.sum/self.rows_counter
        return len(output_items[0])
