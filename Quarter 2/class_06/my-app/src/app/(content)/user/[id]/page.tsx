import { notFound } from 'next/navigation';

async function UserId({ params }: { params: { id: string } }) {
  const {id} = await  params
  const userId = Number(id)

  if (userId > 20) {
    notFound();
  }

  return (
    <div>
      <h1>User ID: {userId}</h1>
    </div>
  );
}

export default UserId;