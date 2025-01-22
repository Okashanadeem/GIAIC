// schemas/order.js
export default {
    name: 'order',
    title: 'Order',
    type: 'document',
    fields: [
        {
            name: 'orderId',
            title: 'Order ID',
            type: 'string',
        },
        {
            name: 'customerId',
            title: 'Customer ID',
            type: 'string',
        },
        {
            name: 'orderDetails',
            title: 'Order Details',
            type: 'array',
            of: [
                {
                    type: 'object',
                    fields: [
                        {
                            name: 'productId',
                            title: 'Product ID',
                            type: 'string',
                        },
                        {
                            name: 'quantity',
                            title: 'Quantity',
                            type: 'number',
                        },
                    ],
                },
            ],
        },
        {
            name: 'totalAmount',
            title: 'Total Amount',
            type: 'number',
        },
        {
            name: 'status',
            title: 'Status',
            type: 'string',
            options: {
                list: [
                    { title: 'Pending', value: 'pending' },
                    { title: 'Shipping', value: 'shipping' },
                    { title: 'Delivered', value: 'delivered' },
                ],
            },
        },
        {
            name: 'orderDate',
            title: 'Order Date',
            type: 'datetime',
        },
    ],
};
