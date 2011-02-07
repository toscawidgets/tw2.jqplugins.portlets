
/* Just a little helper method I add to the String class */
String.prototype.format = function() {
    var formatted = this;
    for(arg in arguments) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};


function makeIntoPortlet(id) {
    $("#" + id)
        .addClass("ui-widget ui-widget-content")
        .addClass("ui-helper-clearfix ui-corner-all")
        .find(".portlet-header")
        .addClass("ui-widget-header ui-corner-all")
        .prepend('<span class="ui-icon ui-icon-minus"></span>')
        .end()
        .find(".portlet-content");
    $("#" + id + " .portlet-header .ui-icon").click(function() {
        $(this).toggleClass("ui-icon-minus");
        $(this).toggleClass("ui-icon-plus");
        $(this).parents(".portlet:first").find(".portlet-content").toggle();
        saveOrder(); // This is important
    });
    $("#" + id + " .portlet-header .ui-icon").hover(
        function() {$(this).addClass("ui-icon-hover"); },
        function() {$(this).removeClass('ui-icon-hover'); }
    );
}

/* Create a portlet with id, title and content and attach it
 * to column 'column'
 */
function createPortlet(id, title, content, column) {
  var template = "<div class='portlet' id='{0}'><div class='portlet-header'>{1}</div><div class='portlet-content'>{2}</div></div>";
  var target = template.format(id, title, content);
  $('#' + column).append(target);
  makeIntoPortlet(id);
}


// function that writes the list order to a cookie
function saveOrder() {
    if ($.cookie == null) { return; }
    $(".column").each(function(index, value){
        var colid = value.id;
        var cookieName = "cookie-" + colid;
        // Get the order for this column.
        var order = $('#' + colid.replace(/:/g, '\\:')).sortable("toArray");
        // For each portlet in the column
        for ( var i = 0, n = order.length; i < n; i++ ) {
            // Determine if it is 'opened' or 'closed'
            var v = $('#' + order[i].replace(/:/g, '\\:'))
                .find('.portlet-content').is(':visible');
            // Modify the array we're saving to indicate what's open and
            //  what's not.
            order[i] = order[i] + ":" + v;
        }
        $.cookie(cookieName, order, { path: "/", expiry: new Date(2012, 1, 1)});
    });
}

// function that restores the list order from a cookie
function restoreOrder() {
    if ($.cookie == null) { return; }
    $(".column").each(function(index, value) {
        var colid = value.id;
        var cookieName = "cookie-" + colid
        colid = colid.replace(/:/g, '\\:');
        var cookie = $.cookie(cookieName);
        if ( cookie == null ) { return; }
        var IDs = cookie.split(",");
        if ( IDs[0] == '' ) { return; }
        for (var i = 0, n = IDs.length; i < n; i++ ) {
            var toks = IDs[i].split(":");
            var portletID = toks.slice(0, toks.length-1).join('\\:');
            var visible = toks[toks.length-1]
            var portlet = $(".column")
                .find('#' + portletID)
                .appendTo($('#' + colid));
            if (visible === 'false') {
                portlet.find(".ui-icon").toggleClass("ui-icon-minus");
                portlet.find(".ui-icon").toggleClass("ui-icon-plus");
                portlet.find(".portlet-content").hide();
            }
        }
    });
} 

$(document).ready( function () {
    $(".column").sortable({
        connectWith: ['.column'],
        stop: function() { saveOrder(); }
    }); 
}); 
