// schemas/customer.js
export default {
    name: 'customer',
    title: 'Customer',
    type: 'document',
    fields: [
        {
            name: 'customerId',
            title: 'Customer ID',
            type: 'string',
        },
        {
            name: 'name',
            title: 'Name',
            type: 'string',
        },
        {
            name: 'email',
            title: 'Email',
            type: 'string',
        },
        {
            name: 'contactInfo',
            title: 'Contact Info',
            type: 'object',
            fields: [
                {
                    name: 'phone',
                    title: 'Phone',
                    type: 'string',
                },
                {
                    name: 'alternatePhone',
                    title: 'Alternate Phone',
                    type: 'string',
                },
            ],
        },
        {
            name: 'address',
            title: 'Address',
            type: 'object',
            fields: [
                {
                    name: 'street',
                    title: 'Street',
                    type: 'string',
                },
                {
                    name: 'city',
                    title: 'City',
                    type: 'string',
                },
                {
                    name: 'state',
                    title: 'State',
                    type: 'string',
                },
                {
                    name: 'postalCode',
                    title: 'Postal Code',
                    type: 'string',
                },
                {
                    name: 'country',
                    title: 'Country',
                    type: 'string',
                },
            ],
        },
    ],
};
