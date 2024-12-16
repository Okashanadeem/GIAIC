import Image from "next/image";
import img from "../images/facebook.svg";

function page() {
  return (
<div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {/* Facebook Logo */}
      <div className="mb-2">
        <Image src={img} alt="Facebook Logo" width={300} height={100} />
      </div>

      {/* Login Form */}
      <div className="bg-white shadow-md rounded-lg p-8 w-96">
        <p className="text-black text-center text-xl font-bold mb-2">Log in to Facebook</p>
        <form>
          <input
            type="text"
            placeholder="Email or phone number"
            className="w-full mb-4 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full mb-4 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="w-full py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Log In
          </button>
        </form>
        <div className="text-center mt-4">
          <a href="#" className="text-blue-500 hover:underline">
            Forgotten password?
          </a>
        </div>
        <hr className="my-4" />
        <div className="text-center">
          <button
            className="w-full py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500"
          >
            Create New Account
          </button>
        </div>
      </div>
    </div>
  )
}

export default page
