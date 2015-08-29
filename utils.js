// modified from http://beckism.com/2010/09/splitting-lines-javascript/
// modified from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#Using_regular_expression_to_split_lines_with_different_line_endingsends_of_lineline_breaks
var LINE_BREAKS = /^.*((\r\n|\n|\r)|$)/gm;

function break_lines(string){
    // return string.match(LINE_BREAKS);
    return string.split(LINE_BREAKS);
}
