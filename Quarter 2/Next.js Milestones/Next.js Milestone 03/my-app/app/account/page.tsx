import React from 'react'
import Navbar from '../myComponents/Navbar'
import Image from 'next/image'
import { ChevronRight } from 'lucide-react'
import logo from '../../public/images/Meubel House_Logos-05.png';
import Footer from '../myComponents/footer';

const Page = () => {
  return (
    <div>
        <Navbar />
            {/* Hero Section */}
            <div
                className="bg-cover bg-center bg-fixed mt-12 pt-20 pb-24 mb-10"
                style={{
                    backgroundImage: "url('/images/Rectangle 1.png')",
                }}
            >
                <div className="flex flex-col items-center justify-center h-full px-4 md:px-8 lg:px-16">
                    <Image src={logo} alt='Logo' />
                    <h1 className="text-4xl">My Account</h1>
                    <p className="flex items-center text-sm">
                        Home <ChevronRight /> My Account
                    </p>
                </div>
            </div>

            <div className="flex flex-col md:flex-row justify-center gap-10 m-8 lg:gap-24 lg:px-16">
                            {/* Contact Form */}
                <div className="flex flex-col gap-4">
                    <h1 className='text-3xl font-semibold mb-5'>Log In</h1>
                    <div>
                        <p className="mb-4 font-semibold text-sm">Username or email address</p>
                        <input
                            type="text"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div>
                        <p className="mb-2 font-semibold text-sm">Password</p>
                        <input
                            type="email"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div className='flex gap-5'>
                    <input type="checkbox" name="Subject" value="Subject"/>
                    <p>Remember me</p>
                    </div>
                    <div className='flex gap-5'>
                    <button className="w-full md:w-[215px] h-[48px] border border-black rounded-xl mt-4">
                        Submit
                    </button>
                    <p className='m-7'>Lost Your Password?</p>
                    </div>
                </div>

                <div className="flex flex-col gap-4">
                    <h1 className='text-3xl font-semibold'>Register</h1>
                    <div>
                        <p className="mb-2">Email Address</p>
                        <input
                            type="text"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div>
                        <p className="mb-2 text-sm">A link to set a new password will be sent to your email <br />address.</p>
                        <p className='text-sm mb-2'>Your personal data will be used to support your <br />experience throughout this website, to manage access <br />to your account, and for other purposes described in our <br /><span className='font-bold'>privacy policy.</span> </p>
                    </div>
                    <div className='flex gap-5'>
                    <button className="w-full md:w-[215px] h-[48px] border border-black rounded-xl mt-6">
                        Register
                    </button>
                    </div>
                </div>
                </div>
                            {/* Info Section */}
            <div className="flex flex-col md:flex-row justify-center items-center gap-8 bg-[#FAF4F4] p-8 md:p-16">
                <div className="text-center md:text-left">
                    <h1 className="text-xl font-bold">Free Delivery</h1>
                    <p className="text-[#9F9F9F] text-sm">
                        For all orders over $50, consectetur adipiscing elit.
                    </p>
                </div>
                <div className="text-center md:text-left">
                    <h1 className="text-xl font-bold">90 Days Return</h1>
                    <p className="text-[#9F9F9F] text-sm">
                        For all orders over $50, consectetur adipiscing elit.
                    </p>
                </div>
                <div className="text-center md:text-left">
                    <h1 className="text-xl font-bold">Secure Payment</h1>
                    <p className="text-[#9F9F9F] text-sm">
                        For all orders over $50, consectetur adipiscing elit.
                    </p>
                </div>
            </div>

            <Footer/>
    </div>
  )
}

export default Page