$(document).ready(function () {
    $('#addCategoryButton').on('click', function () {
        var url = "/list_categories"; // Django URL for adding a category
        
        // Load content into the modal dynamically
        $('#addCategoryModal .modal-body').load(url, function (response, status, xhr) {
            if (status == "error") {
                console.error("Error loading content: " + xhr.status + " " + xhr.statusText);
            }
        });
    });
});