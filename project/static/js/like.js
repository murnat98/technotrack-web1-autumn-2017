$(document).on('click', 'button.like', function (e) {
    var post_data = $(this).data();

    $.ajax(
        {
            url: post_data.url,
            method: 'POST',
            data: post_data,
            async: true
        }
    ).done(function (data, status, response) {
        document.getElementById('likes-' + post_data.postid).innerHTML = data;
    });
});