// connects to Google Calendar and creates an event in the default calendar
// of the account
function create_event(title, date){
    return CalendarApp.getDefaultCalendar().createAllDayEvent(title, date);
}
