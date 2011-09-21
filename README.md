# CUPrint

A project to make printing at Columbia University super-duper easy

# WISH LIST

 - Drag-n-drop!
 - Android interface!
 - Dynamic re-routing!
 - Maybe we could scrape the queue, and figure out if printers get heavily used during certain times
 - We can use rate of add to queue/rate of prints from queue/number of computers occupied in a lab to estimate load on a printer
 - Actually, printers aren't that sexy
 - Autocomplete UNIs? Only 8000 undergrads, prefix sharing should be usefully low
 - Geolocate (ish?) to estimate nearest printer

# Current Status

 - Basic functionality implemented. 
 - Can specify printer and UNI.
 - Can enter # of copies and page ranges.
 - Only supports file formats supported natively by CUPS 
   (i.e. PostScript, PDF, and Image Formats).

# Dependencies
 - Flask
 - PyCUPS

# Usage

 - To start the server, use `./manage.py runapp`. 
