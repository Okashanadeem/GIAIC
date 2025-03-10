import React from 'react'
import ProductSection from './productSection'
import Image from 'next/image'
import playstation from "../../public/images/Frame 684.png"
import womensCollection from "../../public/images/Frame 685.png"
import Speakers from "../../public/images/Frame 686.png"
import perfume from "../../public/images/Frame 687.png"


const Featured = () => {
    return (
        <div className='hidden md:block'>
            {/* Product Section */}
            <div className="md:ml-[100px] m-auto max-w-[1170px] px-4">
                <div className="flex flex-col gap-6 md:flex-row md:items-center justify-between px-4">
                    {/* Product Section Content */}
                    <div className="flex flex-col items-center md:items-start text-center md:text-left space-y-4 w-full md:w-auto">
                        <ProductSection
                            heading="Flash Sales"
                            subHeading="Today's"
                            showTime={false} // Show the timer section
                            action={null} // Leave action outside for better alignment on small screens
                            product={[]} // Pass your product list or keep as an empty array for now
                            isCarousal={false} // Disable carousel behavior
                        />
                    </div>
                </div>
            </div>
            {/* Featured Items  */}
            <div className='flex m-auto max-w-[1080px] px-4 mt-10 gap-5'>
                <div className=''><Image src={playstation} alt='Playstation 5' className='w-[570px] h-[589px]' /></div>
                <div >
                    <div><Image src={womensCollection} alt='Womens Collection' className='w-[570px] h-[284px] mb-5' /></div>
                    <div className='flex gap-5'>
                        <div><Image src={Speakers} alt='Speakers' className='w-[270px] h-[284px]' /></div>
                        <div><Image src={perfume} alt='perfume' className='w-[270px] h-[284px]' /></div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Featured