---
layout: post
title: CSV to Address Book
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2012-07-21 23:55:13 +0200'
date_gmt: '2012-07-21 21:55:13 +0200'
tags:
- programming
- csv
- AppleScript
- Address Book
- Tech &amp; Gizmos
comments: []
---

Sending a few emails during the day had me realize that [the move from Sparrow to Mail](http://sesam.hu/2012/07/20/so-long-sparrow) raised the issue of Mail not autofilling addresses automatically. I suppose once I've written to that specific address Mail would "learn" it as well, but that sounded arduous.

The other choice was finally buckling down and entering my coworkers' data in Address Book. We have a Google Spreadsheet with contact info for everyone in the office. Only I just refused to enter close to a hundred names, addresses and phone numbers manually.

My first idea was using Automator, but there was no option to create an Address Book entry with it. So I moved on to Apple Script and it looked promising: I could parse a CSV file with it.

As step one I copied the entire Spreadsheet into Excel, removed the unnecessary columns, such as Skype ID, and had the names separated into first name and last name:

`=LEFT(A1,FIND(" ",A1,1)-1)`

The above function took the contents of the first cell, and copied the text leading up to the first space, excluding the space itself. This resulted in the family name in one cell. (Because in Hungary we write names in the family name, given name order.)

`=RIGHT(A1,LEN(A1)-FIND(" ",A1,1))`

This one took the content of the first cell, and copied the text from the right excluding the leading part until the first space, which is the family name. Worked well for people who had two last names as well.

Exported to CSV, and there I had the input data.

Then I set out to create a script that opened this file, parsed the values, checked for existing entries and if a name was missing from Address Book then added the data. Took me a couple of hours of reading documentation and googling for examples, but in the end:
    
    
    set csvData to read file ((path to home folder) & "Documents:hu-office.csv" as string)
    
    set csvEntries to paragraphs of csvData
    
    set existingPeople to 0
    set newPeople to 0
    
    repeat with i from 1 to count csvEntries
    	set {lastName, firstName, emailAddress, phoneNumber} to parseCsvEntry(csvEntries's item i)
    	tell application "Address Book"
    		set thePerson to (every person whose last name = lastName and first name = firstName)
    		if thePerson is not {} then
    			set existingPeople to existingPeople + 1
    		else
    			tell application "Address Book"
    				set thePersonNew to make new person with properties {first name:firstName, last name:lastName}
    				make new email at end of emails of thePersonNew with properties {label:"Work", value:emailAddress}
    				make new phone at end of phones of thePersonNew with properties {label:"Work", value:phoneNumber}
    				save
    			end tell
    			set newPeople to newPeople + 1
    		end if
    	end tell
    end repeat
    
    log existingPeople
    log newPeople
    
    to parseCsvEntry(csvEntry)
    	set AppleScript's text item delimiters to ","
    	set {fullName, lastName, firstName, email, foo, phone} to csvEntry's text items
    	set AppleScript's text item delimiters to {""}
    	return {lastName, firstName, email, phone}
    end parseCsvEntry

During this experiment I learned the following:

  * For usability's sake it would have been better to ask for an input file rather than hard coding it in the script but I just couldn't make it work. As a compromise at least the script runs fine if a properly named data file is placed in the user's Documents folder.
  * The script doesn't fail too gracefully when there is no input file either. Or if the data in the file is corrupted, etc.
  * During the process Excel or something messed up the character encoding of the CSV and the ő and ű letters came out as _. They had to be manually corrected.
  * Funnily enough, Excel wasn't even needed, I just failed to realize Google Docs does CSV exporting as well.
  * My formulas weren't dealing with the double spaces and trailing extra spaces in the name fields, which - as it later turned out - were left in the source document in abundance. More manual fixing for yours truly.
  * Apple Script is _very_ powerful.
