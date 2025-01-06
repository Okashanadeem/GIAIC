import { defineType } from 'sanity';

export const testSchema = defineType({
  name: 'test',
  title: 'Test Profile',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Test Name',
      type: 'string',
    },
    {
        name: 'Image',
        title: 'Test Image',
        type: 'image',
      },
  ],
});