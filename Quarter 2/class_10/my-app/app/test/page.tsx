'use client'
import React, { useEffect, useState } from 'react';
import client from '../../sanity/lib/client'; // Path to your Sanity client file

interface Profile {
  name: string;
  imageUrl?: string;
}

const TestProfiles: React.FC = () => {
  const [profiles, setProfiles] = useState<Profile[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await client.fetch<Profile[]>(`*[_type == "test"]{
          name,
          "imageUrl": Image.asset->url
        }`);
        setProfiles(data);
      } catch (err) {
        setError('Failed to load profiles.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h1>Test Profiles</h1>
      {profiles.length > 0 ? (
        profiles.map((profile, index) => (
          <div key={index} style={{ marginBottom: '20px' }}>
            <h2>{profile.name}</h2>
            {profile.imageUrl && (
              <img
                src={profile.imageUrl}
                alt={profile.name}
                style={{ maxWidth: '200px', borderRadius: '8px' }}
              />
            )}
          </div>
        ))
      ) : (
        <div>No profiles found.</div>
      )}
    </div>
  );
};

export default TestProfiles;
