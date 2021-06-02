// $.getJSON("/example", function(data) {

//     var ul = document.createElement('div');

//     for (var i = 0, len = data.length; 
//         i < len; i ++) {
//         var li = document.createElement('li');
//         var row = data[i]
//         li.innerText = "Paint Used: " + row['paint'] + " Canvas Selected:   " + row['canvas'] + " Weather Condition:   " + row['weather'] + " Total Dry time:   " +  row['total'];
//         ul.appendChild(li);
//         }
//     var element = document.getElementById("example");
//         element.appendChild(ul)

// });

$.getJSON("/example", function(data) {

    var ul = document.createElement('div');

    for (var i = 0, len = data.length; 
        i < len; i ++) {
        var p = document.createElement('p');
        var row = data[i]
        p.innerText = "Paint Used: " + row['paint'] + " Canvas Selected:   " + row['canvas'] + " Weather Condition:   " + row['weather'] + " Total Dry time:   " +  row['total'];
        ul.appendChild(p);
        }
    var element = document.getElementById("example");
        element.appendChild(ul)

});