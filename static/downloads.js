function updateProgress() {
    var request = new XMLHttpRequest(); // Create a request variable and assign a new XMLHttpRequest object to it.
    request.open('GET', 'http://localhost:'+location.port+'/query/all/info'); // Open a new connection, using the GET request on the URL endpoint
    request.send();
    
    request.onload = async function () {
        var data = JSON.parse(this.response);
        let table_string = `<table border=1>
        <tr><th>Name</th><th>Progress</th><th>Status</th><th>Toggle</th><th>Delete</th></tr>`;
    
        for(let key in data) {
            table_string += '<tr><td>'+data[key].name+'</td><td>'+data[key].progress+'</td><td>'+data[key].state+'</td><td><input type="submit" value="Pause/Resume"></td><td><input name=\"'+data[key].name+'\" type=\"checkbox\"></td></tr>';
        }
        table_string += '</table><br><input type=\"submit\" value=\"Delete All\" onclick=\"return deleteAll()\">';

        document.getElementById("table").innerHTML = table_string;
    }
}

function deleteAll() {
    var request = new XMLHttpRequest(); // Create a request variable and assign a new XMLHttpRequest object to it.
    request.open('GET', 'http://localhost:'+location.port+'/query/all/delete'); // Open a new connection, using the GET request on the URL endpoint
    request.send();
}

function pauseTorrent() {
    
}

function stopUpdating(updater) {
    clearInterval(updater);
}

const updater = setInterval(updateProgress, 5000);