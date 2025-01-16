import React, { useEffect, useState } from 'react';
import Link from 'next/link';

// Define the product type
interface Product {
    id: string;
    name: string;
    description: string;
    price: number;
    image: string;
}

const ItemsPage = () => {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        // Fetch products from the Mock API
        const fetchProducts = async () => {
            try {
                const response = await fetch('https://6783a6208b6c7a1316f51701.mockapi.io/products');
                const data = await response.json();
                setProducts(data);
            } catch (error) {
                console.error('Error fetching products:', error);
            }
        };

        fetchProducts();
    }, []);

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 p-8">
            {products.map((product) => (
                <Link key={product.id} href={`/product/${product.id}`}>
                    <div className="bg-white shadow rounded p-4 hover:shadow-lg transition-shadow">
                        <img
                            src={product.image}
                            alt={product.name}
                            className="w-full h-40 object-cover rounded"
                        />
                        <h2 className="text-lg font-bold mt-2">{product.name}</h2>
                        <p className="text-gray-500">{product.description}</p>
                        <p className="text-gray-700 font-semibold">${product.price}</p>
                    </div>
                </Link>
            ))}
        </div>
    );
};

export default ItemsPage;
