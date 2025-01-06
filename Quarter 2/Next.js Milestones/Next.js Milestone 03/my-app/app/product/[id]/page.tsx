import Navbar from '@/app/myComponents/Navbar';
import { client } from '../../../sanity/lib/client'; // Sanity client import
import { notFound } from 'next/navigation'; // to handle 404
import ItemsPage from '@/app/myComponents/itemsHome';
import Footer from '@/app/myComponents/footer';

interface Product {
    _id: string;
    title: string;
    price: number;
    description: string;
    imageUrl: string;
    rating: number; // Add the rating field
}

async function getProductData(id: string): Promise<Product> {
    const data = await client.fetch(
        `*[_type == "product" && _id == $id]{_id, title, price, description, "imageUrl": image.asset->url, rating}`,
        { id }
    );

    if (data.length === 0) {
        return notFound(); // If no product is found, show 404
    }

    return data[0];
}

const ProductPage = async ({ params }: { params: { id: string } }) => {
    const { id } = params;
    const product = await getProductData(id);

    // Function to render stars based on rating
    const renderStars = (rating: number) => {
        const stars = [];
        for (let i = 0; i < 5; i++) {
            stars.push(
                <span
                    key={i}
                    className={`inline-block ${i < rating ? 'text-yellow-500' : 'text-gray-300'}`}
                >
                    ★
                </span>
            );
        }
        return stars;
    };

    return (
        <div>
            <Navbar />
            <div className="flex flex-col sm:flex-row p-8">
                <div className="sm:w-1/2 mb-4 sm:mb-0">
                    <img
                        src={product.imageUrl}
                        alt={product.title}
                        className="w-full h-96 rounded-lg"
                    />
                </div>
                <div className="sm:w-1/2 sm:pl-8">
                    <h1 className="text-3xl font-bold">{product.title}</h1>
                    <p className="text-xl font-semibold text-gray-700">${product.price}</p>

                    {/* Rating Section */}
                    <div className="flex mt-2">
                        {renderStars(product.rating)}
                    </div>

                    <p className="mt-4">{product.description}</p>

                    {/* Predefined Sizes */}
                    <div className="mt-4">
                        <h2 className="text-sm text-[#9F9F9F]">Size</h2>
                        <div className="flex gap-4">
                            <div>
                                <input
                                    type="radio"
                                    id="s"
                                    name="size"
                                    value="S"
                                    className="mr-2"
                                />
                                <label htmlFor="s">L</label>
                            </div>
                            <div>
                                <input
                                    type="radio"
                                    id="xl"
                                    name="size"
                                    value="XL"
                                    className="mr-2"
                                />
                                <label htmlFor="xl">XL</label>
                            </div>
                            <div>
                                <input
                                    type="radio"
                                    id="xs"
                                    name="size"
                                    value="XS"
                                    className="mr-2"
                                />
                                <label htmlFor="xs">XS</label>
                            </div>
                        </div>
                    </div>

                    {/* Predefined Colors */}
                    <div className="mt-4">
                        <h2 className="text-sm text-[#9F9F9F]">Color</h2>
                        <div className="flex gap-4">
                            <div>
                                <input
                                    type="radio"
                                    id="purple"
                                    name="color"
                                    value="Purple"
                                    className="mr-2"
                                    style={{ backgroundColor: 'purple' }}
                                />
                                <label htmlFor="purple">Purple</label>
                            </div>
                            <div>
                                <input
                                    type="radio"
                                    id="black"
                                    name="color"
                                    value="Black"
                                    className="mr-2"
                                    style={{ backgroundColor: 'black' }}
                                />
                                <label htmlFor="black">Black</label>
                            </div>
                            <div>
                                <input
                                    type="radio"
                                    id="skin"
                                    name="color"
                                    value="Skin"
                                    className="mr-2"
                                    style={{ backgroundColor: 'peachpuff' }}
                                />
                                <label htmlFor="skin">Skin Color</label>
                            </div>
                        </div>
                    </div>
                    
                    <div className="flex gap-3">
                        <button className="w-full sm:w-[123px] h-[48px] border border-black rounded-xl mt-4">
                            1
                        </button>
                        <button className="w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4">
                            Add To Cart
                        </button>
                    </div>
                </div>
            </div>

            <hr />

            <div>
                <div className="flex justify-around mt-7">
                    <p className="text-black text-lg">Description</p><p className="text-[#9F9F9F] text-lg">Additional Information</p><p className="text-[#9F9F9F] text-lg">Reviews 5</p>
                </div>
                <div className="md:mx-28 mx-3 text-sm text-[#9F9F9F] my-9">
                    <p>
                        Embodying the raw, wayward spirit of rock roll, the Kilburn portable active stereo speaker takes the unmistakable look and sound of Marshall, unplugs the chords, and takes the show on the road. <br /><br />
                        Weighing in under 7 pounds, the Kilburn is a lightweight piece of vintage-styled engineering. Setting the bar as one of the loudest speakers in its class, the Kilburn is a compact, stout-hearted hero with a well-balanced audio that boasts a clear midrange and extended highs for a sound that is both articulate and pronounced. The analogue knobs allow you to fine-tune the controls to your personal preferences, while the guitar-influenced leather strap enables easy and stylish travel.
                    </p>
                </div>

                <hr />
                <ItemsPage />

                <Footer />
            </div>
        </div>
    );
};

export default ProductPage;
