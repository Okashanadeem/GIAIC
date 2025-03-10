import React from 'react'
import { Facebook, Instagram, Linkedin, QrCode, SendHorizonal, Twitter } from 'lucide-react'
import qrcode from "../../public/images/Frame 719.png"
import Image from 'next/image'

const Footer = () => {
    return (
        <>
            <div className='w-auto h-[440px] bg-black flex text-white pt-16 px-24 gap-12'>
                <div>
                    <h1 className='mb-5 text-xl font-bold'>Exclusive</h1>
                    <p className='mb-5'>Subscribe</p>
                    <p className='mb-5'>Get 10% off your first order</p>
                    <div className="relative hidden md:flex">
                        <input type="text" placeholder='Enter your email' className='bg-black border-gray-400 outline rounded h-10 w-52 p-1' />
                        <SendHorizonal className="absolute top-2 right-2 text-gray-500" />
                    </div>
                </div>
                <div>
                    <h1 className='mb-5 text-xl'>Support</h1>
                    <p className='mb-5 text-sm'>111 Bijoy sarani, Dhaka, <br />DH 1515, Bangladesh.</p>
                    <p className='mb-5  text-sm'>exclusive@gmail.com</p>
                    <p className=' text-sm'>+88015-88888-9999</p>
                </div>
                <div>
                    <h1 className='mb-5 text-xl'>Account</h1>
                    <p className='mb-5  text-sm'>My Account</p>
                    <p className='mb-5  text-sm'>Login / Register</p>
                    <p className='mb-5  text-sm'>Wishlist</p>
                    <p className=' text-sm'>Shop</p>
                </div>
                <div>
                    <h1 className='mb-5 text-xl'>Quick Link</h1>
                    <p className='mb-5  text-sm'>Privacy Policy</p>
                    <p className='mb-5  text-sm'>Terms Of Use</p>
                    <p className='mb-5  text-sm'>FAQ</p>
                    <p className=' text-sm'>Contact</p>
                </div>
                <div>
                    <h1 className='mb-5 text-xl'>Download App</h1>
                    <p className='text-xs text-[#FAFAFA] mb-5'>Save $3 with App New User Only</p>
                    <div className='mb-5'><Image src={qrcode} alt='Qrcode' /></div>
                    <div className='flex gap-5'>
                        <Facebook />
                        <Twitter />
                        <Instagram />
                        <Linkedin />
                    </div>
                </div>
            </div>
            <p className='text-center bg-black text-gray-400 pb-2'>Copyright Rimel 2022. All right reserved</p>
        </>
    )
}

export default Footer