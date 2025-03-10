document.getElementById('add-product-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, price })
    })
    .then(response => response.json())
    .then(data => {
        alert('Product added successfully');
        window.location.href = '/product_list/';
    })
    .catch(error => {
        alert('Error adding product');
        console.error('Error:', error);
    });
});
