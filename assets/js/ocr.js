function process() {
    document.getElementById("xk").value;
    var req = {
        requests: [{
            features: [{
                type: "DOCUMENT_TEXT_DETECTION"
            }],
            image: {
                source: {
                    imageUri: document.getElementById("xurl").value
                }
            },
            imageContext = {
                languageHints: ["zh-handwrit"]
            }
        }]
    };
    var fullUrl = "https://vision.googleapis.com/v1/images:annotate?key=" + document.getElementById("xk").value;
    fetch(fullUrl, {
        method: "POST",
        body: JSON.stringify(req),
        headers: {
            "Content-Type": "application/json; charset=UTF-8"
        }
    }).then(function(response) {
        return response.json();
    }).then(res => {
        document.getElementById("xout").innerHTML = res.responses[0].fullTextAnnotation.text;
    }).catch(function(error) {
        document.getElementById("xout").innerHTML = error.toString();
    });
}