import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router'; // Import useRouter
import { client } from '../../sanity/lib/client'; // Import the Sanity client

// Define the product type
interface Product {
    _id: string;
    title: string;
    price: number;
    description: string;
    imageUrl: string;
}

const ProductPage = () => {
    const router = useRouter();
    const { id } = router.query; // Get the id from the URL
    const [product, setProduct] = useState<Product | null>(null);

    useEffect(() => {
        // Fetch product data if id is available
        if (id) {
            const fetchProduct = async () => {
                const data = await client.fetch(
                    `*[_type == "product" && _id == $id]{_id, title, price, description, "imageUrl": image.asset->url}`,
                    { id }
                );
                if (data && data.length > 0) {
                    setProduct(data[0]);
                }
            };

            fetchProduct();
        }
    }, [id]);

    if (!product) return <div>Loading...</div>; // Display loading state if product is not found

    return (
        <div className="p-8">
            <div className="max-w-2xl mx-auto bg-white shadow rounded p-6">
                <img
                    src={product.imageUrl}
                    alt={product.title}
                    className="w-full h-60 object-cover rounded"
                />
                <h1 className="text-2xl font-bold mt-4">{product.title}</h1>
                <p className="text-gray-500 mt-2">{product.description}</p>
                <p className="text-xl font-semibold mt-4">${product.price}</p>

                {/* Add to Cart Button (you can enhance this functionality later) */}
                <button className="mt-6 px-6 py-2 bg-blue-500 text-white rounded">Add to Cart</button>
            </div>
        </div>
    );
};

export default ProductPage;
