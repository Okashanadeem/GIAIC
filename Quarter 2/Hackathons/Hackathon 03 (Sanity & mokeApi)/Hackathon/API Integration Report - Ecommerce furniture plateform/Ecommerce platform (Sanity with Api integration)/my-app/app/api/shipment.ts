// // pages/api/shipment.js
// import axios from 'axios';

// export default async function handler(req, res) {
//   if (req.method === 'GET') {
//     const { trackingNumber } = req.query; // Get the tracking number from the query

//     // Example: Replace with your external shipment API URL and API key
//     const apiKey = 'YOUR_SHIPMENT_API_KEY';
//     const shipmentApiUrl = `https://api.example.com/track?tracking_number=${trackingNumber}&api_key=${apiKey}`;

//     try {
//       // Call the external shipment API
//       const response = await axios.get(shipmentApiUrl);
//       const shipmentData = response.data;

//       res.status(200).json(shipmentData);
//     } catch (error) {
//       console.error('Error fetching shipment data:', error);
//       res.status(500).json({ error: 'Failed to fetch shipment data' });
//     }
//   } else {
//     res.status(405).json({ message: 'Method Not Allowed' });
//   }
// }
