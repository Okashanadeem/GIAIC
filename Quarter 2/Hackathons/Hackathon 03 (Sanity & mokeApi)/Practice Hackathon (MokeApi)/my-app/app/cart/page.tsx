'use client';
import Image from 'next/image';
import { useCart } from '../context/CartContext';
import Navbar from '../myComponents/Navbar';
import { ChevronRight } from 'lucide-react';
import logo from '../../public/images/Meubel House_Logos-05.png';
import Footer from '../myComponents/footer';

const CartPage = () => {
  const { cartItems, removeFromCart } = useCart();

  if (cartItems.length === 0) {
    return (
      <div>
        <Navbar />
        <div
          className="bg-cover bg-center bg-fixed mt-12 pt-20 pb-24 mb-10"
          style={{
            backgroundImage: "url('/images/Rectangle 1.png')",
          }}
        >
          <div className="flex flex-col items-center justify-center h-full px-4 md:px-8 lg:px-16">
            <Image src={logo} alt='Logo' />
            <h1 className='text-4xl '>Cart</h1>
            <p className='flex'>Product <ChevronRight /> Cart</p>
          </div>
        </div>

        <div className="flex justify-center mt-12">
          <p className="text-xl font-semibold text-gray-600">Your cart is currently empty.</p>
        </div>
        <Footer />
      </div>
    );
  }

  return (
    <div>
      <Navbar />
      <div
        className="bg-cover bg-center bg-fixed mt-12 pt-20 pb-24 mb-10"
        style={{
          backgroundImage: "url('/images/Rectangle 1.png')",
        }}
      >
        <div className="flex flex-col items-center justify-center h-full px-4 md:px-8 lg:px-16">
          <Image src={logo} alt='Logo' />
          <h1 className='text-4xl'>Cart</h1>
          <p className='flex'>Product <ChevronRight /> Cart</p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-extrabold text-gray-900 mb-6">Your Cart</h1>

        <div className="space-y-6">
          {cartItems.map((item) => (
            <div key={item.id} className="flex justify-between items-center p-6 border border-gray-300 rounded-lg shadow-lg bg-white hover:shadow-xl transition duration-300 ease-in-out">
              <div className="flex items-center">
                <img src={item.image} alt={item.name} className="w-24 h-24 object-cover rounded-lg mr-6" />
                <div>
                  <h2 className="text-xl font-semibold text-gray-800">{item.name}</h2>
                  <p className="text-gray-600 text-lg">${item.price}</p>
                  <p className="text-gray-500">Quantity: {item.quantity}</p>
                </div>
              </div>
              <button
                onClick={() => removeFromCart(item.id)}
                className="text-red-600 font-semibold hover:text-red-800 transition duration-300"
              >
                Remove
              </button>
            </div>
          ))}
        </div>

        <div className="flex justify-between items-center mt-8 bg-gray-100 p-6 rounded-lg shadow-lg">
          <p className="text-lg font-semibold text-gray-900">
            Total: <span className="text-xl font-bold">${cartItems.reduce((total, item) => total + item.price * item.quantity, 0)}</span>
          </p>
          <button className="w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4">
            Checkout
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default CartPage;
