#!/usr/bin/env python
# usage: unz.py infile outfile [start offset]
import zlib, sys
inf = open(sys.argv[1],"rb")
off = 0
#if len(sys.argv)>3: off = int(sys.argv[3],16)
if len(sys.argv)>3: off = int(sys.argv[3])
inf.seek(off)
cdata = inf.read()
# auto-detect zlib/gzip/deflate
# http://stackoverflow.com/a/22310760/422797
d = zlib.decompressobj(-zlib.MAX_WBITS)
udata = d.decompress(cdata)
udata += d.flush()

clen = len(cdata) - len(d.unused_data)
ulen = len(udata)

open(sys.argv[2],"wb").write(udata)
print("%d -> %d; end of data: %08X" % (clen, ulen, off+clen))
