var smokealarm_url = "//example.com/errors/";
var smokealarm_data = {};
window.onerror = function(errorMessage, url, line) {
    var data = {
        error: errorMessage,
        file: url,
        line: line,
        url: document.location.href,
        additional_data: JSON.stringify(smokealarm_data)
    };
    $.ajax({
        type: "POST",
        url: smokealarm_url,
        data: data
    });
};

