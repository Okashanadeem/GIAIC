// schemas/deliveryZone.js
export default {
    name: 'deliveryZone',
    title: 'Delivery Zone',
    type: 'document',
    fields: [
        {
            name: 'zoneId',
            title: 'Zone ID',
            type: 'string',
        },
        {
            name: 'zoneName',
            title: 'Zone Name',
            type: 'string',
        },
    ],
};
