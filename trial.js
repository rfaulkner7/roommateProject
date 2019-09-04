const https = require("https");
const url = "https://us-central1-codingchallenge-3057f.cloudfunctions.net/app/genCode?phone=1233211233";
https.get(url, resp => {
    resp.setEncoding("utf8");
    let body = "";
    resp.on("data", data => {
        body += data;
    });
    resp.on("end", () => {
        // body = JSON.parse(body);
        console.log(body);
    });
});

//Async/await and verification of phone number w/ twilio
// When hitting submit on same number - change it
