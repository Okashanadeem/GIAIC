'use client'
import { useEffect, useState } from "react";
import Image from "next/image";
import Link from "next/link";

const ItemsPage = () => {
  const [products, setProducts] = useState<any[]>([]); // State to hold the products
  const [loading, setLoading] = useState(true); // Loading state

  // Fetching products from the API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res = await fetch("https://6783a6208b6c7a1316f51701.mockapi.io/products");
        const data = await res.json();
        setProducts(data); // Set the fetched data
      } catch (error) {
        console.error("Error fetching products:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  // Render the first three products
  const firstThreeProducts = products.slice(0, 4);

  return (
    <div className="w-full px-6 py-10 md:px-12 lg:px-16">
      {/* Items List */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {loading ? (
          <p className="text-center text-lg">Loading...</p>
        ) : (
          firstThreeProducts.map((item, index) => (
            <div
              key={index}
              className="flex flex-col items-center bg-white p-4 rounded-md shadow-lg"
            >
              <Image
                src={item.image} // Assuming the API returns a field called 'image' with the product image URL
                alt={item.name}
                className="h-auto w-full rounded-md"
                width={200}
                height={200}
              />
              <h4 className="text-center mt-4 font-semibold text-lg">{item.name}</h4>
              <p className="text-center text-gray-600 mt-2">{item.price}</p>
            </div>
          ))
        )}
      </div>

      {/* View More Link */}
      <p className="underline text-center text-lg md:text-2xl mt-10">
        <Link href={"/shop"}>View More</Link>
      </p>
    </div>
  );
};

export default ItemsPage;
