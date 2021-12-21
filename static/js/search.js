$(document).on("click", "#search", function (e) {
    e.preventDefault();
        let search_term = $('input[name=q]').val().toLowerCase();
    console.log(search_term )
        $.ajax(
            {
                type: "POST",
                url: "/api/v1/search",
                data: { "q": search_term },
                success: function (response) {
                        $("#searchResults").empty(); //remove whatever is there and append whatever is returned
                        $("#searchResult").append(response.result) //append whatever you want to append
                }
            }
        )

});
