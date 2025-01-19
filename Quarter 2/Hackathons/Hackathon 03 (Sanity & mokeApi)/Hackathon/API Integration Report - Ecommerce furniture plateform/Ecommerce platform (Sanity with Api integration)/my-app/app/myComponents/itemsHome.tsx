'use client'
import React, { useEffect, useState } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { client } from '@/sanity/lib/client';

interface Product {
  _id: string;
  title: string;
  price: number;
  productImage: string;
}

export default function ItemsPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      const fetchedProducts: Product[] = await client.fetch(
        `*[_type == "product"][0..3]{_id, title, price, "productImage": productImage.asset->url}`
      );
      setProducts(fetchedProducts);
      setLoading(false);
    };

    fetchProducts();
  }, []);

  if (loading) {
    return <div className="text-center py-10">Loading products...</div>;
  }

  return (
    <div className="w-full px-6 py-10 md:px-12 lg:px-16 bg-gray-50">
      <h2 className="text-center text-2xl md:text-4xl font-bold text-gray-800 mb-8">
        Our Featured Products
      </h2>

      {/* Items List */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        {products.map((product) => (
          <div
            key={product._id}
            className="flex flex-col items-center bg-white shadow-lg p-5 rounded-lg hover:shadow-xl transform hover:scale-105 transition duration-300 ease-in-out"
          >
            <Image
              src={product.productImage}
              alt={product.title}
              className="h-[250px] w-full object-cover rounded-md border-2 border-gray-200"
              width={250}
              height={250}
            />
            <h4 className="text-center mt-4 font-semibold text-lg text-gray-700">
              {product.title}
            </h4>
            <p className="text-center text-gray-500 mt-2 text-sm">
              Rs. {product.price.toLocaleString()}
            </p>
            <Link
              href={`/product/${product._id}`}
              className="mt-4 bg-black text-white px-6 py-2 rounded-md text-sm font-medium hover:bg-gray-800 transition duration-300"
            >
              View Details
            </Link>
          </div>
        ))}
      </div>

      {/* View More Link */}
      <div className="mt-10 flex justify-center">
        <Link
          href="/"
          className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4 
               hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105"
        >
          View More Products
        </Link>
      </div>
    </div>
  );
}
