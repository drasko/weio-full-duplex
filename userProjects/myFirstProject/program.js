function create_client() {
    var client_sockjs_url = 'http://localhost:8082/test';		 
    var client_sockjs = new SockJS(sockjs_url);

    client_sockjs.onopen    = function(){
         $('#consoleOutput').append("CLIENT SOCKJS OPENED" + "<br>");
    };
    
    client_sockjs.onmessage = function(e){
            var pydat = JSON.parse(e.data);
            $('#consoleOutput').append(pydat["name"]);
    };
    
    client_sockjs.onclose   = function(){
        $('#consoleOutput').append("CLIENT SOCKJS CLOSED");
    };
}
