// main function, which gets all unread GMail messages and process them all
function main(){
    Logger.log("Initiating the process of the call for papers emails...");
    get_unread_messages(get_unread_threads()).map(process_email);
    Logger.log("Execution is over.");
}
