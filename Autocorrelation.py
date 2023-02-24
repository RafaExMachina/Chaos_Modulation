
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, N=1024):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Autocorrelacao',   # will show up in GRC
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.N = N

    def work(self, input_items, output_items):
        x=input_items[0]
        y=output_items[0]

        L=x.shape

        for i in list(range(L[0])):
            y[i][:]=np.correlate(x[i],x[i],mode='same')/self.N

        return len(output_items[0])


