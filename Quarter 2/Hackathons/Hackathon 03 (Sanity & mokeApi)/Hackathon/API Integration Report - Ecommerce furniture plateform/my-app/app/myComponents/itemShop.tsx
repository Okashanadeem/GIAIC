import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { client } from '../../sanity/lib/client';// is cliet ko commen kr do jab api se data fetch krna ho.
import Image from 'next/image';
import imageUrlBuilder from '@sanity/image-url';

//postinng content on sanity from the api
//this code will be commented after it it is used once.


// import { createClient } from '@sanity/client';

// const client = createClient({
//   projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID,
//   dataset: 'production',
//   useCdn: true,
//   apiVersion: '2025-01-13',
//   token: process.env.SANITY_API_TOKEN,
// });



// async function uploadImageToSanity(imageUrl: string) {
//   try {
//     console.log(`Uploading image: ${imageUrl}`);

//     const response = await fetch(imageUrl);
//     if (!response.ok) {
//       throw new Error(`Failed to fetch image: ${imageUrl}`);
//     }

//     const buffer = await response.arrayBuffer();
//     const bufferImage = Buffer.from(buffer);

//     const asset = await client.assets.upload('image', bufferImage, {
//       filename: imageUrl.split('/').pop(),
//     });

//     console.log(`Image uploaded successfully: ${asset._id}`);
//     return asset._id;
//   } catch (error) {
//     console.error('Failed to upload image:', imageUrl, error);
//     return null;
//   }
// }

// interface Product {
//     title: string;
//     description: string;
//     imageUrl: string;
//     price: number;
//     tags?: string[]; // optional
//     discountPercentage?: number; // optional
//     isNew?: boolean; // optional
//   }


// async function uploadProduct(product: Product) {
//   try {
//     const imageId = await uploadImageToSanity(product.imageUrl);

//     if (imageId) {
//       const document = {
//         _type: 'product',
//         title: product.title,
//         price: product.price,
//         productImage: {
//           _type: 'image',
//           asset: {
//             _ref: imageId,
//           },
//         },
//         tags: product.tags,
//         discountPercentage: product.discountPercentage,
//         description: product.description,
//         isNew: product.isNew,
//       };

//       const createdProduct = await client.create(document);
//       console.log(`Product ${product.title} uploaded successfully:`, createdProduct);
//     } else {
//       console.log(`Product ${product.title} skipped due to image upload failure.`);
//     }
//   } catch (error) {
//     console.error('Error uploading product:', error);
//   }
// }

// async function importProducts() {
//   try {
//     const response = await fetch('https://template6-six.vercel.app/api/products');

//     if (!response.ok) {
//       throw new Error(`HTTP error! Status: ${response.status}`);
//     }

//     const products = await response.json();

//     for (const product of products) {
//       await uploadProduct(product);
//     }
//   } catch (error) {
//     console.error('Error fetching products:', error);
//   }
// }

// importProducts();



// Creating the image URL builder
const builder = imageUrlBuilder(client);

function urlFor(source: any) {
    // Check if source exists and is valid
    if (source) {
        return builder.image(source);
    }
    return null; // Return null if the source is invalid...
}

interface Product {
    _id: string;
    title: string;
    price: number;
    description: string;
    productImage: any; // Sanity image field (updated from 'image' to 'productImage')
}

const ItemsPage = () => {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const fetchProducts = async () => {
            // Fetch products and their productImage from sanity...
            const data = await client.fetch(
                `*[_type == "product"]{_id, title, price, description, productImage}`
            );
            setProducts(data);
        };

        fetchProducts();
    }, []);

    const truncateDescription = (description: string, length: number) => {
        if (description.length > length) {
            return description.substring(0, length) + '...';
        }
        return description;
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 p-8">
            {products.map((product) => (
                <Link key={product._id} href={`/product/${product._id}`}>
                    <div className="bg-white shadow rounded p-4">
                        <Image
                            src={urlFor(product.productImage)?.width(500).url() || '/images/default-image.jpg'} // Correct path to the default image in the public folder
                            alt={product.title}
                            width={500}
                            height={300}
                            className="w-full h-40 object-cover rounded"
                            priority
                        />
                        <h2 className="text-lg font-bold mt-2">{product.title}</h2>
                        <p className="text-gray-500">{truncateDescription(product.description, 100)}</p>
                        <p className="text-gray-700 font-semibold">${product.price}</p>
                    </div>
                </Link>
            ))}
        </div>
    );
};

export default ItemsPage;
