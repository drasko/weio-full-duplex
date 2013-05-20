/**
*
* WEIO Web Of Things Platform
* Copyright (C) 2013 Nodesign.net, Uros PETREVSKI, Drasko DRASKOVIC
* All rights reserved
*
*               ##      ## ######## ####  #######  
*               ##  ##  ## ##        ##  ##     ## 
*               ##  ##  ## ##        ##  ##     ## 
*               ##  ##  ## ######    ##  ##     ## 
*               ##  ##  ## ##        ##  ##     ## 
*               ##  ##  ## ##        ##  ##     ## 
*                ###  ###  ######## ####  #######
*
*                    Web Of Things Platform
*
* WEIO is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* WEIO is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
* 
* This file is part of WEIO.
*
* Authors : 
* Uros PETREVSKI <uros@nodesign.net>
* Drasko DRASKOVIC <drasko.draskovic@gmail.com>
*
**/
  
//var baseFiles = new SockJS(document.URL + '/baseFiles');
//var baseFiles = new WebSocket('ws://192.168.10.183:8081/' + 'editor/baseFiles');
  var weio = new SockJS('http://localhost:8081/' + 'api');


  var HIGH = "1";
  var LOW = "0";
  var OUTPUT = "out";
  var INPUT = "in";
  
  weio.onopen = function() {
      console.log('socket opened for weio API');
      
  };
  
  weio.onmessage = function(e) {
      data = JSON.parse(e.data);
      
  };
  
  weio.onclose = function() {
      console.log('socket is closed for editor');
      
  };
  
  
  function digitalWrite(pin, value) {
      var askWeio = { "request": "digitalWrite", "data" : [pin,value] };
      //	console.log(askWeio);
      weio.send(JSON.stringify(askWeio));
  };
  
  function pinMode(pin, mode) {
      var askWeio = { "request": "pinMode", "data" : [pin,mode] };
      weio.send(JSON.stringify(askWeio));
  };



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



