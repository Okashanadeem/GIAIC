import React from 'react';
import SectionHeader from './sectionHeader';
import Time from './timer'; // Ensure your `Time` component is correctly imported

interface product {
  name: string;
  image: string;
  price: number;
  rating: {
    rate: number;
    count: number;
  };
}

interface ProductSectionProps {
  heading: string;
  subHeading: string;
  showTime: boolean;
  action: React.ReactNode;
  product: product[];
  isCarousal: boolean;
  ctaText?: string;
}

const ProductSection: React.FC<ProductSectionProps> = ({
  heading,
  subHeading,
  showTime,
  action,
}) => {
  return (
    <div className="space-y-6 mt-14 flex flex-col justify-center items-center md:items-start">
      {/* Main Container with Flexbox for Section Header, Timer, and Arrows */}
      <div className="flex flex-wrap items-center justify-between md:justify-start md:gap-[87px] w-full">
        {/* Section Header */}
        <SectionHeader heading={heading} subHeading={subHeading} />

        {/* Time Display (only if showTime is true) */}
        {showTime && <Time targetTime={3 * 24 * 60 * 60} />}

        {/* Action (Arrow Buttons) */}
        <div className="flex gap-2 md:ml-auto mr-[100px]">
          {action}
        </div>
      </div>
    </div>
  );
};

export default ProductSection;
