

$.get("/example", (data) => {
    $('paint_used').text(`${data.paint_used}`);
    $('canvas_selected').text(`${data.canvas_selected}`);
    $('weather_condition').text(`${data.weather_condition}`);
    $('total_dry_time').text(`${data.total_dry_time}`);

    console.log(data)

});