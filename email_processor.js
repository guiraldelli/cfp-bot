// regex patter for finding the "key line" that classifies the email as "call for papers"
var REGEX_KEY_LINE = /((call\s+for\s+(paper|papers))|submission|deadline)/i; //ignore case
// regex for the line which contains paper submission deadline information
var REGEX_PAPER_DEADLINE = /(paper(s)?)*(submission|deadline)(paper(s)?)*/i;

// verifies if a line contains the information of a call for paper email,
// returning a true value in positive case
function has_key_line(line){
    return REGEX_KEY_LINE.test(line);
}

// verifies if the line contain the keywords for paper submission deadline date,
// returning a true value in positive case
function is_paper_deadline(line){
    return line.test(REGEX_PAPER_DEADLINE);
}

// takes a GmailMessage object and process it, extracting
function process_email(gmail_message){
    var subject = get_subject_text(gmail_message);
    var lines_body = break_lines(get_message_text(gmail_message));
    for (line in lines_body){
        if (has_date(line) && is_paper_deadline(line)){
            var date = get_date(get_literal_date(line));
            var calendar_event = create_event(subject, date);
            if (calendar_event == null){
                Logger.log("It was not possible to create an event with the following details:\n\tSubject: %s\n\tDate: %s", subject, date);
            }
            break;
        }
    }
}
