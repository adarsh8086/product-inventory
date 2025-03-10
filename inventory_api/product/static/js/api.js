// static/js/api.js

const API = {
    // Add a new product
    addProduct: async (name, price, stock) => {
        try {
            const response = await fetch('/api/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, price, stock })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error adding product:', error);
        }
    },

    // Update a product
    updateProduct: async (id, name, price, stock) => {
        try {
            const response = await fetch(`/api/update/${id}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, price, stock })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error updating product:', error);
        }
    },

    // Delete a product
    deleteProduct: async (id) => {
        try {
            const response = await fetch(`/api/delete/${id}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({})
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error deleting product:', error);
        }
    }
};
