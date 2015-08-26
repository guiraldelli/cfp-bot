var UNREAD_THREADS_QUERY = "is:unread";

// get an array unread threads from GMail
function get_unread_threads(){
    return GmailApp.search(UNREAD_THREADS_QUERY);
}

// given an array of unread GMail threads, composes an array of unread messages
function get_unread_messages(unread_threads){
    return unread_threads.reduce(reduce_unread_messages, []);
}

// reduce function in which all unread messages are merged in a single array
function reduce_unread_messages(previousValue, currentValue){
    // var messages = currentValue.getMessages();
    // var unread = messages.filter(is_message_unread);
    // return previousValue.concat(unread);
    return previousValue.concat(currentValue.getMessages().filter(is_message_unread));
}

// filter function which says if a GMail message is unread or not
function is_message_unread(gmail_message){
    return gmail_message.isUnread();
}

// returns the plain body text of a GMail message
function get_message_text(gmail_message){
    return gmail_message.getPlainBody();
}

// main function, which returns the plain text body of all unread GMail messages
function get_body_all_unread_messages(){
    return get_unread_messages(get_unread_threads()).map(get_message_text);
}

// debug function
function debug(){
    Logger.log("Unread messages:\n%s", get_body_all_unread_messages());
}
