import Navbar from '@/app/myComponents/Navbar';
import Footer from '@/app/myComponents/footer';
import { client } from '../../../sanity/lib/client';
import { notFound } from 'next/navigation';
import CartButton from './CartButton';
import Link from 'next/link';

interface Product {
    _id: string;
    title: string;
    price: number;
    description: string;
    productImage: string;
    rating: number;
    tags: string[];
    discountPercentage?: number;
    isNew?: boolean;
    imageUrl: string;
}

async function getProductData(id: string): Promise<Product> {
    const data = await client.fetch(
        `*[_type == "product" && _id == $id]{
            _id, 
            title, 
            price, 
            description, 
            "productImage": productImage.asset->url, 
            rating, 
            tags, 
            discountPercentage, 
            isNew
        }`,
        { id }
    );

    if (data.length === 0) {
        return notFound();
    }

    return data[0];
}

const ProductPage = async ({ params }: { params: { id: string } }) => {
    const { id } = params;
    const product = await getProductData(id);

    const renderStars = (rating: number) => {
        return Array(5)
            .fill(0)
            .map((_, i) => (
                <span
                    key={i}
                    className={`inline-block text-lg ${i < rating ? 'text-yellow-500' : 'text-gray-300'}`}
                >
                    ★
                </span>
            ));
    };

    return (
        <div>
            <Navbar />
            <div className="flex flex-col lg:flex-row p-8 gap-8 lg:gap-16">
                {/* Image Section */}
                <div className="lg:w-1/2 flex justify-center">
                    <img
                        src={product.productImage}
                        alt={product.title}
                        className="w-full max-w-lg h-96 object-cover rounded-lg shadow-lg"
                    />
                </div>

                {/* Product Info Section */}
                <div className="lg:w-1/2">
                    <h1 className="text-3xl font-bold mb-4">{product.title}</h1>
                    <p className="text-xl font-semibold text-gray-700 mb-2">${product.price}</p>
                    <div className="flex items-center mb-4">{renderStars(product.rating)}</div>

                    {/* Discount Percentage */}
                    {product.discountPercentage && (
                        <p className="text-lg text-red-500 font-medium">
                            {product.discountPercentage}% off
                        </p>
                    )}

                    {/* New Badge */}
                    {product.isNew && (
                        <span className="text-sm font-semibold text-green-500 bg-green-100 px-2 py-1 rounded-lg">
                            New
                        </span>
                    )}

                    {/* Tags */}
                    {product.tags?.length > 0 && (
                        <div className="mt-6">
                            <h2 className="text-sm text-gray-500 mb-2">Tags</h2>
                            <div className="flex gap-4">
                                {product.tags.map((tag) => (
                                    <span
                                        key={tag}
                                        className="border border-gray-300 px-4 py-1 rounded-lg text-sm"
                                    >
                                        {tag}
                                    </span>
                                ))}
                            </div>
                        </div>
                    )}

                    {/* Sizes
                    <div className="mt-6">
                        <h2 className="text-sm text-gray-500 mb-2">Size</h2>
                        <div className="flex gap-4">
                            {['S', 'M', 'L', 'XL'].map((size) => (
                                <label
                                    key={size}
                                    htmlFor={size}
                                    className="flex items-center gap-2 cursor-pointer"
                                >
                                    <input
                                        type="radio"
                                        id={size}
                                        name="size"
                                        value={size}
                                        className="hidden"
                                    />
                                    <span className="border px-4 py-1 rounded-lg text-sm">
                                        {size}
                                    </span>
                                </label>
                            ))}
                        </div>
                    </div>

                    // colors
                    <div className="mt-6">
                        <h2 className="text-sm text-gray-500 mb-2">Color</h2>
                        <div className="flex gap-4">
                            {[
                                { name: 'Purple', color: 'bg-purple-500' },
                                { name: 'Black', color: 'bg-black' },
                                { name: 'Peach', color: 'bg-peachpuff' },
                            ].map(({ name, color }) => (
                                <label
                                    key={name}
                                    htmlFor={name}
                                    className="flex items-center gap-2 cursor-pointer"
                                >
                                    <input
                                        type="radio"
                                        id={name}
                                        name="color"
                                        value={name}
                                        className="hidden"
                                    />
                                    <span
                                        className={`w-6 h-6 rounded-full border ${color}`}
                                        title={name}
                                    ></span>
                                </label>
                            ))}
                        </div>
                    </div> */}
                    

                    {/* Buttons */}
                    <div className="mt-8 flex gap-4">
                        <CartButton product={product} />
                        <Link
                            href="/cart"
                            className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4 
                            hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105"
                        >
                            View Cart
                        </Link>
                    </div>
                </div>
            </div>

            <hr className="my-8" />

            {/* Additional Info */}
            <div className="px-8 lg:px-16">
                <div className="flex justify-around mb-8">
                    <p className="text-black text-lg font-medium cursor-pointer">Description</p>
                    <p className="text-gray-500 text-lg cursor-pointer">Additional Info</p>
                    <p className="text-gray-500 text-lg cursor-pointer">Reviews (5)</p>
                </div>
                <div className="text-gray-600 leading-relaxed">
                    {/* Description */}
                    <p className="mt-6 text-gray-700">{product.description}</p>
                </div>
            </div>

            <Footer />
        </div>
    );
};

export default ProductPage;
