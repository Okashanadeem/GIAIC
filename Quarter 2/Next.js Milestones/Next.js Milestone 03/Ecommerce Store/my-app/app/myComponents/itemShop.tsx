import React, { useEffect, useState } from 'react';
import Link from 'next/link'; // Import Link from Next.js
import { client } from '../../sanity/lib/client'; // Import the Sanity client

// Define the product type
interface Product {
    _id: string;
    title: string;
    price: number;
    description: string;
    imageUrl: string;
}

const ItemsPage = () => {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        // Fetch products from Sanity
        const fetchProducts = async () => {
            const data = await client.fetch(`*[_type == "product"]{_id, title, price, description, "imageUrl": image.asset->url}`);
            setProducts(data);
        };

        fetchProducts();
    }, []);

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 p-8">
            {products.map((product) => (
                <Link key={product._id} href={`/product/${product._id}`}>
                <div className="bg-white shadow rounded p-4">
                    <img
                        src={product.imageUrl}
                        alt={product.title}
                        className="w-full h-40 object-cover rounded"
                    />
                    <h2 className="text-lg font-bold mt-2">{product.title}</h2>
                    <p className="text-gray-500">{product.description}</p>
                    <p className="text-gray-700 font-semibold">${product.price}</p>
                </div>
            </Link>
            
            ))}
        </div>
    );
};

export default ItemsPage;
