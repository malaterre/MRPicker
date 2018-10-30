# MRPicker
Weird gzip

> $ file file1000.gz
> file1000.gz: gzip compressed data, max compression, from FAT filesystem (MS-DOS, OS/2, NT)

> $ gunzip file1000.gz
> gzip: file1000.gz: invalid compressed data--format violated


Extracted from DICOM files:

    $ gdcmraw -t 7101,1000 input.dcm file1000.gz
    $ gdcmraw -t 7101,1002 input.dcm file1002.gz

Because tag 7101,1002 is repeated (bitwise identical) only the first attribute from other files have been uploaded:

    $ gdcmraw -t 7101,1000 input1.dcm file1000_other1.gz
    $ gdcmraw -t 7101,1002 input2.dcm file1000_other2.gz
    $ gdcmraw -t 7101,1002 input3.dcm file1000_other3.gz
    $ gdcmraw -t 7101,1002 input4.dcm file1000_other4.gz


