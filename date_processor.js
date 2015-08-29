// regex pattern for finding the dates
var REGEX_DATE = /((\d{1,2}/\d{1,2}/(\d{4}|\d{2}))|(\d{4}-\d{2}-\d{2})|(\d{1,2}(st|nd|rd|th)*\s*(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)(,)?\s*\d{1,2}(st|nd|rd|th)*\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*\d{1,2}(st|nd|rd|th)*\s*(,)?\s*(\d{4}|\d{2})))/i;
// ISO format for dates
var DATE_ISO_FORMAT = "yyyy-MM-dd";

// gets a mathced date from regex and converts to a string in the ISO format
// using the Datejs library
function get_iso_date(matched_date){
    Date.parse(matched_date).toString(DATE_ISO_FORMAT);
}

// returns the matched date found in the line
function get_literal_date(line){
    return line.match(REGEX_DATE);
}

// verifies if a line contains a date
// returning a true value in positive case
function has_date(line){
    return REGEX_DATE.test(line);
}
