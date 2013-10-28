Packer.io Demo
===========

Create a virtual machine image from scratch

How do i run it?
==============

Packer reads a template configuration file in json format and installs the OS from the ISO file, applies the OS configuration from a .cfg file and package everything in a vagrant box format.


1. Download Packer from Packer.io [Download](http://www.packer.io/downloads.html) 
2. Run ```packer build virtualbox.json```

![packer ouput](http://github.com/lmayorga1980/packer-demo/raw/master/packer-image.png)