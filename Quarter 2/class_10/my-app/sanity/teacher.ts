import { defineType } from 'sanity';

export const teacherSchema = defineType({
  name: 'teacher',
  title: 'Teacher Profile',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Teacher Name',
      type: 'string',
    },
    {
      name: 'subject',
      title: 'Subject Taught',
      type: 'string',
    },
  ],
});
