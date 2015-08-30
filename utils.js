// empty string
var EMPTY_STRING = "";
// modified from http://beckism.com/2010/09/splitting-lines-javascript/
var LINE_BREAKS = /^.*((\r\n|\n|\r)|$)/gm;

function break_lines(string){
    return string.match(LINE_BREAKS);
}
