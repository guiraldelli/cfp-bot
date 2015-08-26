// regex patter for finding the "key line" that classifies the email as "call for papers"
var regex_key_line = /((call\s+for\s+(paper|papers))|submission|deadline)/i; //ignore case
// regex pattern for finding the dates
// var regex_date = /((\d{1,2}/\d{1,2}/(\d{4}|\d{2}))|(\d{4}-\d{2}-\d{2})|(\d{1,2}(st|nd|rd|th)*\s*(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)(,)?\s*\d{1,2}(st|nd|rd|th)*\s*(\d{4}|\d{2}))|((Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s*\d{1,2}(st|nd|rd|th)*\s*(,)?\s*(\d{4}|\d{2})))/i;

function find_key_line(line){
    return regex_key_line.test(line);
}

// returns -1 if no match is found
// otherwise, returns the index of the match
// see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search
//  or https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions?redirectlocale=en-US&redirectslug=JavaScript%2FGuide%2FRegular_Expressions#Working_with_regular_expressions
function find_date(line){
    return line.search(regex_date);
}
