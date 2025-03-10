const productId = new URLSearchParams(window.location.search).get('id');

fetch(`/api/products/${productId}/`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('product-id').value = data.product.id;
        document.getElementById('name').value = data.product.name;
        document.getElementById('price').value = data.product.price;
    })
    .catch(error => {
        alert('Error fetching product for update');
        console.error('Error:', error);
    });

document.getElementById('update-product-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;
    const id = document.getElementById('product-id').value;

    fetch(`/api/products/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, price })
    })
    .then(response => response.json())
    .then(data => {
        alert('Product updated successfully');
        window.location.href = '/product_list/';
    })
    .catch(error => {
        alert('Error updating product');
        console.error('Error:', error);
    });
});
