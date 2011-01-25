#!/usr/bin/env python

# Copyright (c) 2011, R. H. Gracini Guiraldelli <rguira@acm.org>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# Neither the name of the R. H. Gracini Guiraldelli nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import re
import parsedatetime.parsedatetime as pdt
import parsedatetime.parsedatetime_consts as pdc
import gdata.calendar
import gdata.calendar.service
import gdata.service
import atom
import time
import imaplib
import array

def load_file(filename):
    fp = None
    try:
        fp = open(filename, "r")
    except:
        sys.stderr.write("File not found!\n")
    return fp

def find_key_line(line):
    pattern = r"((call\s+for\s+(paper|papers))|submission|deadline)"
    regex = re.compile(pattern, re.IGNORECASE | re.UNICODE)
    found = regex.search(line)
    return found

def find_date(line):
#   FIXME: Let global these regex components
#   FIXME: define a config file where these regex could be
    pattern = r"((\d{1,2}/\d{1,2}/(\d{4}|\d{2}))|(\d{4}-\d{2}-\d{2})|(\d{1,2}(st|nd|rd|th)*\s*(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)(,)?\s*\d{1,2}(st|nd|rd|th)*\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*\d{1,2}(st|nd|rd|th)*\s*(,)?\s*(\d{4}|\d{2})))"
    regex = re.compile(pattern, re.IGNORECASE | re.UNICODE)
    found = regex.search(line)
    return found

def connect_google_calendar(username, password):
    calendar_service = gdata.calendar.service.CalendarService()
    calendar_service.email = username
    calendar_service.password = password
    calendar_service.source = "Call For Papers App - Beta Version"
    calendar_service.ProgrammaticLogin()
    return calendar_service

def create_calendar_event(calendar_service, title, date):
    event = gdata.calendar.CalendarEventEntry()
    event.title = atom.Title(text=title)
    content = "Deadline for submission @ " + title
    event.content = atom.Content(text=content)
    start_time = time.strftime('%Y-%m-%d', date)
    event.when.append(gdata.calendar.When(start_time = start_time, end_time = start_time))
    new_event = calendar_service.InsertEvent(event, '/calendar/feeds/default/private/full')
    return new_event

def connect_imap_server(username, password):
    imap_connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    imap_connection.login(username,password)
    return imap_connection

def disconnect_imap_server(imap_connection):
    imap_connection.close()
    imap_connection.logout()

def processing_emails(imap_connection):
    print ">> Processing e-mails..."
    status, count = imap_connection.select('[Gmail]/All Mail')
    print "\tYou have %s in the '[Gmail]/All Mail' folder." % (count)
    status, found = imap_connection.search(None, '(UNSEEN)')
    print "\tAnd you have %d unseen e-mail in that folder." % (len(found[0].strip()))
    regex = re.compile('(?<=(Subject:\s))(.*)')
    i = 0
    mails = []
    for mail_number in found[0].strip():
        try:
            status, data = imap_connection.fetch(mail_number, '(BODY[HEADER])')
            mail_header = regex.search(data[0][1])
            single_mail = []
            single_mail.append(mail_header.group(0).strip())
            status, data = imap_connection.fetch(mail_number, '(BODY[TEXT])')
            single_mail.append(data[0][1])
            if ( (single_mail[0] == '') or (single_mail[0] == None) or (single_mail[1] == '') or (single_mail[1] == None) ):
                print ">> WARNING: Message could not be processed. Flaggind it! <<"
                imap_connection.store(mail_number, '+FLAGS', '\\Flagged')
            mails.append(single_mail)
        except:
            print ">> WARNING: Could not fetch message of number %s <<" % (mail_number)
    return mails

def process_dates(mails):
# TODO: I must improve it: what if it does not parse the date? The array index will go wrong!
    dates = []
    c = pdc.Constants()
    date_parser = pdt.Calendar(c)
    for single_mail in mails:
        parsed_date = None
        matched_line = find_key_line(single_mail[1])
        matched_date = find_date(single_mail[1])
        if ( (matched_line != None) and (matched_date != None) ):
            parsed_date = date_parser.parseDateText(matched_date.group(0))
        else:
            pass
        dates.append(parsed_date)
    return dates

def main():
    username = raw_input("E-mail address: ")
    password = raw_input("Password: ")
    imap_connection = connect_imap_server(username, password)
    mails = processing_emails(imap_connection)
    disconnect_imap_server(imap_connection)
    dates = process_dates(mails)
    calendar_service = connect_google_calendar(username, password)
    for i in range(0,len(dates)):
        single_mail = mails[i]
        date = dates[i]
        print "\t Subject: '%s' and Date: '%s'" % (single_mail[0], date)
        try:
            new_event = create_calendar_event(calendar_service, single_mail[0], date)
        except:
            print ">> ERROR: Event could not be added to Google Calendar! <<"

if __name__ == "__main__":
    main()
