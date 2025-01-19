'use client';

import { useCart } from '@/app/context/CartContext';

interface CartButtonProps {
    product: {
        _id: string;
        title: string;
        price: number;
        imageUrl: string;
    };
}

const CartButton = ({ product }: CartButtonProps) => {
    const { addToCart } = useCart();

    const handleAddToCart = () => {
        addToCart({
            _id: product._id,
            title: product.title,
            price: product.price,
            imageUrl: product.imageUrl,
            quantity: 1,
        });
        alert('Product added successfully');
    };

    return (
        <button
            className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4 
               hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105"
            onClick={handleAddToCart}
        >
            Add To Cart
        </button>
    );
};

export default CartButton;
