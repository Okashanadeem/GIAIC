import React from 'react';
import Navbar from '../myComponents/Navbar';
import Image from 'next/image';
import logo from '../../public/images/Meubel House_Logos-05.png';
import { ChevronRight, Clock, MapPin, Phone } from 'lucide-react';
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
                    <h1 className="text-4xl">Contact</h1>
                    <p className="flex items-center text-sm">
                        Home <ChevronRight /> Contact
                    </p>
                </div>
            </div>

            {/* Contact Info */}
            <div className="text-center px-4 md:px-8 lg:px-16">
                <h1 className="text-2xl font-bold mt-5">Get In Touch With Us</h1>
                <p className="text-[#9F9F9F] mt-3 text-sm">
                    For More Information About Our Product & Services, Please Feel Free To Drop Us <br className="hidden md:block" />
                    An Email. Our Staff Always Be There To Help You Out. Do Not Hesitate!
                </p>
            </div>

            {/* Contact Details & Form */}
            <div className="flex flex-col md:flex-row justify-center gap-10 m-8 lg:gap-24 lg:px-16">
                {/* Contact Details */}
                <div className="flex flex-col gap-8">
                    <div className="flex items-start gap-3">
                        <MapPin className="text-gray-600" />
                        <div>
                            <h1 className="font-bold">Address</h1>
                            <p>
                                236 5th SE Avenue, New <br />
                                York NY10000, United States
                            </p>
                        </div>
                    </div>
                    <div className="flex items-start gap-3">
                        <Phone className="text-gray-600" />
                        <div>
                            <h1 className="font-bold">Phone</h1>
                            <p>
                                Mobile: +84 546-6789 <br />
                                Hotline: +84 456-6789
                            </p>
                        </div>
                    </div>
                    <div className="flex items-start gap-3">
                        <Clock className="text-gray-600" />
                        <div>
                            <h1 className="font-bold">Working Time</h1>
                            <p>
                                Monday-Friday: 9:00 - 22:00 <br />
                                Saturday-Sunday: 9:00 - 21:00
                            </p>
                        </div>
                    </div>
                </div>

                {/* Contact Form */}
                <div className="flex flex-col gap-4">
                    <div>
                        <p className="mb-2">Your Name</p>
                        <input
                            type="text"
                            placeholder="Abc"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div>
                        <p className="mb-2">Email Address</p>
                        <input
                            type="email"
                            placeholder="Abc@def.com"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div>
                        <p className="mb-2">Subject</p>
                        <input
                            type="text"
                            placeholder="This is optional"
                            className="border w-full md:w-[345px] h-[50px] rounded p-2"
                        />
                    </div>
                    <div>
                        <p className="mb-2">Message</p>
                        <textarea
                            placeholder="Hi! I would like to ask about..."
                            className="border w-full md:w-[345px] h-[90px] rounded p-2"
                        />
                    </div>
                    <button className="w-full md:w-[237px] h-[48px] border border-black rounded-xl mt-4">
                        Submit
                    </button>
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

            <Footer />
        </div>
    );
};

export default Page;
