#!/bin/bash/env python
# coding=UTF-8

import Crypto.Random 
import base64

def generate_key(bits, encode=False):
    a = Crypto.Random.OSRNG.posix.DevURandomRNG()
    content = a.read(bits)
    
    if(encode):
        return base64.b64encode(content)

    return content

