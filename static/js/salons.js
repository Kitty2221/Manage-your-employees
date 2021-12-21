$(document).ready(function () {
    $.ajax({
        url: '/api/v1/salons',
        method: 'GET',
        success: function (response) {
            for (let plant of response) {
                let el = " <li class='list-group-item'>" + salon.name + "</li>";
                $('#salons').append(el);
            }
        }
    })
});
