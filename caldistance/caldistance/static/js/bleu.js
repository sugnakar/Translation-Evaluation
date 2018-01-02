   


var sent = "welcome to learn english language";
var sent1 = sent.split(" ");
var correct = sent1;
     function myfunction(){
        document.getElementById("originalTxt").innerHTML = sent;
        //alert(document.getElementById("txtTarget").value);
        var src = document.getElementById("txtTarget").value.split(" ");
 
        
          $.ajax('givetoPy',
            {
              type : 'post',
              async : false,

              success : function(resp) {
                  alert("bleu distance: " + resp.result);
                },
              error : function(
                  xhr,
                  status,
                  error) {
                alert("Error in processing the request.");
              },
              data : {
                'candidate' : JSON.stringify(src) , 'reference' : JSON.stringify(correct)
              },
            })          

     }