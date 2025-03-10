document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list');
            data.products.forEach(product => {
                const productItem = document.createElement('li');
                productItem.innerHTML = `${product.name} - $${product.price} 
                    <button onclick="deleteProduct(${product.id})">Delete</button>
                    <a href="update_product.html?id=${product.id}">Update</a>`;
                productList.appendChild(productItem);
            });
        });
});

function deleteProduct(id) {
    fetch(`/api/products/${id}/`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(() => {
        alert('Product deleted successfully');
        location.reload();
    })
    .catch(error => {
        alert('Error deleting product');
        console.error('Error:', error);
    });
}
