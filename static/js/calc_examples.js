$.get("/example", (data) => {
    $('#paint_used').text(data[0].paint);
    $('#canvas_selected').text(data[0].canvas);
    $('#weather_condition').text(data[0].weather);
    $('#total_dry_time').text(data[0].total);

    $('#paint_used').text(data[1].paint);
    $('#canvas_selected').text(data[1].canvas);
    $('#weather_condition').text(data[1].weather);
    $('#total_dry_time').text(data[1].total);

    $('#paint_used').text(data[2].paint);
    $('#canvas_selected').text(data[2].canvas);
    $('#weather_condition').text(data[2].weather);
    $('#total_dry_time').text(data[2].total);

    $('#paint_used').text(data[3].paint);
    $('#canvas_selected').text(data[3].canvas);
    $('#weather_condition').text(data[3].weather);
    $('#total_dry_time').text(data[3].total);

    $('#paint_used').text(data[4].paint);
    $('#canvas_selected').text(data[4].canvas);
    $('#weather_condition').text(data[4].weather);
    $('#total_dry_time').text(data[4].total);
});