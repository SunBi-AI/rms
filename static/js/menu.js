function fetchSubcategories() {
    const categoryId = document.getElementById('category-select').value;

    // Make an AJAX request to fetch the subcategories
    fetch(`/subcategories/${categoryId}/`)
        .then(response => response.json())
        .then(data => {
            const subcategorySelect = document.getElementById('subcategory-select');
            // Clear existing options
            subcategorySelect.innerHTML = '';

            // Populate new options
            data.forEach(subcategory => {
                const option = document.createElement('option');
                option.value = subcategory.id;
                option.textContent = subcategory.name;
                subcategorySelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching subcategories:', error));
}