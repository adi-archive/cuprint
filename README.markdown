# CUPrint

A project to make printing at Columbia University super-duper easy

# WISH LIST

 - Drag-n-drop!
 - Android interface!
 - Dynamic re-routing!
 - Maybe we could scrape the queue, and figure out if printers get heavily used during certain times
 - Display printer availability from Owl Printers
 - We can use rate of add to queue/rate of prints from queue/number of computers occupied in a lab to estimate load on a printer
 - Autocomplete UNIs? Only 8000 undergrads, prefix sharing should be usefully low
 - Geolocate (ish?) to estimate nearest printer
 - Pick more than one file
 - Pick more than one printer (fits with re-routing)
 - Drop-down menu -> buttons

# Current Status

 - Can specify printer and UNI.
 - Can enter # of copies and page ranges.
 - Double sided printing
 - Can print the following file formats 
 	- Portable Document Format (.pdf)
	- PostScript (.ps)
	- Open Document Formats (.odt,.odp,ods)
	- Microsoft Office 97-2003 Formats (.doc, .xls, .ppt)
	- Office Open XML Formats (.docx, .xlsx, .pptx)

# Dependencies
 - Flask (web interface)
 - PyCUPS (printing)
 - ZeroMQ (message passing)
 - PyZMQ (message passing)
 - Libreoffice/Openoffice (for file conversion)
 - Unoconv (for file conversion)

# Usage

 - To start the server, use `./manage.py runapp`. 
 - To run the worker, use `./manage.py runworker`.

