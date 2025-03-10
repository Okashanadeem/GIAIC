"use client";
import { Bot } from "lucide-react";
import { useState, useEffect } from "react";

const messages = [
  "Let me assist you with AI automation...",
  "Your AI-powered assistant is here...",
  "Enhancing intelligence with autonomy...",
];

const TypingBubble = () => {
  const [currentText, setCurrentText] = useState("");
  const [messageIndex, setMessageIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    const typeSpeed = isDeleting ? 50 : 100;
    const delayBeforeDelete = 1500;

    if (!isDeleting && charIndex < messages[messageIndex].length) {
      setTimeout(() => {
        setCurrentText((prev) => prev + messages[messageIndex][charIndex]);
        setCharIndex((prev) => prev + 1);
      }, typeSpeed);
    } else if (isDeleting && charIndex > 0) {
      setTimeout(() => {
        setCurrentText((prev) => prev.slice(0, -1));
        setCharIndex((prev) => prev - 1);
      }, typeSpeed);
    } else if (!isDeleting && charIndex === messages[messageIndex].length) {
      setTimeout(() => setIsDeleting(true), delayBeforeDelete);
    } else if (isDeleting && charIndex === 0) {
      setIsDeleting(false);
      setMessageIndex((prev) => (prev + 1) % messages.length);
    }
  }, [charIndex, isDeleting]);

  return (
    <div className="mt-16 flex flex-wrap items-center justify-center gap-6">
    <div className="w-full flex md:w-[600px] justify-center px-4">
      {/* Outer Black Box with Fixed Width for Large Screens, Responsive for Small Screens */}
      <div className="bg-black/30 backdrop-blur-lg shadow-xl z-50 p-6 rounded-2xl border border-gradient-to-r from-purple-500 to-cyan-400 
          w-full max-w-[600px] flex items-center justify-between">
        
        {/* Inner Chat Bubble (Adjusts Responsively) */}
        <div className="bg-white/10 backdrop-blur-xl rounded-2xl p-3 border border-white/20 shadow-lg 
            w-[75%] max-w-[480px] bg-[radial-gradient(circle_at_top_left,_rgba(255,255,255,0.1),_rgba(0,0,0,0.2))]">
          <p className="text-gray-300 text-lg font-medium leading-relaxed tracking-wide">
            {currentText}
            <span className="inline-block w-0.5 h-5 ml-1 bg-purple-500 animate-pulse rounded shadow-lg"></span>
          </p>
        </div>

        {/* Bot Icon Inside a Textured Box */}
        <div className="w-12 h-12 md:w-16 md:h-16 rounded-full bg-gradient-to-br from-purple-700 via-blue-500 to-cyan-400 
            flex items-center justify-center shadow-lg  border border-white/20">
          <Bot className="w-8 h-8 md:w-10 md:h-10 text-white drop-shadow-lg" />
        </div>
      </div>
    </div>
    <div className="flex flex-wrap gap-4 justify-center sm:justify-start">
    <button className="relative px-6 py-3 h-14 rounded-lg bg-gradient-to-r from-purple-600 to-blue-500 text-white font-medium transition-all duration-300 shadow-lg 
      hover:scale-105 hover:shadow-xl active:scale-95 overflow-hidden group">
  Deploy Your AI Agent

  {/* Top-Right to Center Line */}
  <span className="absolute top-0 right-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

  {/* Bottom-Left to Center Line */}
  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

  {/* Diagonal Lines Animation */}
  <span className="absolute top-0 left-0 h-full border-l-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
  <span className="absolute bottom-0 right-0 h-full border-r-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
</button>


    <button className="bg-gradient-to-r from-blue-500 to-orange-700 relative px-6 py-3 h-14 rounded-lg text-white font-medium transition-all duration-300 shadow-lg 
      hover:scale-105 hover:shadow-xl active:scale-95 overflow-hidden group">
  Watch Demo

  {/* Top-Right to Center Line */}
  <span className="absolute top-0 right-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

  {/* Bottom-Left to Center Line */}
  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

  {/* Diagonal Lines Animation */}
  <span className="absolute top-0 left-0 h-full border-l-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
  <span className="absolute bottom-0 right-0 h-full border-r-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
</button>

  </div>
    </div>
  );
};

export default TypingBubble;
