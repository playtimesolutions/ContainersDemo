var http = require('http');
var os = require("os")

var app = http.createServer(function(req,res){
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({
        runtime: 'nodejs',
        hostname: os.hostname(),
        dateTimeUtc: new Date(new Date().toUTCString())
    }));
});
app.listen(80);