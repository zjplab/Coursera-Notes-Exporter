# Coursera-Notes-Exporter
Export Video Lecture Notes to docx file
Save parsed page source code into `source.txt` file and then run `export.py`

# To do

- [x] Add support for note export to docx file
- [x] Add support for automatic get page source

# Instruction 

* Download [Geckodriver](https://github.com/mozilla/geckodriver/releases), release to system path
* Install [Firefox](https://www.mozilla.org/en-US/firefox/new/)
* Run `firefox.exe -marionette -start-debugger-server 2828`
* Run `export.py`