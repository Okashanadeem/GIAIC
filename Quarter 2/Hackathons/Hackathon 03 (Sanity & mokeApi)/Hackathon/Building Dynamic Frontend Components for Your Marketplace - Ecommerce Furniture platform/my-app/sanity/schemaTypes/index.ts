import { type SchemaTypeDefinition } from 'sanity'
import product from '../schema/product'
import customer from '../schema/customer'
import order from '../schema/order'
import deliveryZone from '../schema/deliveryZone'

export const schema: { types: SchemaTypeDefinition[] } = {
  types: [product, customer, order, deliveryZone],
}
