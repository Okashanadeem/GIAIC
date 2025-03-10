'use client'
import React, { useEffect, useState } from "react";

interface TimerProps {
  targetTime: number; // Time in seconds
}

const Time: React.FC<TimerProps> = ({targetTime }) => {
  const [timeLeft, setTimeLeft] = useState(targetTime);

  useEffect(() => {
    if (timeLeft <= 0) return; // Stop the timer if it reaches zero
    const interval = setInterval(() => {
      setTimeLeft((prev) => prev - 1); // Decrement time
    }, 1000);

    return () => clearInterval(interval); // Cleanup the interval on unmount
  }, [timeLeft]);

  // Calculate days, hours, minutes, and seconds
  const days = Math.floor(timeLeft / (24 * 60 * 60));
  const hours = Math.floor((timeLeft % (24 * 60 * 60)) / (60 * 60));
  const minutes = Math.floor((timeLeft % (60 * 60)) / 60);
  const seconds = timeLeft % 60;

  return (
    <div className="text-center space-y-4 pt-8 ml-6">
      <div className="flex justify-center space-x-4">
        <div>
          <p className="text-sm">Days</p>
          <p className="text-3xl font-bold">{days}</p>
        </div>
        <span className="text-[#E07575] text-xl w-[4px] h-[14px] py-4">:</span>
        <div>
          <p className="text-sm">Hours</p>
          <p className="text-3xl font-bold">{hours}</p>
        </div>
        <span className="text-[#E07575] text-xl w-[4px] h-[14px] py-4">:</span>
        <div>
          <p className="text-sm">Minutes</p>
          <p className="text-3xl font-bold">{minutes}</p>
        </div>
        <span className="text-[#E07575] text-xl w-[4px] h-[14px] py-4">:</span>
        <div>
          <p className="text-sm">Seconds</p>
          <p className="text-3xl font-bold">{seconds}</p>
        </div>
      </div>
    </div>
  );
};

export default Time;
