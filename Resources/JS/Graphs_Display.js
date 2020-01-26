function getData(){
    var body = document.getElementsByClassName('body')[0];
    var year ="";
    var amount = 0;
    var polar_bear_data ="";
    $.get("https://lc-project-d2adc.firebaseio.com/.json", function(data,status){
        polar_bear_data = data["lc-project-d2adc"].polarbears["-LzYdr5SUMz63A83_NtC"];
        polar_bear_data.forEach(function(value , key){
            year = value.year;
            amount = value["Estimate of amount of polar bears"];
            var code = '<h1>'+ year +'</h1>' + '<br\>' + '<h1>'+ amount +'</h1>';
            body.append(code);
        });
    });
    
}

getData();