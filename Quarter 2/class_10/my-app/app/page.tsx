import { client } from "@/sanity/lib/client";
import { GetData } from "./api/service";

interface Book {
  id: number;
  name: string;
  type: string;
}

async function sanityFetchData (){
  const fetchData = client.fetch('')
  return fetchData
}

export default async function Home() {
  const data = await GetData<Book[]>('https://simple-books-api.glitch.me/books');

  return (
    <div className="flex justify-center mt-10">
      <ol className="bg-gray-50 shadow-lg p-7 rounded-lg w-full max-w-3xl">
        <h1 className="text-2xl font-extrabold text-center mb-5 text-gray-800">Book List</h1>
        {data.map((obj) => (
          <li
            key={obj.id}
            className="flex justify-between items-center my-4 p-4 border-b border-gray-200 hover:bg-gray-100 transition duration-200"
          >
            <span>
              <h2 className="font-serif text-lg font-semibold text-gray-700">Name</h2>
              <p className="text-gray-900">{obj.name}</p>
            </span>
            <span>
              <h2 className="font-serif text-lg font-semibold text-gray-700">Type</h2>
              <p className="text-gray-900">{obj.type}</p>
            </span>
          </li>
        ))}
      </ol>
    </div>
  );
}
