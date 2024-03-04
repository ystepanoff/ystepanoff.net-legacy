$(document).ready(function () {
    $(".mr-auto .nav-item").bind("click", function (event) {
        var clickedItem = $(this);
        $(".mr-auto .nav-item").each(function () {
            $(this).removeClass("active");
        });
        clickedItem.addClass("active");
    });

    $("#contactButton").click(function () {
        $.ajax({
            type: "POST",
            url: "/contact/",
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                contactName: $("#contactName").val(),
                contactEmail: $("#contactEmail").val(),
                contactMessage: $("#contactMessage").val(),
            },
            success: () => {
                alert("Message was sent. Thank you!");
            }
        });
    });
});
