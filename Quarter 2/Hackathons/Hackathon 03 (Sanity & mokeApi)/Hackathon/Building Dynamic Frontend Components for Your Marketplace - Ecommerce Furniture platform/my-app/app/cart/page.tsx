'use client';
import Image from 'next/image';
import emptycart from "@/public/images/empty cart.png";
import logo from '../../public/images/Meubel House_Logos-05.png';
import { useCart } from '@/app/context/CartContext';
import Navbar from '../myComponents/Navbar';
import { ChevronRight } from 'lucide-react';
import Footer from '../myComponents/footer';

const CartPage = () => {
    const { cart, removeFromCart } = useCart();

    return (
        <div>

<Navbar />
            <div
                className="bg-cover bg-center bg-fixed pt-20 pb-24 "
                style={{
                    backgroundImage: "url('/images/Rectangle 1.png')",
                }}
            >
                <div className="flex flex-col items-center justify-center h-full px-4 md:px-8 lg:px-16">
                    <Image src={logo} alt='Logo' />
                    <h1 className='text-4xl'>Cart</h1>
                    <p className='flex'>Shop<ChevronRight /> Cart</p>
                </div>
            </div>

            <div className="p-8 bg-gray-50 min-h-screen">
                {cart.length === 0 ? (
                    <div className="flex flex-col items-center justify-center mt-20">
                        <Image
                            src={emptycart}
                            alt="Empty Cart"
                            className="mb-6 opacity-50"
                            width={160}
                            height={160}
                        />
                        <p className="text-lg font-semibold text-gray-600">Your cart is empty.</p>
                        <a
                            href="/shop"
                            className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4 
               hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105 mb-8"
                        >
                            Start Shopping
                        </a>
                        <Footer/>
                    </div>
                ) : (
                    <div className="space-y-6">
                        {cart.map((item) => (
                            <div
                                key={item._id}
                                className="flex items-center justify-between bg-white shadow-md rounded-lg p-4 hover:shadow-lg transition"
                            >
                                <div className="flex items-center gap-6">
                                    <Image
                                        src={item.imageUrl}
                                        alt={item.title}
                                        className="rounded-lg"
                                        width={80}
                                        height={80}
                                    />
                                    <div>
                                        <h2 className="text-xl font-semibold text-gray-700">
                                            {item.title}
                                        </h2>
                                        <p className="text-gray-500">
                                            ${item.price} x {item.quantity}
                                        </p>
                                        <p className="text-gray-700 font-medium">
                                            Total: ${(item.price * item.quantity).toFixed(2)}
                                        </p>
                                    </div>
                                </div>
                                <button
                                    className="px-4 py-2 text-red-500 bg-red-100 rounded-lg hover:bg-red-200 transition"
                                    onClick={() => removeFromCart(item._id)}
                                >
                                    Remove
                                </button>
                            </div>
                        ))}
                    </div>
                )}

                {cart.length > 0 && (
                    <div className="mt-10 bg-white shadow-lg rounded-lg p-6">
                        <h2 className="text-2xl font-bold text-gray-800">Order Summary</h2>
                        <div className="flex justify-between items-center mt-4 text-lg">
                            <span className="font-medium text-gray-600">Subtotal:</span>
                            <span className="font-bold text-gray-800">
                                $
                                {cart
                                    .reduce((total, item) => total + item.price * item.quantity, 0)
                                    .toFixed(2)}
                            </span>
                        </div>
                        <button
                            className="mt-6 w-full py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
                            onClick={() => alert('Proceed to Checkout')}
                        >
                            Checkout
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default CartPage;
